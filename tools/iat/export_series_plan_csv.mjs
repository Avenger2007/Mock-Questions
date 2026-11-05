// Run a copy from /tmp/iat-plan-authoring with node_modules linked to the primary runtime.
// Input is metadata assembled from canonical questions and literal future briefs; no question authoring.
import fs from 'node:fs/promises';
import path from 'node:path';
import {createHash} from 'node:crypto';
import {Workbook} from '@oai/artifact-tool';
const root=process.env.IAT_REPO_ROOT;if(!root)throw new Error('IAT_REPO_ROOT required');
const d=JSON.parse(await fs.readFile(path.join(root,'tmp/iat_plan/plan_data.json'),'utf8'));
const w=Workbook.create();
const outputs=[['plan','25-test plan','iat_25_test_plan.csv'],['coverage','Syllabus scope','iat_syllabus_coverage.csv']];
const letter=n=>{let r='';for(n++;n;n=Math.floor((n-1)/26))r=String.fromCharCode(65+(n-1)%26)+r;return r;};
for(const [key,name,file] of outputs){
 const rows=d[key];const sh=w.worksheets.add(name);
 sh.getRange(`A1:${letter(rows[0].length-1)}${rows.length}`).values=rows;
 const actual=sh.getRange(`A1:${letter(rows[0].length-1)}${rows.length}`).values;
 if(JSON.stringify(actual)!==JSON.stringify(rows))throw new Error('Round-trip changed metadata');
 const quote=v=>'"'+String(v??'').replaceAll('"','""')+'"';
 await fs.writeFile(path.join(root,'docs/blueprints',file),'\ufeff'+actual.map(r=>r.map(quote).join(',')).join('\r\n')+'\r\n');
 console.log(file,actual.length-1,'records; workbook cell round-trip exact');
}

const checkPath=path.join(root,'docs/blueprints/iat_coverage_plan_check.json');
const check=JSON.parse(await fs.readFile(checkPath,'utf8'));
for(const [name,file] of [['plan_csv_sha256','iat_25_test_plan.csv'],['coverage_csv_sha256','iat_syllabus_coverage.csv']])check[name]=createHash('sha256').update(await fs.readFile(path.join(root,'docs/blueprints',file))).digest('hex');
await fs.writeFile(checkPath,JSON.stringify(check,null,2)+'\n');
