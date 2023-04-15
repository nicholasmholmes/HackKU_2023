const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');

const card = new Card('heart', 'king', 50, 50, 100, 150, 'red');

canvas.width = window.innerWidth;
canvas.height = window.innerWidth;

function drawCard() {
  ctx.fillStyle = card.color;
  ctx.fillRect(card.x, card.y, card.width, card.height);
}

function clearCanvas() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
}

function mainLoop() {
  clearCanvas();
  drawCard();
}

canvas.addEventListener('mousedown', (event) => {
  card.startDrag(event);
});

canvas.addEventListener('mouseup', (event) => {
  card.stopDrag(event);
});

canvas.addEventListener('mousemove', (event) => {
  card.onDrag(event);
});

setInterval(mainLoop, 16); // 60 FPS
