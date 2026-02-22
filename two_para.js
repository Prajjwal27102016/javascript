const btn = document.getElementById('fetchBtn');
const p1 = document.getElementById('display1');
const p2 = document.getElementById('display2');

btn.addEventListener('click', () => {
    const titleText = document.title;
    p1.textContent = titleText;
    p2.textContent = titleText;
});