'use strict'

function makeArray (col, row) {
    let arr = new Array(col);
    for (let i = 0; i < arr.length; i++) {
        arr[i] = new Array(row);
    }
    return arr;
}

function fillArray () {
    
    let grid = makeArray(cols, rows);
    for (let i = 0; i < cols; i++) {
        for (let j = 0; j < rows; j++) {
            grid[i][j] = 0
            
        }
    }
    return grid;
}

function fillRandom () {

    // clearing previous "white" class
    let outerDivs = document.querySelectorAll('.container > div')
    for (let i = 0; i < cols; i++) {
        let innerDivs = outerDivs[i].querySelectorAll('.container > div > div')
        for (let j = 0; j < rows; j++) {
            innerDivs[j].classList.remove('white')
        }
    }

    for (let i = 0; i < cols; i++) {
        for (let j = 0; j < rows; j++) {
            grid[i][j] = Math.round(Math.random()) 
        }
    }
    for (let i = 0; i < cols; i++) {
        let innerDivs = outerDivs[i].querySelectorAll('.container > div > div')
        for (let j = 0; j < rows; j++) {
            if (grid[i][j] == 1) {
                innerDivs[j].classList.add('white')
            }
        }
    }
}

function updateState () {
    if (canvas.getContext) {
        let ctx = canvas.getContext('2d');
        for (let i = 0; i < cols; i++) {
            for (let j = 0; j < rows; j++) {
                if (grid[i][j] == 0) {
        
                    ctx.fillStyle = 'black';
                    ctx.fillRect(j * res, i * res,res,res);
                } else if (grid[i][j] == 1) {
                    
                    ctx.fillStyle = 'white';
                    ctx.fillRect(j * res, i * res,res,res);
                    ctx.strokeStyle = 'black';
                    ctx.strokeRect(j * res, i * res,res,res);
                }             
            }
        }
    }
}

function counting(grid, x, y) {
    let sum = 0;
    for (let i = -1; i < 2; i++) {
        for (let j = -1; j < 2; j++) {
            let col = (x + i + cols) % cols;
            let row = (y + j + rows) % rows;
            sum += grid[col][row]
        }
    }
    sum -= grid[x][y]
    return sum;
}

function nextState () {
    let next = makeArray(cols, rows)
    for (let i = 0; i < cols; i++) {
        for (let j = 0; j < rows; j++) {

            let state = grid[i][j]

            let neighbours = counting(grid, i, j)
            if (state == 0 && neighbours == 3) {
                next[i][j] = 1;
            } else if (state == 1 && (neighbours < 2 || neighbours > 3)) {
                next[i][j] = 0;
            } else {
                next[i][j] = state;
            }
        }
    }
    grid = next;
}
var gameTimer;

function gameLoop () {
    nextState()
    updateState()
}
function gameFlow () {
    gameTimer = setInterval(gameLoop, 100)
}
function stopTimer () {

    let called = true
    
    let stopButton = document.querySelector('button:last-of-type')
    
    if (stopButton.textContent == 'STOP') {
        stopButton.textContent = 'CONTINUE';
        clearInterval(gameTimer)
        called = false
    }
    if (stopButton.textContent == 'CONTINUE' && called) {
        stopButton.textContent = 'STOP';
        gameTimer = setInterval(gameLoop, 100)

    }
    
}

let canvas = document.createElement('canvas')
canvas.style['width'] = '90%'
// document.body.appendChild(canvas)

canvas.width = 1000;
canvas.height = 500;

const res = 10;

const rows = canvas.width / res;
const cols = canvas.height / res;

let grid = fillArray()
updateState()


let body = document.querySelector('body')
let container = document.createElement('div')
container.classList.add('container')
body.appendChild(container)

let status = false

function startStatus(e) {
    if (!status) {
        status = true
    } else {
        status = false
    }
}

function checked(e) {
    if (e.altKey) {
        e.target.classList.remove('white')
    }
    e.stopPropagation()
    if (status) {
        e.target.classList.add('white')
    } else {
        return
    }
}

for (let i = 0; i < cols; i++) {
    let newRowDiv = document.createElement('div')
    for (let j = 0; j < rows; j++) {
        let newColDiv = document.createElement('div')
        newColDiv.addEventListener('mousemove', checked)
        newRowDiv.appendChild(newColDiv)
    }
    container.addEventListener('click', startStatus)
    container.addEventListener('auxclick', startStatus)
    container.appendChild(newRowDiv)
}

function drawState () {
    let outerDivs = document.querySelectorAll('.container > div')
    for (let i = 0; i < cols; i++) {
        let innerDivs = outerDivs[i].querySelectorAll('.container > div > div')
        for (let j = 0; j < rows; j++) {
            if (innerDivs[j].classList.contains('white')) {
                grid[i][j] = 1
            }
        }
    }
}


function startGame () {
    console.log('start')


    drawState()
    
    document.body.removeChild(container)
    document.body.appendChild(canvas)
    
    gameFlow()
}

document.querySelector('button:first-of-type').addEventListener('click', startGame);
document.querySelector('button:nth-of-type(2n)').addEventListener('click', fillRandom);
document.querySelector('button:last-of-type').addEventListener('click', stopTimer);

