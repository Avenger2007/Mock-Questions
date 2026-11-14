// usage: node tools/iat/check_katex.mjs "IISER/IAT TEST 1.json" — strict KaTeX+mhchem parse of every \( \) and \[ \] in a paper
import fs from 'node:fs'; import {createRequire} from 'node:module'; import path from 'node:path';
const require=createRequire(import.meta.url);
const base=process.env.IAT_NODE_MODULES||'/Users/nithishreddy/.hermes/hermes-agent/node_modules';
const katex=require(path.join(base,'katex')); require(path.join(base,'katex/dist/contrib/mhchem.min.js'));
const d=JSON.parse(fs.readFileSync(process.argv[2],'utf8')); let n=0,bad=0;
for(const q of d.questions){ const txt=[q.question,...q.options,q.explanation].join('\n');
  for(const m of txt.matchAll(/\\\((.+?)\\\)|\\\[([\s\S]+?)\\\]/g)){ n++;
    try{katex.renderToString(m[1]??m[2],{throwOnError:true,strict:'ignore',displayMode:!!m[2]});}
    catch(e){bad++;console.log(q.id,String(e.message).slice(0,160));}}}
console.log(process.argv[2],'expressions',n,'errors',bad);
