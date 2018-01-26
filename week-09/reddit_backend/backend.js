'use strict'

const express = require('express')
const bodyParser = require('body-parser')

const app = express()

const mysql = require("mysql");

const conn = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "12345",
  database: "reddit"
});

conn.connect(function(err){
  if(err){
    console.log("Error connecting to Database !");
    return;
  }
  console.log("Connection established !");
});

app.use(bodyParser.json());

app.use('/',express.static('public'))

app.get('/', function (req, res) {
  res.sendFile(__dirname + '/public/index.html');
})

app.get('/posts', function (req, res) {

  let queryString = 'SELECT * FROM data';
  conn.query(queryString, function(err, rows, fields) {
    if (err) throw err;
    res.json(rows)
  });
})

app.post('/posts', function (req, res) {
  let user = req.headers.username
  let title = req.body.title
  let url = req.body.url
  let time = Math.floor(Date.now() / 1000)
  let post  = {owner: user, timestamp: time, url: url, score: 0, title: title};

  conn.query('INSERT INTO data SET ?', post, function (error, results, fields) {
    if (error) throw error;

    res.status(200);
    res.send();
  });
})

app.delete('/posts/:id', function (req, res) {
  let id = req.params.id

  conn.query(`DELETE FROM data WHERE id = ${id};`, function (error, results, fields) {
    if (error) throw error;

    res.status(200);
    res.send();
  });
})

app.patch('/posts/:id/upvote', function (req, res) {
  let id = req.params.id

  conn.query(`UPDATE data SET score = score + 1 WHERE id = ${id};`, function (error, results, fields) {
    if (error) throw error;
  });
  conn.query(`SELECT * FROM data WHERE id = ${id};`, function (error, results, fields) {
    if (error) throw error;
    res.status(200);
    res.json(results);
  });
})

app.patch('/posts/:id/downvote', function (req, res) {
  let id = req.params.id

  conn.query(`UPDATE data SET score = score - 1 WHERE id = ${id};`, function (error, results, fields) {
    if (error) throw error;
  });
  conn.query(`SELECT * FROM data WHERE id = ${id};`, function (error, results, fields) {
    if (error) throw error;
    res.status(200);
    res.json(results);
  });
})

app.patch('/posts/:id', function (req, res) {
  let id = req.params.id
  let title = req.body.title
  let url = req.body.url
  let time = Math.floor(Date.now() / 1000)
  let escape = [title, url, time]

  conn.query(`UPDATE data SET title = ?, url = ?, timestamp = ? WHERE id = ${id}`, escape, function (error, results, fields) {
    if (error) throw error;
    res.status(200);
    res.send()
  });
})

app.post('/accounts', function (req, res) {
  let name = req.body.name
  let password = req.body.password

  conn.query(`SELECT * FROM accounts`, function (error, results, fields) {
    if (error) throw error;

    for (let i = 0; i < results.length; i++) {
      if (results[i].name == name) {
        if (results[i].password == password) {
          res.send(true)
        }
      }
    }
  })
})

app.post('/newaccounts', function (req, res) {
  let newName = req.body.name
  let newPassword = req.body.password
  let accData = {name: newName, password: newPassword}

  conn.query('INSERT INTO accounts SET ?', accData, function (error, results, fields) {
    if (error) throw error;

    res.status(200);
    res.send(true);
  })
})
   
app.listen('8080', function() {
  console.log('server is on the fly...')
})