'use strict'

const express = require('express')
const bodyParser = require('body-parser')

const XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;

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

app.post('/arrays', function (req, res) {
    let method = req.body.what
    let arr = req.body.numbers
    if (typeof method === 'undefined' || typeof arr === 'undefined') {
        res.json({"error": "Please provide what to do with the numbers!"})
    } else {
        if (method === 'sum') {
            arr = arr.reduce((a, b) => a + b, 0)
            res.json({"result": arr})
        } else if (method === 'multiply') {
            arr = arr.reduce((a, b) => a * b, 1)
            res.json({"result": arr})
        } else if (method === 'double') {
            let newArr = arr.map(function (item) {
                return item * 2
            })
            res.json({"result": newArr})       
        }
    }
})

app.post('/sith', function (req, res) {
    let sentence = req.body.text
    if (typeof sentence === 'undefined' || sentence === '') {
        res.json({"error": "Feed me some text you have to, padawan young you are. Hmmm."})
    } else {
        let httpRequest = new XMLHttpRequest();
        
        httpRequest.open('GET', 'https://yoda.p.mashape.com/yoda?sentence=' + sentence);
        httpRequest.setRequestHeader("X-Mashape-Key", "kD0uEpXfdLmshbBtzPxApb2C0lWAp1SYQo9jsn5BqjtXfvh4bu");
        httpRequest.setRequestHeader("Accept", "text/plain");
        
        httpRequest.onload = function() {
            console.log(httpRequest.responseText)
            res.json({"sith_text": httpRequest.responseText})
        }
        httpRequest.send();
    }
})

app.post('/translate', function (req, res) {
    let text = req.body.text
    let lang = req.body.lang
    if (typeof text === 'undefined' || typeof lang === 'undefined') {
        res.json({"error": "I can't translate that!"})        
    } else {
        if (lang === 'hu') {

            let isVovel = function(char){
                if (char == '' || char.length > 1) {
                  throw Error('Please, give me one character')
                } else {
                  return 'aeiouéáőűöüóí'.indexOf(char) > -1;
                }
            }

            text = text.split('');
            let teve = '';
            text.forEach(function(char){
              if (isVovel(char)){
                teve += char + 'v'+ char;
              } else {
                  teve += char
              }
            });

            res.json({
                "translated": teve,
                "lang": "teve"
            })

        } else if (lang === 'en') {

            let isVovel = function(char){
                if (char == '' || char.length > 1) {
                  throw Error('Please, give me one character')
                } else {
                  return 'aeiou'.indexOf(char) > -1;
                }
            }

            text = text.split('');
            let ubi = '';
            text.forEach(function(char){
              if (isVovel(char)){
                ubi += 'ub'+ char;
              } else {
                  ubi += char
              }
            });

            res.json({
                "translated": ubi,
                "lang": "ubi"
            })

        }
    }
})


// ub

// Create a POST /translate endpoint
// That receives a simple json object:
// {
//   "text": "Ez egy példamondat. Remélem célbatalál.",
//   "lang": "hu"
// }
// And responds with the translated text and its language:
// {
//   "translated": "Evez evegy pévéldavamovondavat. Revemévélevem cévélbavavtavalávál.",
//   "lang": "teve"
// }
// from hungarian translate to teve language
// from english translate to any form of gibberish:
// https://www.wikiwand.com/en/Gibberish_(language_game)
// if the input doesnt contain the text (and the language) or its empty, respond with:
// {
//   "error": "I can't translate that!"
// }







app.listen('8080', function() {
    console.log('server is on the fly...')
})