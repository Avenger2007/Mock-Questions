/* Render the authored JSON without modifying content or order.
 * Dependencies: playwright, katex (including mhchem), a Chromium executable.
 * Example:
 * IAT_NODE_MODULES=/path/node_modules IAT_BROWSER=/path/chromium node export_iat_review.mjs
 */
import fs from 'node:fs';
import path from 'node:path';
import {createHash} from 'node:crypto';
import {createRequire} from 'node:module';
import {fileURLToPath, pathToFileURL} from 'node:url';
const require = createRequire(import.meta.url);
const root = path.dirname(fileURLToPath(import.meta.url));
const extra = process.env.IAT_NODE_MODULES;
const get = (name) => {
  try { return require(name); }
  catch (error) {
    for (const base of [extra, process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES].filter(Boolean)) {
      try { return require(path.join(base,name)); } catch {}
    }
    throw error;
  }
};
const katex = get('katex');
get('katex/dist/contrib/mhchem.min.js');
const {chromium} = get('playwright');
const input = path.resolve(root, process.argv[2] || 'IISER/IAT TEST 1.json');
const data = JSON.parse(fs.readFileSync(input,'utf8'));
const out = path.join(root,'IISER/review');
fs.mkdirSync(out,{recursive:true});
const stem = `IAT_TEST_${data.test_number}`;
const htmlPath = path.join(out, stem+'.html');
const pdfPath = path.join(out, stem+'.pdf');
let mathCount = 0;
const esc = (s) => String(s).replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;');
function rich(text) {
  const re = /\\\(([\s\S]*?)\\\)|\\\[([\s\S]*?)\\\]/g;
  let html = '', end = 0;
  for (const match of text.matchAll(re)) {
    html += esc(text.slice(end,match.index)).replaceAll('\n','<br>');
    html += katex.renderToString(match[1] ?? match[2], {
      displayMode:match[2] !== undefined, throwOnError:true, strict:'error', output:'html',
    });
    end = match.index+match[0].length;
    mathCount++;
  }
  html += esc(text.slice(end)).replaceAll('\n','<br>');
  return html;
}
const cssPath = extra ? path.join(extra,'katex/dist/katex.min.css') : require.resolve('katex/dist/katex.min.css');
// Embed font files as data URLs so the review HTML also works offline when copied.
let katexCSS = fs.readFileSync(cssPath,'utf8').replace(/url\(([^)]+)\)/g,(_,src) => {
  const f=path.resolve(path.dirname(cssPath),src.replace(/["']/g,''));
  const ext=path.extname(f).slice(1);
  return `url(data:font/${ext};base64,${fs.readFileSync(f).toString('base64')})`;
});
function question(q,n) {
  let picture = '';
  if (q.image_reference) {
    const p=path.join(root,data.image_base_path,q.image_reference);
    picture=`<figure><img src="data:image/png;base64,${fs.readFileSync(p).toString('base64')}" alt="${esc(q.image_alt)}"><figcaption>Figure for Q${n}</figcaption></figure>`;
  }
  const lines=q.question.split('\n');
  let stemHTML='', tableRows=[];
  const flush=()=>{if(tableRows.length){stemHTML+='<table class="data-table">'+tableRows.map((line,i)=>'<tr>'+line.split('|').map(c=>`<${i?'td':'th'}>${rich(c.trim())}</${i?'td':'th'}>`).join('')+'</tr>').join('')+'</table>';tableRows=[];}};
  for(const line of lines){if(line.includes(' | '))tableRows.push(line);else{flush();stemHTML+=rich(line)+'<br>';}}flush();
  return `<article class="question" id="question-${n}"><div class="qline"><b>Q${n}</b><span>+4 / -1</span></div><div class="stem">${stemHTML}</div>${picture}<div class="options">${q.options.map(o=>`<div>${rich(o)}</div>`).join('')}</div></article>`;
}
function solution(q,n) {
  return `<article class="solution" id="solution-${n}"><h3>Q${n} <span>${esc(q.subject)} · ${esc(q.difficulty)}</span></h3><div class="topic">${esc(q.topic)} / ${esc(q.sub_topic)}</div><div class="explanation">${q.explanation.split('\n').map(line=>{
    const colon=line.indexOf(':');
    return `<p>${colon>=0&&colon<22?'<strong>'+esc(line.slice(0,colon+1))+'</strong>'+rich(line.slice(colon+1)):rich(line)}</p>`;
  }).join('')}</div></article>`;
}
let html=`<!doctype html><html lang="en"><head><meta charset="utf-8"><title>OurMocks | IAT Test ${data.test_number} | Review</title><style>${katexCSS}</style><style>
@page {size:A4; margin:18mm 17mm 18mm;}
*{box-sizing:border-box} body{font-family:Arial,'DejaVu Sans',sans-serif;font-size:10.5pt;line-height:1.48;color:#172d3b;margin:0}
h1,h2,h3,p{margin-top:0} h1{font-size:40pt;line-height:1.06;margin-bottom:15px} h2{font-size:23pt;margin-bottom:8px} h3{font-size:12pt;margin-bottom:5px}
.eyebrow{font-size:10pt;letter-spacing:2px;color:#28746c;font-weight:bold;margin-bottom:26px}.subtitle{font-size:15pt;color:#395666;margin-bottom:26px}
.badge{border-left:4px solid #28746c;background:#f0f6f5;padding:12px 15px;margin:20px 0;font-size:10pt}
.cover{break-after:page;padding-top:20px}.metrics{display:flex;border-top:1px solid #cad8dc;border-bottom:1px solid #cad8dc;padding:15px 0;gap:40px;margin:24px 0}.metrics b{display:block;font-size:21pt}.metrics span{font-size:9pt;color:#526a78}
table{width:100%;border-collapse:collapse;margin:15px 0}th,td{border-bottom:1px solid #dbe3e5;padding:8px;text-align:left}th{color:#28746c;background:#f2f6f7}
li{margin-bottom:6px}.small{font-size:9pt;color:#526a78}.section{break-before:page}.section-heading{border-bottom:2px solid #28746c;padding-bottom:12px;margin-bottom:20px}.section-heading p{margin:0;color:#526a78}
.question{break-inside:avoid;margin:0 0 19px;padding-bottom:14px;border-bottom:1px solid #dbe3e5}.qline{display:flex;justify-content:space-between;margin-bottom:7px}.qline b{font-size:12pt;color:#164f55}.qline span{font-size:8pt;color:#526a78}
.options{margin-top:9px;padding-left:12px}.options>div{margin:5px 0}figure{margin:8px auto 9px;text-align:center}figure img{width:130mm;height:97.5mm;object-fit:contain}figcaption{font-size:8pt;color:#526a78}
.katex{font-size:1.03em}.katex-display{margin:.5em 0}.key{break-before:page}.keygrid{display:grid;grid-template-columns:repeat(4,1fr);gap:13px}.keygrid table{font-size:10pt}.keygrid td{padding:5px}.solution{break-inside:avoid;margin:0 0 20px;padding-bottom:13px;border-bottom:1px solid #dbe3e5}.solution h3 span{font-size:9pt;font-weight:normal;color:#526a78;float:right}.topic{font-size:8.5pt;color:#526a78;margin-bottom:9px}.explanation p{margin:0 0 5px}.explanation strong{color:#164f55}.review-note{margin-top:24px;border:1px solid #cad8dc;padding:12px}.review-note p{margin:0 0 10px}
</style></head><body>
<section class="cover"><div class="eyebrow">OURMOCKS / SCIENCE PREPARATION</div><h1>IAT Test ${data.test_number}</h1><div class="subtitle">Question paper, answer key<br>and worked solutions</div><div class="badge"><strong>MANUAL REVIEW DRAFT</strong><br>2027 preparation using the verified 2026 pattern and stored 2026 syllabus.<br>The 2027 brochure has not been verified. Not approved for student publication.</div><div class="metrics"><div><b>60</b><span>single-correct questions</span></div><div><b>180</b><span>minutes</span></div><div><b>240</b><span>maximum marks</span></div></div><table><tr><th>Subject</th><th>Question numbers</th><th>Marks</th></tr>${data.sections.map(s=>`<tr><td>${s.title}</td><td>${s.question_range}</td><td>60</td></tr>`).join('')}</table><h3>Instructions</h3><ol>${data.instructions.slice(1).map(i=>`<li>${rich(i)}</li>`).join('')}</ol><p class="small">Fixed authored order. Figures and IDs must remain linked during review.<br>Revised 30 October 2026 · ${esc(data.test_id)} · Original AI-assisted content.</p></section>`;
for (const section of data.sections) {
  const qs=data.questions.filter(q=>q.section===section.id);
  html+=`<section class="section"><div class="section-heading"><div class="eyebrow" style="margin-bottom:7px">QUESTION PAPER / ${section.id}</div><h2>${section.title}</h2><p>Questions ${section.question_range} · 15 questions · 60 marks</p></div>${qs.map(q=>question(q,data.questions.indexOf(q)+1)).join('')}</section>`;
}
html+=`<section class="key"><div class="eyebrow">REVIEW MATERIAL / KEEP HIDDEN DURING AN ATTEMPT</div><h2>Answer key</h2><p>One correct option per question. Question and option order are fixed.</p><div class="keygrid">${data.sections.map(s=>`<div><h3>${s.title}</h3><table><tr><th>Q</th><th>Answer</th></tr>${data.questions.map((q,i)=>({q,n:i+1})).filter(r=>r.q.section===s.id).map(r=>`<tr><td>${r.n}</td><td><strong>${r.q.correct_option}</strong></td></tr>`).join('')}</table></div>`).join('')}</div><div class="review-note"><p><b>Reviewer checklist</b></p><p>Accuracy and single correct answer · Syllabus fit · Distractor quality<br>Diagram labels · Solution clarity · Difficulty and timed attempt</p><p>Reviewer: ____________________ Date: ____________________</p><p>Decision / notes: ________________________________________</p></div><p class="small" style="margin-top:20px">Editorial difficulty mix: 9 easy / 42 medium / 9 hard. These labels require human review and are not official item statistics.</p></section>`;
for (const s of data.sections) {
  html+=`<section class="section"><div class="section-heading"><div class="eyebrow" style="margin-bottom:7px">WORKED SOLUTIONS / ${s.id}</div><h2>${s.title}</h2><p>Method, reasoning and common errors</p></div>${data.questions.filter(q=>q.section===s.id).map(q=>solution(q,data.questions.indexOf(q)+1)).join('')}</section>`;
}
html+='</body></html>';
fs.writeFileSync(htmlPath,html);
const browser=await chromium.launch({executablePath:process.env.IAT_BROWSER,headless:true,
  args:['--no-sandbox','--disable-gpu','--disable-dev-shm-usage']});
try {
  const page=await browser.newPage();
  const errors=[];
  page.on('pageerror',error=>errors.push(String(error)));
  await page.goto(pathToFileURL(htmlPath).href,{waitUntil:'load'});
  await page.evaluate(()=>document.fonts.ready);
  const dom=await page.evaluate(()=>({
    questions:document.querySelectorAll('.question').length,
    solutions:document.querySelectorAll('.solution').length,
    images:[...document.images].map(i=>({ok:i.complete&&i.naturalWidth>0,alt:!!i.alt})),
    overflowing:[...document.querySelectorAll('.question,.solution')].filter(e=>e.scrollWidth>e.clientWidth+1).map(e=>e.id),
    overheight:[...document.querySelectorAll('.question,.solution')].filter(e=>e.getBoundingClientRect().height>940).map(e=>e.id),
  }));
  if(errors.length||dom.questions!==60||dom.solutions!==60||dom.images.some(i=>!i.ok||!i.alt)||dom.overflowing.length||dom.overheight.length) {
    throw Error(JSON.stringify({errors,dom}));
  }
  await page.pdf({path:pdfPath,format:'A4',printBackground:true,preferCSSPageSize:true,
    displayHeaderFooter:true,headerTemplate:'<div></div>',
    footerTemplate:'<div style="font-family:Arial;font-size:8px;width:100%;padding:0 64px;color:#526a78;display:flex;justify-content:space-between"><span>OURMOCKS · IAT TEST 1 · MANUAL REVIEW DRAFT</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>'});
  const sha = file => createHash('sha256').update(fs.readFileSync(file)).digest('hex');
  const deliveryJSON=path.join(out,stem+'.json');
  fs.copyFileSync(input,deliveryJSON);
  fs.writeFileSync(path.join(out,stem+'_render_check.json'),JSON.stringify({
    source_json:path.relative(root,input),source_json_sha256:sha(input),
    delivery_json_sha256:sha(deliveryJSON),pdf_sha256:sha(pdfPath),html_sha256:sha(htmlPath),
    image_sha256:Object.fromEntries(data.questions.filter(q=>q.image_reference).map(q=>[
      q.image_reference,sha(path.join(root,data.image_base_path,q.image_reference))])),
    math_expressions:mathCount,errors,dom},null,2)+'\n');
  console.log(JSON.stringify({pdf:pdfPath,html:htmlPath,math_expressions:mathCount,dom}));
} finally {await browser.close();}
