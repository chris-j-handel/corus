// Session v380A; this session version remains fixed.
export function prepareNames(data){
  const list=document.getElementById('number-list'),rows=document.getElementById('cycle-rows');
  const buttons=[];
  for(const entry of data.names){const b=document.createElement('button');b.type='button';b.textContent=entry.number;b.dataset.number=entry.number;b.setAttribute('aria-label',entry.name);b.addEventListener('click',()=>select(entry.number));buttons.push(b);list.append(b);}
  for(const cycle of data.cycles){
    const row=document.createElement('tr');row.dataset.root=cycle.root;
    const name=document.createElement('th');name.scope='row';name.textContent=cycle.root;
    const cell=document.createElement('td'),route=document.createElement('div');route.className='route';
    cycle.numbers.forEach((n,i)=>{const b=document.createElement('button');b.type='button';b.textContent=n;b.setAttribute('aria-label',data.names[n-1].name);b.addEventListener('click',()=>select(n));route.append(b);const arrow=document.createElement('span');arrow.textContent='→';arrow.setAttribute('aria-hidden','true');route.append(arrow);if(i===3){const first=document.createElement('span');first.textContent=cycle.numbers[0];route.append(first);}});
    const note=document.createElement('div');note.className='move-note';const changes=cycle.numbers.map((n,i)=>{const next=cycle.numbers[(i+1)%4];return n+'→'+next+': '+(n%2===next%2?'numerical parity continues':'numerical parity changes');});note.textContent=changes.join(' · ');
    cell.append(route,note);row.append(name,cell);rows.append(row);
  }
  function select(n){
    const entry=data.names[n-1];document.getElementById('whole-name').textContent=entry.name;
    document.getElementById('name-details').replaceChildren();for(const value of ['Opens '+entry.opening,entry.sides,entry.direction==='—'?'':entry.direction]){if(value){const span=document.createElement('span');span.textContent=value;document.getElementById('name-details').append(span);}}
    buttons.forEach(b=>b.setAttribute('aria-pressed',String(Number(b.dataset.number)===n)));
    const cycle=data.cycles.find(c=>c.numbers.includes(n));Array.from(rows.children).forEach(row=>row.classList.toggle('selected-row',row.dataset.root===cycle?.root));
    document.getElementById('cycle-detail').textContent=cycle?cycle.root+' · two numerical parity changes, each at n → 17 − n.':'17 joins along, opening co, at the sides social and self. These four cycles contain names 1–16.';
    window.selectedName=n;
  }
  select(1);
}
