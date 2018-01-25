'use strict'

const express = require('express')
const bodyParser = require('body-parser')

const app = express()

app.use(bodyParser.json());

app.use('/assets',express.static('assets'))

app.get('/', function (req, res) {
    res.sendFile(__dirname + '/index.html');
})

app.get('/doubling', function (req, res) {
    let input = req.query.input

    if (typeof input === 'undefined') {
        res.json({"error": "Please provide an input!" })
    } else {
        res.json({"received": Number(input), "result": Number(input * 2)})
    }
})

app.get('/greeter', function (req, res) {
    let name = req.query.name
    let title = req.query.title

    if (typeof name === 'undefined') {
        res.json({"error": "Please provide a name!" })
    } else if (typeof title === 'undefined') {
        res.json({"error": "Please provide a title!" })
    } else if (typeof name !== 'undefined' && typeof title !== 'undefined') {
        res.json({"welcome_message": `Oh, hi there ${name}, my dear ${title}!`})
    }
})

app.get('/appenda/:word', function (req, res) {
    res.json({"appended": req.params.word + "a"})
})

app.post('/dountil/:what', function (req, res) {
    let method = req.params.what
    let number = req.body.until

    if (typeof number === "undefined") {
        res.json({"error": "Please provide a number!" })
    } else if (method == "sum") {
        let sum = 0
        for (let num = 1; num <= number; num++) {
            sum += num;
        }
        res.json({"result": sum})
    } else if (method == 'factor') {
        let fact = 1;
        for (let num = 1; num <= number; num++) {
            fact *= num;
        }
        res.json({"result": fact})
    }
})

app.listen('8080', function() {
    console.log('server is on the fly...')
})