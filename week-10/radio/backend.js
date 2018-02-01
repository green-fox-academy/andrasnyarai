'use strict'

const express = require('express')
const bodyParser = require('body-parser')

const app = express()

const mysql = require("mysql");



const conn = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "12345",
  database: "radio"
});

conn.connect(function(err){
  if(err){
    console.log("Can't connect to db!");
    return
  }
  console.log("Server is on the air...");
});

app.use(bodyParser.json());

app.use('/',express.static('./'))

app.get('/', function (req, res) {
  res.sendFile(__dirname + '/index.html');
})



app.get('/music', function (req, res) {

    conn.query(`SELECT * FROM songs`, function(err, rows, fields) {
        if (err) throw err;
        res.status(200);
        res.json(rows)
    });


})

app.get('/music/favourites', function (req, res) {
    if (req.headers.favourites == 'true') {
        conn.query(`SELECT * FROM songs WHERE fav = 'true'`, function (error, results, fields) {

            res.status(200)
            res.json(results)
        })
    }
})


app.patch('/favourite', function(req, res) {
    let s_id = req.query.f
    if (s_id == 'undefined') {
        return
    }
    console.log(req.headers.method)
    console.log(s_id)
    let bool;

    if (req.headers.method == 'do') {
        bool = true
    } else {
        bool = false
    }

    conn.query(`UPDATE songs SET fav = '${bool}' WHERE s_id = ${s_id};`, function (error, results, fields) {
        res.status(200);
        if (bool) res.send(true);
        if (!bool) res.send(false);
        
    })

    
})


app.post('/playlist/:name', function (req, res) {
    let newEntry = {name: req.params.name}

    conn.query(`INSERT INTO playlists SET ?`, newEntry, function (error, results, fields) {
        if (error) throw error;
    
        res.status(200);
        res.send(true);
      })
})

app.post('/addtrack/:p_id', function (req, res) {
    let playlistName = req.params.p_id
    let trackName = req.body.id
    console.log(playlistName)
    
    conn.query(`SELECT * FROM playlists WHERE name = '${playlistName}'`, function (error, results, fields) {
        if (results.length == 0) {
            return
        }
        console.log(results[0].p_id)

        let newEntry = {s_id: trackName, p_id: results[0].p_id}

        conn.query(`INSERT INTO joined SET ?`, newEntry, function (error, results, fields) {
            if (error) throw error;
    
        })
    })
    res.status(200)
    res.send(true)
})

app.post('/delete/:p_id', function (req, res) {
    let playlistName = req.params.p_id
    console.log(playlistName)

    conn.query(`SELECT p_id FROM playlists WHERE name = '${playlistName}'`, function (error, results, fields) {
        let mark = results[0].p_id
        conn.query(`DELETE FROM playlists WHERE name = '${playlistName}'`, function (error, results, fields) {
            conn.query(`DELETE FROM joined WHERE p_id = ${mark}`, function (error, results, fields) {

            })
        })
    })

    res.status(200)
    res.send(true)

})


app.get('/music/:id', function (req, res) {
    console.log(req.params.id)
    let id = req.params.id
    conn.query(`SELECT p_id FROM playlists WHERE name = '${id}'`, function (error, results, fields) {
        console.log(results[0].p_id)
        let identicator = results[0].p_id
        conn.query(`SELECT * FROM songs JOIN joined ON songs.s_id = joined.s_id WHERE joined.p_id = ${identicator}`, function (error, results, fields) {
            console.log(results)

            res.status(200)
            res.json(results)
        })
    })
})


app.get('/playlists', function (req, res) {

    conn.query(`SELECT * FROM playlists`, function (error, results, fields) {
        if (error) throw error;

        res.status(200)
        res.json(results)
    })
})


app.listen('8080', function() {
    console.log('server is on the fly...')
  })