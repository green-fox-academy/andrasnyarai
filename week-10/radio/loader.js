'use strict'

const fs = require('fs');
const mm = require('musicmetadata');


let wStream = fs.createWriteStream('output.json', {'flags': 'w'} );
wStream.write('');
wStream.end();  


fs.readdir('./music', function (err, files) {

    let all = []
    
    files.forEach( function (file, index) {
        
        let readableStream = fs.createReadStream(`./music/${file}`);
        let writeStream = fs.createWriteStream('output.json', {'flags': 'w'} );

        
        var parser = mm(readableStream, {duration: true} ,function (err, metadata) {
            if (err) throw err;

            let music = {
                showcase: file,
                metadata: {
                    title: metadata.title,
                    artist: metadata.artist,
                    album: metadata.album,
                    duration: metadata.duration
                }
            }
            console.log(metadata.artist)
            all.push(music)
            if (index == files.length - 1) {

                writeStream.write(JSON.stringify(all));

                writeStream.on('finish', () => {  
                    console.log('wrote all data to file');
                });
                
                writeStream.end();
            }
            
            
            
            
            readableStream.close();
            
        });
    })
    
    
    
});
