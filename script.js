const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

let gridSize = 20;
let snake = [{x: 10, y: 10}];
let food = {};
let d = "RIGHT";
let score = 0;

// Controle de direção
document.addEventListener("keydown", direction);
function direction(event) {
    if(event.keyCode == 37 && d != "RIGHT") d = "LEFT";
    else if(event.keyCode == 38 && d != "DOWN") d = "UP";
    else if(event.keyCode == 39 && d != "LEFT") d = "RIGHT";
    else if(event.keyCode == 40 && d != "UP") d = "DOWN";
}

function draw() {
    // Fundo
    ctx.fillStyle = "black";
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // Cobrinha
    for(let i=0; i<snake.length; i++) {
        ctx.fillStyle = (i == 0) ? "green" : "white";
        ctx.fillRect(snake[i].x*gridSize, snake[i].y*gridSize, gridSize, gridSize);
    }

    // Comida
    ctx.fillStyle = "red";
    ctx.fillRect(food.x*gridSize, food.y*gridSize, gridSize, gridSize);

    // Posição atual da cabeça
    let snakeX = snake[0].x;
    let snakeY = snake[0].y;

    if(d == "LEFT") snakeX--;
    if(d == "UP") snakeY--;
    if(d == "RIGHT") snakeX++;
    if(d == "DOWN") snakeY++;

    // Comer comida
    if(snakeX == food.x && snakeY == food.y) {
        score++;
        spawnFood();
    } else {
        snake.pop(); // Remove cauda
    }

    let newHead = {x: snakeX, y: snakeY};

    // Game Over
    if(snakeX < 0 || snakeX >= canvas.width/gridSize || 
       snakeY < 0 || snakeY >= canvas.height/gridSize || 
       collision(newHead, snake)) {
        clearInterval(game);
        alert("Game Over! Pontuação: " + score);
        location.reload();
    }

    snake.unshift(newHead);
}

function spawnFood() {
    food = {
        x: Math.floor(Math.random() * (canvas.width/gridSize)),
        y: Math.floor(Math.random() * (canvas.height/gridSize))
    }
}

function collision(head, array) {
    for(let i=0; i<array.length; i++) {
        if(head.x == array[i].x && head.y == array[i].y) return true;
    }
    return false;
}

spawnFood();
let game = setInterval(draw, 100);

