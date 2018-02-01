const mysql = require('mysql')
let config = require('./output.json')

console.log(config[0])

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
  console.log("Server is on the air...");
});

config.forEach( function (item, index) {

    let metadata  = {url: item.showcase, title: item.metadata.title, artist: item.metadata.artist, album: item.metadata.album, duration: item.metadata.duration, fav: 'false'};
    console.log(metadata)

    conn.query('INSERT INTO songs SET ?', metadata, function (error, results, fields) {
      if (error) throw error;
    });
})




