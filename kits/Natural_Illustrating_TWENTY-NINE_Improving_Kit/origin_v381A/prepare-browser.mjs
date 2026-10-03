import fs from 'node:fs';
import path from 'node:path';
import {createRequire} from 'node:module';
import {createBrotliDecompress} from 'node:zlib';
import {pipeline} from 'node:stream/promises';
import {execFileSync} from 'node:child_process';
import os from 'node:os';
import {fileURLToPath} from 'node:url';
const require=createRequire(import.meta.url);
export async function prepareBrowser(){
  const packageEntry=require.resolve(process.env.V381A_CHROMIUM_MODULE||'@sparticuz/chromium');
  const bin=path.resolve(path.dirname(packageEntry),'../bin');
  const runtime=path.join(os.tmpdir(),'v381a-origin-render');fs.mkdirSync(runtime,{recursive:true});
  const exe=path.join(runtime,'chromium');
  await pipeline(fs.createReadStream(path.join(bin,'chromium.br')),createBrotliDecompress(),fs.createWriteStream(exe));fs.chmodSync(exe,0o755);
  for(const name of ['swiftshader','fonts']){const dest=name==='fonts'?path.join(runtime,'fonts'):runtime;fs.mkdirSync(dest,{recursive:true});const marker=path.join(runtime,name+'.ready');if(!fs.existsSync(marker)){const archive=path.join(runtime,name+'.tar');await pipeline(fs.createReadStream(path.join(bin,name+'.tar.br')),createBrotliDecompress(),fs.createWriteStream(archive));execFileSync('tar',['--no-same-owner','-xf',archive,'-C',dest]);fs.unlinkSync(archive);fs.writeFileSync(marker,'ready');}}
  const xml=s=>s.replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;');
  const bundled=path.join(path.dirname(fileURLToPath(import.meta.url)),'vendor');
  fs.writeFileSync(path.join(runtime,'fonts','fonts.conf'),'<?xml version="1.0"?><fontconfig><dir>'+xml(path.join(runtime,'fonts','fonts'))+'</dir><dir>'+xml(bundled)+'</dir><cachedir>'+xml(path.join(runtime,'font-cache'))+'</cachedir></fontconfig>');
  return {exe,runtime};
}
