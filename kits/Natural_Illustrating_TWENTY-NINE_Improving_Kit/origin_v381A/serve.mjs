import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const root=path.dirname(fileURLToPath(import.meta.url));
const types={'.html':'text/html','.js':'text/javascript','.mjs':'text/javascript','.md':'text/plain','.ttf':'font/ttf','.mp4':'video/mp4'};
http.createServer((req,res)=>{const u=new URL(req.url,'http://127.0.0.1'),p=path.resolve(root,'.'+decodeURIComponent(u.pathname==='/'?'/index.html':u.pathname));if(!p.startsWith(root+path.sep)){res.writeHead(403);res.end();return;}fs.readFile(p,(e,b)=>{if(e){res.writeHead(404);res.end();return;}res.writeHead(200,{'Content-Type':types[path.extname(p)]||'application/octet-stream'});res.end(b);});}).listen(3812,'127.0.0.1',()=>console.log('Origin study: http://127.0.0.1:3812'));
