async function loadData() {
  try {
    const response = await fetch('/api/data');
    const data = await response.json();
    const container = document.getElementById('data-container');
    data.forEach(item => {
      const div = document.createElement('div');
      div.className = 'item';
      div.innerHTML = `<h3>${item.name}</h3><p>${item.description}</p>`;
      container.appendChild(div);
    });
  } catch (err) {
    console.error('Error loading data', err);
  }
}
window.onload = loadData;
