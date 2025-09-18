async function matchName(){
  const name = document.getElementById('name').value;
  if(!name) return alert('enter name');
  const resp = await fetch('/api/match_name', {method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify({name:name, limit:10})});
  const data = await resp.json();
  document.getElementById('name_out').innerText = JSON.stringify(data, null, 2);
}
async function getRecipes(){
  const ings = document.getElementById('ings').value;
  if(!ings) return alert('enter ingredients');
  const list = ings.split(',').map(s=>s.trim()).filter(Boolean);
  const resp = await fetch('/api/get_recipes', {method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify({ingredients:list})});
  const data = await resp.json();
  document.getElementById('recipe_out').innerText = JSON.stringify(data, null, 2);
}
