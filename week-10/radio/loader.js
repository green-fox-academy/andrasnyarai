'use strict'

const fs = require('fs');
const mm = require('musicmetadata');
const mysql = require('mysql')

const conn = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "12345",
    database: "radio"
});

conn.connect(function(err){
    if(err){
        console.log("Can't connect to db!");
        return;
    }
  console.log("Connected to db...");
});

fs.readdir('./music', function (err, files) {
    files.forEach( function (file, index) {
        let readableStream = fs.createReadStream(`./music/${file}`);
        let parser = mm(readableStream, {duration: true} ,function (err, metadata) {
            if (err) throw err;

            let data  = {url: file,
                        title: metadata.title,
                        artist: metadata.artist,
                        album: metadata.album,
                        duration: metadata.duration,
                        fav: 'false'};

            conn.query('INSERT INTO songs SET ?', data, function (error, results, fields) {
              if (error) throw error;
              console.log(`wrote at ${index} ||| ` + file )
            });
            readableStream.close(); 
        });
    }) 
});
