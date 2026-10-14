// Constantes injetadas pelo build.py: TR (trechos), LEG (legendas), END, LAYER
const $ = (s) => document.querySelector(s);
const S = (id) => TR[id].start;
const tl = gsap.timeline({ paused: true });

// ---------- montagem do DOM dinamico (antes da timeline) ----------
// calendario outubro/2026 (comeca na quinta)
(function () {
  const g = $("#calgrid");
  const head = "DSTQQSS".split("");
  let html = '<div style="display:grid;grid-template-columns:repeat(7,54px);column-gap:4px;row-gap:4px;">';
  head.forEach((d) => (html += `<div style="height:36px;text-align:center;font-weight:700;font-size:20px;color:#8a847b;">${d}</div>`));
  for (let i = 0; i < 35; i++) {
    const day = i - 3;
    const ok = day >= 1 && day <= 31;
    const id = day === 25 ? ' id="d25"' : "";
    const sun = i % 7 === 0 ? "color:#8a847b;" : "";
    html += `<div${id} style="height:54px;display:flex;align-items:center;justify-content:center;border-radius:27px;font-weight:700;font-size:24px;${sun}" class="tnum">${ok ? day : ""}</div>`;
  }
  g.innerHTML = html + "</div>";
})();
// teclado da urna
(function () {
  const k = $("#keypad");
  const keys = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "", "0", ""];
  keys.forEach((n, i) => {
    if (!n) return;
    const d = document.createElement("div");
    d.className = "tecla";
    d.textContent = n;
    d.style.left = (i % 3) * 102 + "px";
    d.style.top = Math.floor(i / 3) * 82 + "px";
    k.appendChild(d);
  });
  $("#presid").innerHTML = "PRESIDENTE".split("").map((c) => `<span class="ch" style="opacity:0">${c}</span>`).join("");
})();
// mini barras das colunas (S05)
document.querySelectorAll("[data-bars]").forEach((el) => {
  const L = el.dataset.bars;
  el.innerHTML = [["Federais", 0.62], ["Estaduais", 0.26], ["Municipais", 0.12]]
    .map(([n, p], i) => `<div style="height:56px;position:relative;"><span class="kicker" style="font-size:22px;">${n}</span>
      <div class="track" style="left:0;right:0;top:32px;height:14px;"><div class="fill mb${L}" data-p="${p}" style="background:${L === "A" ? "#3d3b38" : "#85807a"};"></div></div></div>`)
    .join("");
});
// linhas da NF-e (S07)
$("#nfrows").innerHTML = [["CFOP", "5.102", 1], ["NCM", "4202.12.10", 1], ["Alíquota ICMS", "18%", 1], ["Valor total", "R$ 4.250,00", 0]]
  .map(([l, v, bad], i) => `<div class="row nfrow" style="height:86px;border-top:${i ? "2px solid #e8e5df" : "0"};position:relative;">
      <span class="kicker">${l}</span><span class="title tnum nfv${bad ? " bad" : ""}" style="font-size:31px;position:relative;">${v}
      ${bad ? '<i class="strike" style="position:absolute;left:-6px;right:-6px;top:50%;height:5px;margin-top:-2px;border-radius:3px;background:#cc3d3d;transform-origin:0 50%;display:block;"></i>' : ""}</span></div>`)
  .join("");
// checklist (S09) — cada item responde a um problema do S07
$("#chkrows").innerHTML = ["Regime tributário revisado", "Notas fiscais conferidas", "Dívidas mapeadas"]
  .map((t, i) => `<div class="chkrow" style="height:74px;display:flex;align-items:center;gap:24px;border-top:${i ? "2px solid #e8e5df" : "0"};">
      <svg width="50" height="50" viewBox="0 0 50 50"><circle class="ckc" cx="25" cy="25" r="22" fill="#e7f4ec" stroke="#23874d" stroke-width="3" style="opacity:.0"/>
        <circle cx="25" cy="25" r="22" fill="none" stroke="#d9d5ce" stroke-width="3"/>
        <path class="ckp" d="M14 26 L22 34 L37 17" fill="none" stroke="#23874d" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
      <span style="font-weight:500;font-size:34px;">${t}</span></div>`)
  .join("");
// legendas
(function () {
  const box = $("#legs");
  LEG.forEach(([txt, s], i) => {
    const tr = Object.values(TR).find((x) => s >= x.start - 1e-3 && s < x.end);
    const y = tr.layout === "B" ? 1040 : 1401;
    const cls = tr.layout === "A" ? "a" : "g";
    const d = document.createElement("div");
    d.className = "leg " + cls;
    d.id = "leg" + i;
    d.style.top = y + "px";
    d.textContent = txt;
    box.appendChild(d);
  });
})();

// ---------- helpers ----------
function dashes(sel) {
  document.querySelectorAll(sel).forEach((p) => {
    const L = p.getTotalLength();
    p.style.strokeDasharray = L;
    p.style.strokeDashoffset = L;
  });
}
function draw(sel, t, d, ease) { tl.to(sel, { strokeDashoffset: 0, duration: d, ease: ease || "power2.inOut" }, t); }
function rise(sel, t, o) {
  o = o || {};
  tl.fromTo(sel, { opacity: 0, y: o.y ?? 70, scale: o.s ?? 0.96 },
    { opacity: 1, y: 0, scale: 1, duration: o.d ?? 0.55, ease: o.ease || "power3.out" }, t);
}
function slam(sel, t, rot) {
  tl.fromTo(sel, { opacity: 0, scale: 1.9, rotation: rot - 6 },
    { opacity: 1, scale: 1, rotation: rot, duration: 0.2, ease: "power3.in" }, t - 0.2);
  tl.to(sel, { scale: 1.04, duration: 0.07, yoyo: true, repeat: 1, ease: "power1.out" }, t);
}
function shake(sel, t) {
  tl.to(sel, { keyframes: [{ x: -7 }, { x: 6 }, { x: -3 }, { x: 0 }], duration: 0.22, ease: "none" }, t);
}
function counter(el, from, to, t, d, fmt, ease) {
  const st = { v: from };
  tl.fromTo(st, { v: from }, { v: to, duration: d, ease: ease || "power2.out",
    onUpdate: () => (el.textContent = fmt(st.v)) }, t);
}
const brl = (v) => Math.round(v).toLocaleString("pt-BR");
const pct = (v) => v.toFixed(1).replace(".", ",") + "%";
const hash = (n) => { const x = Math.sin(n * 127.1 + 311.7) * 43758.5453; return x - Math.floor(x); };
// flutuacao ambiente finita (cards vivos depois de entrar)
function floatY(sel, t0, t1, amp) {
  const per = 1.6, n = Math.max(0, Math.floor((t1 - t0) / per) - 1);
  if (n < 1) return;
  tl.to(sel, { y: -(amp || 4), duration: per / 2, ease: "sine.inOut", yoyo: true, repeat: n }, t0);
}

// estados iniciais
dashes("#c25, #conA, #conB, #cxline, #anel, #cg1, #cg2, #cg3, #cg4, #cg5, .ckp, #prepck");
tl.set(".fill, .strike", { scaleX: 0 }, 0);

// =========================================================== S01 (B) gancho
{
  const t0 = S("S01");
  rise("#cal", t0 + 0.12, { y: 90 });
  floatY("#cal", t0 + 0.8, TR.S01.end, 3);
  // "dia 25" — circulo dourado desenhado e dia preenchido
  draw("#c25", 0.92, 0.42, "power2.out");
  tl.to("#d25", { backgroundColor: "#f6f0e1", color: "#8f7330", duration: 0.25 }, 1.08);
  // "eleições" — card da urna
  rise("#urnacard", 1.62, { y: 90 });
  // "segundo turno" — carimbo
  slam("#stamp1", 2.26, -9);
  shake("#cal", 2.26);
}

// =========================================================== S02 (C) urna
{
  const t0 = S("S02"), t1 = TR.S02.end;
  tl.fromTo("#urnabig", { scale: 0.93, y: 30 }, { scale: 1, y: 0, duration: 0.45, ease: "power3.out" }, t0);
  tl.fromTo("#urnabig", { scale: 1 }, { scale: 1.06, duration: t1 - t0 - 0.45, ease: "none", immediateRender: false }, t0 + 0.45);
  // cursor piscando a partir de "em quem"
  tl.set("#cur", { opacity: 0 }, t0);
  const blinkT = 3.86, n = Math.floor((t1 - blinkT) / 0.26);
  for (let i = 0; i <= n; i++) tl.set("#cur", { opacity: i % 2 ? 0 : 1 }, blinkT + i * 0.26);
  // "presidente" — digitado letra a letra
  document.querySelectorAll("#presid .ch").forEach((c, i) => tl.set(c, { opacity: 1 }, 4.2 + i * 0.045));
  tl.fromTo("#kconf", { scale: 1 }, { scale: 1.08, duration: 0.3, yoyo: true, repeat: 1, ease: "sine.inOut" }, 4.2);
}

// =========================================================== S04 (B) apuracao
{
  const t0 = S("S04"), t1 = TR.S04.end;
  rise("#apur", 7.92, { y: 110 });
  tl.fromTo("#rowA", { opacity: 0, x: -40 }, { opacity: 1, x: 0, duration: 0.4, ease: "power3.out" }, 8.5);
  tl.fromTo("#rowB", { opacity: 0, x: -40 }, { opacity: 1, x: 0, duration: 0.4, ease: "power3.out" }, 8.62);
  // corrida das barras (lideranca troca) ate quase empate em "eleições"
  const st = { a: 0, b: 0 };
  const K = [[8.62, 0, 0], [9.3, 31.4, 28.9], [9.95, 42.7, 46.1], [10.6, 49.6, 50.4], [11.2, 50.8, 49.2], [11.75, 50.1, 49.9]];
  const upd = () => {
    $("#pctA").textContent = pct(st.a); $("#pctB").textContent = pct(st.b);
    gsap.set("#barA", { scaleX: st.a / 60 }); gsap.set("#barB", { scaleX: st.b / 60 });
  };
  for (let i = 1; i < K.length; i++) {
    tl.fromTo(st, { a: K[i - 1][1], b: K[i - 1][2] }, { a: K[i][1], b: K[i][2], duration: K[i][0] - K[i - 1][0],
      ease: i === K.length - 1 ? "power2.out" : "sine.inOut", onUpdate: upd, immediateRender: false }, K[i - 1][0]);
  }
  counter($("#secoes"), 87.31, 99.82, 8.5, t1 - 8.5 - 0.3, (v) => v.toFixed(2).replace(".", ",") + "%", "power1.out");
  // ponto ao vivo pulsando
  const pulses = Math.floor((t1 - 7.95) / 0.5) - 1;
  tl.to("#live", { opacity: 0.25, duration: 0.25, yoyo: true, repeat: pulses, ease: "sine.inOut" }, 7.95);
  // "eleições" — "quem vence?"
  tl.fromTo("#quem", { opacity: 0, y: 16 }, { opacity: 1, y: 0, duration: 0.35, ease: "back.out(2)" }, 11.62);
  tl.fromTo("#qm", { scale: 1 }, { scale: 1.35, duration: 0.18, yoyo: true, repeat: 1, ease: "power2.out" }, 11.8);
}

// =========================================================== S05 (C) mesma carga
{
  rise("#emp", S("S05") + 0.02, { y: -60, d: 0.5 });
  draw("#conA, #conB", 13.0, 0.5, "power2.out");
  rise("#colA", 13.18, { y: 80 });
  rise("#colB", 13.26, { y: 80 });
  counter($("#vA"), 0, 18430, 13.56, 0.7, brl);
  counter($("#vB"), 0, 18430, 13.56, 0.7, brl);
  document.querySelectorAll(".mbA, .mbB").forEach((f, i) =>
    tl.to(f, { scaleX: +f.dataset.p, duration: 0.6, ease: "power3.out" }, 13.7 + (i % 3) * 0.08));
  // "mesma" — sinal de igual bate entre as colunas
  tl.fromTo("#igual", { opacity: 0, scale: 2.2, rotation: -30 }, { opacity: 1, scale: 1, rotation: 0, duration: 0.24, ease: "power3.in" }, 14.36);
  shake("#colA", 14.6); shake("#colB", 14.6);
  tl.fromTo("#mesma", { opacity: 0, y: 24 }, { opacity: 1, y: 0, duration: 0.4, ease: "power3.out" }, 14.84);
  tl.fromTo("#mesmabar", { scaleX: 0 }, { scaleX: 1, duration: 0.45, ease: "power2.inOut" }, 14.95);
  floatY("#emp", 13.0, TR.S05.end, 3);
}

// =========================================================== S07 (B) sem planejamento
{
  const t1 = TR.S07.end;
  rise("#nf", 18.5, { y: 110 });
  // "erradas" — campos riscados + carimbo
  document.querySelectorAll("#nf .strike").forEach((s, i) => tl.to(s, { scaleX: 1, duration: 0.18, ease: "power2.out" }, 19.18 + i * 0.07));
  tl.to("#nf .nfv.bad", { color: "#cc3d3d", duration: 0.15 }, 19.18);
  slam("#stamp2", 19.42, -8);
  shake("#nf", 19.42);
  // "dívidas desconhecidas"
  rise("#div", 19.86, { y: 110 });
  const dv = $("#dval"), st = { k: 0 };
  tl.fromTo(st, { k: 0 }, { k: 1, duration: t1 - 19.95, ease: "none", immediateRender: false,
    onUpdate: () => {
      const step = Math.floor(tl.time() / 0.05);
      const dig = (j) => Math.floor(hash(step * 13 + j * 7) * 10);
      dv.textContent = `R$ ${dig(1)}${dig(2)}.${dig(3)}${dig(4)}${dig(5)}`;
    } }, 19.95);
  tl.fromTo("#dval", { filter: "blur(0px)" }, { filter: "blur(7px)", duration: 0.5, ease: "power1.in" }, 20.42);
  tl.fromTo("#lupa", { opacity: 0, x: -90, rotation: -12 }, { opacity: 1, x: 0, rotation: 0, duration: 0.35, ease: "power2.out" }, 20.3);
  tl.to("#lupa", { x: 170, duration: 0.55, ease: "sine.inOut" }, 20.65);
  tl.fromTo("#naoid", { opacity: 0, scale: 0.7 }, { opacity: 1, scale: 1, duration: 0.3, ease: "back.out(2.2)" }, 20.62);
  tl.fromTo("#div .q", { opacity: 0, y: 10 }, { opacity: 1, y: 0, duration: 0.2, stagger: 0.07, ease: "power2.out" }, 20.75);
}

// =========================================================== S08 (C) esperar x caixa
{
  rise("#espera", S("S08") + 0.04, { y: -60 });
  tl.to("#esp", { scaleX: 0.03, duration: 1.1, ease: "power2.out" }, 21.6);
  const turns = TR.S08.end - 21.4;
  tl.fromTo("#spin", { rotation: 0 }, { rotation: 360 * Math.floor(turns / 0.9), duration: turns, ease: "none" }, 21.4);
  ["#cg1", "#cg2", "#cg3", "#cg4", "#cg5"].forEach((p, i) => draw(p, 22.18 + i * 0.09, 0.4, "power2.out"));
  // "para resolver" — nao adianta
  slam("#stamp3", 22.8, -6);
  tl.to("#espera", { opacity: 0.55, duration: 0.3 }, 22.85);
  // "o problema do seu caixa" — saldo despencando
  rise("#caixa", 23.2, { y: 120 });
  tl.fromTo("#areaclipr", { attr: { width: 0 } }, { attr: { width: 880 }, duration: 1.2, ease: "power1.inOut" }, 23.4);
  draw("#cxline", 23.4, 1.2, "power1.inOut");
  tl.fromTo("#cxdot, #cxring", { opacity: 0 }, { opacity: 1, duration: 0.1 }, 24.5);
  counter($("#cxv"), 48900, 12350, 23.4, 1.2, (v) => "R$ " + brl(v), "power1.inOut");
  tl.to("#cxv", { color: "#cc3d3d", duration: 0.5 }, 23.9);
  tl.fromTo("#cxring", { attr: { r: 12 }, opacity: 1 }, { attr: { r: 40 }, opacity: 0, duration: 0.6, repeat: 1, ease: "power1.out" }, 24.5);
  tl.fromTo("#cxpct", { opacity: 0, scale: 0.7 }, { opacity: 1, scale: 1, duration: 0.3, ease: "back.out(2.2)" }, 24.42);
}

// =========================================================== S09 (B) com planejamento
{
  const t1 = TR.S09.end;
  rise("#chk", 24.9, { y: 110, d: 0.45 });
  const ticks = [24.98, 25.3, 25.62];
  document.querySelectorAll(".chkrow").forEach((r, i) => {
    tl.to(r.querySelector(".ckc"), { opacity: 1, duration: 0.15 }, ticks[i]);
    tl.to(r.querySelector(".ckp"), { strokeDashoffset: 0, duration: 0.25, ease: "power2.out" }, ticks[i]);
    tl.fromTo(r, { x: 0 }, { x: 8, duration: 0.1, yoyo: true, repeat: 1, ease: "power1.out" }, ticks[i]);
  });
  rise("#venc", 25.78, { y: 40, d: 0.35 });
  // vencedor alterna A/B — a empresa preparada nao depende do resultado
  const fl = $("#flip");
  for (let i = 0, t = 25.9; t < 26.8; i++, t += 0.15) {
    tl.set(fl, { textContent: i % 2 ? "A" : "B", backgroundColor: i % 2 ? "#3d3b38" : "#85807a" }, t);
    tl.fromTo(fl, { rotationX: 70 }, { rotationX: 0, duration: 0.12, ease: "power2.out", immediateRender: false }, t);
  }
  tl.set(fl, { textContent: "?", backgroundColor: "#c5a55a" }, 26.8);
  tl.fromTo("#prep", { opacity: 0, scale: 1.25, y: 10 }, { opacity: 1, scale: 1, y: 0, duration: 0.3, ease: "back.out(1.8)" }, 26.78);
  tl.to("#prepck", { strokeDashoffset: 0, duration: 0.25, ease: "power2.out" }, 26.9);
}

// =========================================================== S10 (C) marca
{
  const t0 = S("S10");
  draw("#anel", t0 + 0.06, 0.5, "power2.inOut");
  tl.fromTo("#logo", { opacity: 0, scale: 0.55 }, { opacity: 1, scale: 1, duration: 0.55, ease: "back.out(1.5)" }, 27.48);
  tl.fromTo("#logo", { boxShadow: "0 0 0px rgba(197,165,90,0)" }, { boxShadow: "0 0 90px rgba(197,165,90,.65)", duration: 0.3, yoyo: true, repeat: 1, ease: "sine.inOut", immediateRender: false }, 27.6);
  tl.fromTo("#nome", { opacity: 0, y: 26 }, { opacity: 1, y: 0, duration: 0.45, ease: "power3.out" }, 27.85);
  // "especialistas" — marca recua, card da carga tributaria entra
  tl.to("#marca", { y: -205, scale: 0.62, duration: 0.5, ease: "power3.inOut" }, 28.7);
  rise("#esp2", 28.86, { y: 160, d: 0.5 });
  tl.set("#needle", { rotation: 72, svgOrigin: "280 290" }, 0);
  tl.to("#needle", { rotation: -62, svgOrigin: "280 290", duration: 0.75, ease: "elastic.out(1, 0.55)" }, 29.74);
  tl.fromTo("#gz2", { opacity: 1 }, { opacity: 0.35, duration: 0.4 }, 29.9);
}

// =========================================================== camada OVL
{
  // etiquetas da emenda
  const tags = [["#tag01", 0.3, "S01"], ["#tag04", 7.95, "S04"], ["#tag07", 17.4, "S07"], ["#tag09", 24.95, "S09"]];
  tags.forEach(([sel, t, id]) => {
    tl.fromTo(sel, { opacity: 0, scale: 0.85, x: -30 }, { opacity: 1, scale: 1, x: 0, duration: 0.25, ease: "back.out(2)" }, t);
    tl.to(sel, { opacity: 0, duration: 0.01 }, TR[id].end - 0.005);
  });
  tl.to("#tag04dot", { opacity: 0.25, duration: 0.25, yoyo: true, repeat: Math.floor((TR.S04.end - 8.2) / 0.5) - 1, ease: "sine.inOut" }, 8.2);
  // selo JA: trechos A (posicao do Reel Pintor) e B com a Malu (canto inferior do cartao)
  ["S03", "S06"].forEach((id) => {
    tl.set("#badgeA", { opacity: 1 }, TR[id].start);
    tl.set("#badgeA", { opacity: 0 }, TR[id].end - 0.005);
  });
  ["S04", "S07", "S09"].forEach((id) => {
    tl.set("#badgeB", { opacity: 1 }, TR[id].start);
    tl.set("#badgeB", { opacity: 0 }, TR[id].end - 0.005);
  });
  // CTA
  tl.fromTo("#cta", { opacity: 0, y: 60, scale: 0.94 }, { opacity: 1, y: 0, scale: 1, duration: 0.45, ease: "back.out(1.6)" }, 30.6);
  tl.fromTo("#hand", { opacity: 0, x: 860, y: 1690 }, { opacity: 1, x: 790, y: 1548, duration: 0.42, ease: "power2.out" }, 30.78);
  tl.to("#hand", { scale: 0.88, duration: 0.08, yoyo: true, repeat: 1, transformOrigin: "30% 10%" }, 31.12);
  tl.to("#ctabtn", { scale: 0.94, duration: 0.08, yoyo: true, repeat: 1 }, 31.12);
  tl.fromTo("#ripple", { opacity: 0.9, scale: 0.6 }, { opacity: 0, scale: 4.2, duration: 0.6, ease: "power2.out" }, 31.14);
  tl.to("#ctabtn", { backgroundColor: "#c5a55a", duration: 0.2 }, 31.14);
  // legendas: entra 120 ms, sai 150 ms antes do proximo bloco (ou 0,35 s apos a fala)
  LEG.forEach(([, s, e], i) => {
    const el = $("#leg" + i);
    const nxt = LEG[i + 1] ? LEG[i + 1][1] : END;
    const out = Math.min(nxt, e + 0.35);
    const trEnd = Object.values(TR).find((x) => s >= x.start - 1e-3 && s < x.end).end;
    tl.fromTo(el, { opacity: 0 }, { opacity: 1, duration: 0.12, ease: "power1.out" }, s);
    if (out >= trEnd - 0.01 && out <= trEnd + 0.2) tl.set(el, { opacity: 0 }, trEnd - 0.005); // muda de posicao no quadro do corte
    else tl.to(el, { opacity: 0, duration: 0.15, ease: "power1.in" }, Math.min(out, END) - 0.15);
  });
}

tl.set({}, {}, END);
window.__timelines["main"] = tl;
