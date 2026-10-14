/**
 * render.mjs — Renderiza o preview HTML frame a frame via Puppeteer,
 * depois monta o vídeo final com ffmpeg (áudio original + overlay animado).
 *
 * Fluxo: Puppeteer captura PNG a 30 fps → ffmpeg junta com áudio original → MP4 final
 */
import puppeteer from 'puppeteer';
import { execSync } from 'child_process';
import { mkdirSync, existsSync, readdirSync } from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const FRAMES_DIR = path.join(__dirname, 'frames');
const FPS = 30;
const DURATION = 8.71; // seconds
const TOTAL_FRAMES = Math.ceil(DURATION * FPS);
const WIDTH = 1080;
const HEIGHT = 1920;

const SRC_VIDEO = path.join(__dirname, '..', 'drive-download-20261013T153446Z-1-001', 'IMG_2168.MOV');
const OUTPUT = path.join(__dirname, '..', 'IMG_2168_renderizado.mp4');

async function main() {
  // 1. Prepare frames dir
  if (!existsSync(FRAMES_DIR)) mkdirSync(FRAMES_DIR, { recursive: true });

  console.log(`[1/4] Extraindo frames do vídeo original (${FPS} fps)...`);
  execSync(
    `ffmpeg -y -loglevel error -i "${SRC_VIDEO}" -vf "fps=${FPS},scale=${WIDTH}:${HEIGHT}:force_original_aspect_ratio=decrease,pad=${WIDTH}:${HEIGHT}:(ow-iw)/2:(oh-ih)/2" "${FRAMES_DIR}\\base_%05d.png"`,
    { stdio: 'inherit' }
  );
  const baseCount = readdirSync(FRAMES_DIR).filter(f => f.startsWith('base_')).length;
  console.log(`   → ${baseCount} frames base extraídos`);

  // 2. Launch Puppeteer
  console.log('[2/4] Abrindo Puppeteer para renderizar overlays GSAP...');
  const browser = await puppeteer.launch({
    headless: 'shell',
    args: [
      `--window-size=${WIDTH},${HEIGHT}`,
      '--no-sandbox',
      '--disable-setuid-sandbox',
      '--disable-web-security',
      '--autoplay-policy=no-user-gesture-required',
    ],
  });

  const page = await browser.newPage();
  await page.setViewport({ width: WIDTH, height: HEIGHT, deviceScaleFactor: 1 });

  const htmlPath = `file:///${path.join(__dirname, 'preview.html').replace(/\\/g, '/')}`;
  await page.goto(htmlPath, { waitUntil: 'networkidle0', timeout: 30000 });
  await page.waitForSelector('#vid');

  // Wait for video to load
  await page.evaluate(() => new Promise((resolve) => {
    const v = document.getElementById('vid');
    if (v.readyState >= 2) return resolve();
    v.addEventListener('canplay', resolve, { once: true });
  }));

  // Pause everything
  await page.evaluate(() => {
    document.getElementById('vid').pause();
  });

  console.log(`[3/4] Capturando ${TOTAL_FRAMES} frames com overlays GSAP...`);
  for (let i = 0; i < TOTAL_FRAMES; i++) {
    const t = i / FPS;
    await page.evaluate((time) => window.__seekAndCapture(time), t);

    const framePath = path.join(FRAMES_DIR, `overlay_${String(i).padStart(5, '0')}.png`);
    await page.screenshot({ path: framePath, type: 'png' });

    if (i % 30 === 0) {
      process.stdout.write(`   → Frame ${i}/${TOTAL_FRAMES} (${(t).toFixed(1)}s)\r`);
    }
  }
  console.log(`\n   → ${TOTAL_FRAMES} frames de overlay capturados`);

  await browser.close();

  // 4. Compose final video with ffmpeg
  console.log('[4/4] Montando vídeo final com ffmpeg...');
  // Use overlay frames (they already contain the video + effects)
  // Add original audio track
  execSync(
    `ffmpeg -y -loglevel warning -framerate ${FPS} -i "${FRAMES_DIR}\\overlay_%05d.png" -i "${SRC_VIDEO}" -map 0:v -map 1:a -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p -c:a aac -b:a 192k -shortest "${OUTPUT}"`,
    { stdio: 'inherit' }
  );

  console.log(`\n✅ PRONTO! Vídeo renderizado em:\n   ${OUTPUT}`);
  console.log(`   Tamanho: ${(require('fs').statSync(OUTPUT).size / 1024 / 1024).toFixed(1)} MB`);
}

main().catch(err => {
  console.error('❌ Erro:', err.message);
  process.exit(1);
});
