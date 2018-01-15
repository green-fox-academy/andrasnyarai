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
            // grid[i][j] = Math.round(Math.random())
            grid[i][j] = 0
            
        }
    }
    return grid;
}

function drawState () {
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

function loop() {
    setTimeout(function () {
        nextState()
        drawState()
        loop();
    }, 100);
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
drawState()


let body = document.querySelector('body')
let container = document.createElement('div')
container.classList.add('container')
body.appendChild(container)

let status = false
console.log(status)

function startStatus(e) {
    if (!status) {
        status = true
    } else {
        status = false
    }
}

function checked(e) {
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
    container.appendChild(newRowDiv)
}




function startGame () {
    console.log('start')
    let outerDivs = document.querySelectorAll('.container > div')
    for (let i = 0; i < cols; i++) {
        let innerDivs = outerDivs[i].querySelectorAll('.container > div > div')
        for (let j = 0; j < rows; j++) {
            if (innerDivs[j].classList.contains('white')) {
                grid[i][j] = 1
            }
        }
    }
    document.body.removeChild(container)
    document.body.appendChild(canvas)
    
    loop()
}

document.querySelector('button').addEventListener('click', startGame);

