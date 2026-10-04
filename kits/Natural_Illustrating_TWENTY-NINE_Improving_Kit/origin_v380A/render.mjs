// Session v380A; this session version remains fixed.
import {createRequire} from 'node:module';
import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import {spawn} from 'node:child_process';
import {fileURLToPath} from 'node:url';
import {prepareBrowser} from './prepare-browser.mjs';
const require=createRequire(import.meta.url),dir=path.dirname(fileURLToPath(import.meta.url));
const {chromium}=require(process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES?process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES+'/playwright':'playwright');
const mime={'.html':'text/html','.js':'text/javascript','.mjs':'text/javascript','.ttf':'font/ttf','.md':'text/plain'};
const server=http.createServer((req,res)=>{const u=new URL(req.url,'http://127.0.0.1'),p=path.resolve(dir,'.'+decodeURIComponent(u.pathname==='/'?'/index.html':u.pathname));if(!p.startsWith(dir+path.sep)){res.writeHead(403);res.end();return;}fs.readFile(p,(e,b)=>{if(e){res.writeHead(404);res.end();return;}res.writeHead(200,{'Content-Type':mime[path.extname(p)]||'application/octet-stream'});res.end(b);});});
await new Promise(r=>server.listen(0,'127.0.0.1',r));const port=server.address().port;
let executablePath=chromium.executablePath(),args=['--disable-dev-shm-usage','--hide-scrollbars'],renderEnv=process.env;
if(!fs.existsSync(executablePath)){const pkg=require(process.env.V380A_CHROMIUM_MODULE||'@sparticuz/chromium'),portable=pkg.default||pkg,prepared=await prepareBrowser();executablePath=prepared.exe;args=[...portable.args,...args];renderEnv={...process.env,FONTCONFIG_PATH:path.join(prepared.runtime,'fonts'),FONTCONFIG_FILE:path.join(prepared.runtime,'fonts','fonts.conf'),LD_LIBRARY_PATH:prepared.runtime+(process.env.LD_LIBRARY_PATH?':'+process.env.LD_LIBRARY_PATH:'')};}
const browser=await chromium.launch({headless:true,executablePath,args,env:renderEnv});
const page=await browser.newPage({viewport:{width:1280,height:720},deviceScaleFactor:1});
const errors=[];page.on('pageerror',e=>{errors.push(e.message);console.error('Study page error:',e.message);});
page.on('console',m=>{if(m.type()==='error'||m.type()==='warning')console.error('Browser:',m.text());});
page.on('requestfailed',r=>console.error('Asset failed:',r.url(),r.failure()?.errorText));
const qa=process.env.V380A_QA_DIR||path.join(os.tmpdir(),'v380a-origin-qa');fs.mkdirSync(qa,{recursive:true});
await page.goto(`http://127.0.0.1:${port}/?capture=1`,{waitUntil:'networkidle'});await page.waitForFunction(()=>window.sceneReady===true,{},{timeout:10000});
const readings=[];for(const t of [0,1,3,4.75,5.7,8.2,10.7,13.8]){const state=await page.evaluate(t=>window.inspectFrame(t),t);readings.push(state);await page.screenshot({path:path.join(qa,'origin_'+t.toFixed(2).replace('.','_')+'.png')});}
if(readings.some(r=>r.selfScreen.some((v,i)=>v!==readings[0].selfScreen[i])))throw new Error('Self screen position changed');
if(readings.some(r=>r.fontWidth<=0))throw new Error('Study font unavailable');
const endpoints=readings.filter(r=>r.progress===1&&r.pair).map(r=>r.pair.join(','));if(new Set(endpoints).size!==4)throw new Error('Four pair endpoints not reached');
console.log('Capture endpoints:',[...new Set(endpoints)].join(' ; '),'; self position fixed.');
const examine=page;await examine.setViewportSize({width:360,height:850});
await examine.goto(`http://127.0.0.1:${port}/`,{waitUntil:'networkidle'});await examine.waitForFunction(()=>window.sceneReady===true);
await examine.getByRole('button',{name:'Next position',exact:true}).click();if((await examine.evaluate(()=>window.inspectFrame(Number(document.querySelector('#seek').value)))).position!==2)throw new Error('Next control does not advance');
await examine.screenshot({path:path.join(qa,'origin_narrow.png')});
await examine.getByRole('tab',{name:'Names · 1–17'}).click();await examine.locator('#number-list button[data-number="17"]').click();if(await examine.evaluate(()=>window.selectedName)!==17)throw new Error('Name selection did not change');
await examine.screenshot({path:path.join(qa,'names_narrow.png'),fullPage:true});
if(await examine.evaluate(()=>document.documentElement.scrollWidth>innerWidth))throw new Error('Narrow view overflows');
await examine.setViewportSize({width:320,height:850});if(await examine.evaluate(()=>document.documentElement.scrollWidth>innerWidth))throw new Error('320px view overflows');
await examine.setViewportSize({width:1080,height:950});await examine.screenshot({path:path.join(qa,'names_wide.png'),fullPage:true});
fs.writeFileSync(path.join(qa,'verification.json'),JSON.stringify({errors,readings},null,2));if(errors.length)throw new Error(errors.join('; '));console.log('Controls, name 17, narrow widths, font and page errors checked.');
if(process.argv.includes('--preview')){await browser.close();server.close();process.exit(0);}
await page.setViewportSize({width:1280,height:720});await page.goto(`http://127.0.0.1:${port}/?capture=1`,{waitUntil:'networkidle'});await page.waitForFunction(()=>window.sceneReady===true);
const output=path.join(dir,'v380A_Origin_1_to_6_First_Study.mp4'),fps=30,total=14*fps;
const ff=spawn('ffmpeg',['-hide_banner','-loglevel','error','-y','-f','image2pipe','-vcodec','mjpeg','-framerate',String(fps),'-i','pipe:0','-an','-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','-movflags','+faststart',output],{stdio:['pipe','inherit','inherit']});
const done=new Promise((resolve,reject)=>{ff.on('error',reject);ff.on('close',code=>code===0?resolve():reject(new Error('ffmpeg exit '+code)));});
for(let f=0;f<total;f++){await page.evaluate(t=>window.setTime(t),f/fps);const jpg=await page.screenshot({type:'jpeg',quality:95});if(!ff.stdin.write(jpg))await new Promise(r=>ff.stdin.once('drain',r));if(f%90===0)console.log('Rendered',f,'of',total);}
ff.stdin.end();await done;await browser.close();server.close();console.log('Origin video completed:',output);
