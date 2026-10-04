// Session v380A; this session version remains fixed.
import {studyData} from './data.js';
import {prepareNames} from './names.js';

const canvas=document.getElementById('origin-canvas'),ctx=canvas.getContext('2d');
const capture=new URLSearchParams(location.search).has('capture');
if(capture)document.body.classList.add('capture');
const starts=[0,2,4,6.5,9,11.5],duration=14;
const signs=studyData.positions,sign=p=>p>0?'+':'−';
const captions=['Beginning at 1','The pair at 1 and 2','3 opposite to 1','4 opposite to 2','5 opposite to 3','6 opposite to 4'];
const pairForms=[[1,1],[1,-1],[-1,-1],[-1,1]];
let time=0,playing=false,lastTick=0,requirements=true,width=0,height=0;
const ease=t=>t*t*(3-2*t),clamp=v=>Math.max(0,Math.min(1,v));

export function stateAt(t){
  t=Math.max(0,Math.min(duration,t));
  let index=0;for(let i=0;i<starts.length;i++)if(t>=starts[i])index=i;
  const progress=index<2?1:ease(clamp((t-starts[index]-.15)/1.25));
  const turns=Math.max(0,index-1),angle=Math.PI/4-(index<2?0:(turns-1+progress))*Math.PI/2;
  return {position:index+1,index,progress,angle,pair:index? [signs[index-1],signs[index]]:null,
    requirementAlike:index<2?'waiting':'ended at 3',
    requirementOpposite:index<2?'waiting':index<3?'following':'ended at 4'};
}

function resize(){
  width=capture?1280:Math.round(canvas.getBoundingClientRect().width);
  height=capture?720:width<500?470:Math.min(620,Math.round(width*.64));
  const ratio=capture?1:Math.min(devicePixelRatio||1,2);
  canvas.width=Math.round(width*ratio);canvas.height=Math.round(height*ratio);canvas.style.height=height+'px';ctx.setTransform(ratio,0,0,ratio,0,0);draw();
}
function text(label,x,y,size=16,color='#dcebe7',align='left',alpha=1){ctx.save();ctx.globalAlpha=alpha;ctx.fillStyle=color;ctx.font=`${size}px StudySans`;ctx.textAlign=align;ctx.textBaseline='middle';ctx.fillText(label,x,y);ctx.restore();}
function draw(){
  const s=stateAt(time),compact=width<500,large=capture,unit=Math.min(width*.25,height*.29);
  const cx=width*.5,cy=height*.445;
  const yaw=-.23,pitch=.22;
  const project=([x,y,z=0])=>{const a=x*Math.cos(yaw)+z*Math.sin(yaw),b=-x*Math.sin(yaw)+z*Math.cos(yaw),c=y*Math.cos(pitch)-b*Math.sin(pitch),d=y*Math.sin(pitch)+b*Math.cos(pitch),scale=5/(5+d);return [cx+a*unit*scale,cy-c*unit*scale,scale];};
  const bg=ctx.createLinearGradient(0,0,width,height);bg.addColorStop(0,'#0b222b');bg.addColorStop(1,'#08171d');ctx.fillStyle=bg;ctx.fillRect(0,0,width,height);
  const halo=ctx.createRadialGradient(cx,cy,0,cx,cy,unit*1.7);halo.addColorStop(0,'rgba(124,193,180,.08)');halo.addColorStop(1,'rgba(124,193,180,0)');ctx.fillStyle=halo;ctx.fillRect(0,0,width,height);
  text('1–6 · Right spiral origin',compact?18:36,large?43:27,large?25:compact?16:21);
  text('v380A',width-(compact?18:36),large?43:27,large?14:12,'#accac9','right');
  text(captions[s.index],compact?18:36,large?80:55,large?20:14,'#accac9');
  // These axes belong to the conceptual prior/now pair, not to the connector face.
  for(const axis of [0,1]){const ends=[[-1,0,0],[1.18,0,0]];if(axis===1)ends.forEach(p=>{p[1]=p[0];p[0]=0;});ctx.beginPath();ends.forEach((p,i)=>{const q=project(p);i?ctx.lineTo(q[0],q[1]):ctx.moveTo(q[0],q[1]);});ctx.strokeStyle='rgba(143,178,181,.17)';ctx.lineWidth=1;ctx.stroke();}
  text('prior',...project([1.48,0]).slice(0,2),large?15:12,'#91afb3','center');
  text('now',...project([0,1.43]).slice(0,2),large?15:12,'#91afb3','center');
  ctx.beginPath();for(let i=0;i<=128;i++){const a=i*Math.PI/64,q=project([Math.cos(a),Math.sin(a)]);i?ctx.lineTo(q[0],q[1]):ctx.moveTo(q[0],q[1]);}ctx.strokeStyle='rgba(158,207,196,.25)';ctx.lineWidth=1.3;ctx.stroke();
  pairForms.forEach((p,i)=>{const a=Math.PI/4-i*Math.PI/2,q=project([Math.cos(a)*1.22,Math.sin(a)*1.22]);text(sign(p[0])+' '+sign(p[1]),q[0],q[1],large?21:16,'#87abae','center',.85);});
  // A surface marker for the accompanied self, with no interior state.
  ctx.save();ctx.strokeStyle='rgba(205,225,218,.52)';ctx.lineWidth=1.2;ctx.beginPath();ctx.ellipse(cx,cy-24,compact?7:10,compact?9:12,0,0,Math.PI*2);ctx.stroke();ctx.beginPath();ctx.moveTo(cx-(compact?22:32),cy+13);ctx.bezierCurveTo(cx-(compact?22:32),cy-5,cx+(compact?22:32),cy-5,cx+(compact?22:32),cy+13);ctx.stroke();ctx.restore();
  text('self',cx,cy+34,large?19:15,'#dcebe7','center');
  if(s.index===0){const q=project([Math.SQRT1_2,Math.SQRT1_2,0]);plate('1'+sign(signs[0]),q[0],q[1],large?23:18);}
  else{
    const start=Math.PI/4,end=s.angle;
    ctx.beginPath();const count=Math.max(1,Math.ceil(Math.abs(end-start)*34));for(let i=0;i<=count;i++){const a=start+(end-start)*i/count,q=project([Math.cos(a),Math.sin(a)]);i?ctx.lineTo(q[0],q[1]):ctx.moveTo(q[0],q[1]);}ctx.strokeStyle='#9ed6c4';ctx.lineWidth=large?3.1:2.2;ctx.stroke();
    // Follow one continuous rotation; no reflected substitute body or zero parity.
    const q=project([Math.cos(s.angle),Math.sin(s.angle)]);
    const tangent=project([Math.cos(s.angle-.09),Math.sin(s.angle-.09)]);
    const heading=Math.atan2(tangent[1]-q[1],tangent[0]-q[0]);
    ctx.save();ctx.translate(q[0],q[1]);ctx.rotate(heading);ctx.beginPath();ctx.moveTo(8,0);ctx.lineTo(-7,-5);ctx.lineTo(-7,5);ctx.closePath();ctx.fillStyle='#bae4d3';ctx.fill();ctx.restore();
    const pair=s.pair;
    const gap=large?32:24,dy=large?32:26;
    plate(s.index+sign(pair[0]),q[0]-gap,q[1]-dy,large?22:16);
    plate((s.index+1)+sign(pair[1]),q[0]+gap,q[1]-dy,large?22:16);
    text('Pair '+s.index+'–'+(s.index+1)+' · ('+sign(pair[0])+', '+sign(pair[1])+')',compact?18:36,large?113:79,large?18:13,'#b4d5cd');
  }
  text('Reading forward · into the plane',cx,height-75,large?16:compact?12:14,'#9ebdc0','center');
  const releasing=studyData.releasings[s.index];
  text(releasing?'Releasing '+sign(releasing):'Quiet releasing',cx,cy+unit*.97+(large?25:20),large?18:compact?13:15,'#bfd9ce','center');
  if(releasing){const age=clamp((time-starts[s.index])/1.3);text(sign(releasing),cx+45+age*(compact?18:38),cy-3,large?25:18,'#a4dbc7','center',1-age*.62);}
  if(requirements){
    const base=height-(large?142:122),size=large?18:compact?12:14;
    requirement('Next alike with now',3,base,size);
    requirement('Next opposite to now',4,base+(large?29:24),size);
  }
  const gap=Math.min(72,(width-40)/6),left=cx-gap*2.5,ty=height-(large?43:28);
  signs.forEach((p,i)=>{const active=i===s.index,x=left+i*gap;ctx.beginPath();ctx.arc(x,ty,large?21:16,0,Math.PI*2);ctx.fillStyle=active?'#d6e8df':i<s.index?'#21424a':'#122c35';ctx.fill();text(String(i+1),x,ty,large?18:14,active?'#0f2a30':'#b4cece','center');});
  function plate(label,x,y,size){const w=size*2.25,h=size*1.75;ctx.save();ctx.fillStyle='#112d36';ctx.strokeStyle='#7aaba8';ctx.lineWidth=1;ctx.beginPath();ctx.roundRect(x-w/2,y-h/2,w,h,7);ctx.fill();ctx.stroke();text(label,x,y,size,'#e0eee7','center');ctx.restore();}
  function requirement(label,failure,y,size){const failed=s.position>=failure,age=time-starts[failure-1],opacity=failed?1-clamp(age/1.05):s.index<1?.52:1;
    if(opacity>.01)text(label,cx,y,size,'#cbdad5','center',opacity);
    if(failed)text('Ended at '+failure+' · '+label,cx,y,size,'#c59889','center',Math.min(1,age/.65));
  }
}

function setTime(t){time=Math.max(0,Math.min(duration,t));document.getElementById('seek').value=time;const s=stateAt(time);document.getElementById('origin-status').textContent='Position '+s.position+' · '+captions[s.index]+(s.pair?' · pair '+s.pair.map(sign).join(' '):'');document.getElementById('back').disabled=s.position===1;document.getElementById('next').disabled=s.position===6;draw();return {...s,time};}
function setPlaying(value){playing=value;document.getElementById('play').textContent=playing?'Pause':'Play';lastTick=performance.now();}
function step(delta){setPlaying(false);const n=Math.max(0,Math.min(5,stateAt(time).index+delta));setTime(starts[n]+(n>=2?1.6:0));}
function tick(now){if(playing){setTime(time+(now-lastTick)/1000);if(time>=duration)setPlaying(false);}lastTick=now;requestAnimationFrame(tick);}
document.getElementById('play').addEventListener('click',()=>{if(time>=duration)setTime(0);setPlaying(!playing);});
document.getElementById('back').addEventListener('click',()=>step(-1));document.getElementById('next').addEventListener('click',()=>step(1));
document.getElementById('seek').addEventListener('input',e=>{setPlaying(false);setTime(Number(e.target.value));});
document.getElementById('requirements').addEventListener('change',e=>{requirements=e.target.checked;draw();});
const tabs=[document.getElementById('origin-tab'),document.getElementById('names-tab')];
tabs.forEach((tab,i)=>tab.addEventListener('click',()=>{setPlaying(false);tabs.forEach((t,j)=>{t.setAttribute('aria-selected',String(i===j));document.getElementById(t.getAttribute('aria-controls')).hidden=i!==j;});if(i===0)resize();}));
prepareNames(studyData);
await document.fonts.load('20px StudySans');await document.fonts.ready;
new ResizeObserver(()=>resize()).observe(canvas);
resize();setTime(0);window.setTime=setTime;window.inspectFrame=t=>{const s=setTime(t);return {...s,selfScreen:[width*.5,height*.445],fontWidth:ctx.measureText('17').width};};window.sceneReady=true;
requestAnimationFrame(tick);
