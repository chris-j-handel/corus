const { biCoupling } = require('./resolver_pure_v265.js');
function run(N,turns,mode){
  let stands=new Map(); for(let i=0;i<N;i++) stands.set(i, i%2===0?1:-1);
  let carry=[]; const trace=[];
  for(let t=0;t<turns;t++){
    const accepted=[];
    for(let i=0;i<N;i++){
      const L=stands.get(((i-1)%N+N)%N);
      if(L) accepted.push([i,L]);
      if(mode===1){ const R=stands.get((i+1)%N); if(R) accepted.push([i,R]); }
    }
    const [seq,carries]=biCoupling(carry,accepted);
    stands=new Map();                                  // only what stands
    for(const [i,m] of seq) if(i>=0 && i<N) stands.set(i,m);
    carry=carries.slice().sort((a,b)=>a[0]-b[0]);      // the writing-down is the trace's
    const cstr=carry.map(a=>`${a[0]}:${a[1]}:${a[2]}:${a[3]}`).join(";");
    const line=[]; for(let i=0;i<N;i++) line.push(stands.get(i)??0);   // the trace's line, made here
    trace.push("S="+line.join(",")+" C="+cstr);
  }
  return trace;
}
const N=+process.argv[2],turns=+process.argv[3],mode=+process.argv[4];
console.log(JSON.stringify(run(N,turns,mode)));
