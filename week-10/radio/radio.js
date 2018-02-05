'use strict';

let audio = document.querySelector('audio')
let shuffle = false

function next (showcase, artist, title, album, s_id, fav) {

    audio.dataset.artist = artist
    audio.dataset.title = title
    audio.dataset.album = album
    audio.dataset.s_id = s_id
    audio.dataset.fav = fav

    let httpRequest = new XMLHttpRequest();
    let api = 'ee125f318852fc7d1c2f4e21458a0035'
    httpRequest.open('GET', `http://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key=${api}&artist=${artist}&album=${album}&format=json`);
    httpRequest.setRequestHeader("Accept", "application/json");
    httpRequest.onreadystatechange = function() {
    
        if(httpRequest.readyState == 4 && httpRequest.status == 200) {
            let data = JSON.parse(httpRequest.response)
            let coverart = data.album.image[2]['#text']
            console.log(data.album.image[2]['#text'])

            let imageContainer = document.querySelector('.albumart img')
            imageContainer.setAttribute('src', coverart)
        }
    }
    httpRequest.send();

    if (fav == 'true') {
        let starButton = document.querySelector('.current img:last-of-type')
        starButton.setAttribute('src', 'icons/star_fill.svg')
    }
    if (fav == 'false') {
        let starButton = document.querySelector('.current img:last-of-type')
        starButton.setAttribute('src', 'icons/star.svg')
    }
    audio.setAttribute('src', `music/${showcase}`)
    audio.pause();
    audio.load();
    
    audio.oncanplaythrough = audio.play();
}

function setCurrent () {
    let titleNotific = document.querySelector('.current p:first-of-type')
    let artistNotific = document.querySelector('.current p:last-of-type')

    titleNotific.innerHTML = '<em>' + audio.dataset.title + '</em>'
    artistNotific.textContent = audio.dataset.artist
}

function setDuration(time) {
    let inhhmmss = new Date(time * 1000).toISOString().substr(11, 8)
    return inhhmmss.slice(3)
}

function loadnext () {
    let mainNodes = document.querySelectorAll('.right > .tracks > .scroll div')
    let tracklist = Array.from(mainNodes)
    let status = true

    if (shuffle) {
        let maximum = tracklist.length - 1
        let minimum = 0
        let randomnumber = Math.floor(Math.random() * (maximum - minimum + 1)) + minimum;

        removeSelected(mainNodes)
        
        let showcase = tracklist[randomnumber].dataset.url
        let artist = tracklist[randomnumber].dataset.artist
        let title = tracklist[randomnumber].dataset.title
        let album = tracklist[randomnumber].dataset.album
        let s_id = tracklist[randomnumber].dataset.s_id
        let fav = tracklist[randomnumber].dataset.fav
        console.log(album)
        next(showcase, artist, title, album, s_id, fav)
        tracklist[randomnumber].classList.add('selected')

    } else {

        tracklist.forEach( function (item, index, array) {
    
            if (index == tracklist.length - 1) {
                status = false
            }
            if (item.classList.contains('selected') && status) {
                removeSelected(mainNodes)
    
                let showcase = tracklist[index + 1].dataset.url
                let artist = tracklist[index + 1].dataset.artist
                let title = tracklist[index + 1].dataset.title
                let album = tracklist[index + 1].dataset.album
                let s_id = tracklist[index + 1].dataset.s_id
                let fav = tracklist[index + 1].dataset.fav
                next(showcase, artist, title, album, s_id, fav)
                array[index + 1].classList.add('selected')
                status = false
            }
        })
    }
}

function loadprev () {
    let mainNodes = document.querySelectorAll('.right > .tracks > .scroll div')
    let tracklist = Array.from(mainNodes)

    if (shuffle) {
        let maximum = tracklist.length - 1
        let minimum = 0
        let randomnumber = Math.floor(Math.random() * (maximum - minimum + 1)) + minimum;
        console.log(randomnumber)

        removeSelected(mainNodes)
        
        let showcase = tracklist[randomnumber].dataset.url
        let artist = tracklist[randomnumber].dataset.artist
        let title = tracklist[randomnumber].dataset.title
        let album = tracklist[randomnumber].dataset.album
        let s_id = tracklist[randomnumber].dataset.s_id
        let fav = tracklist[randomnumber].dataset.fav
        next(showcase, artist, title, album, s_id, fav)
        tracklist[randomnumber].classList.add('selected')

    } else {

        tracklist.forEach( function (item, index, array) {
    
            let status = true
            if (index == 0) {
                status = false
            }
            if (item.classList.contains('selected') && status) {
                removeSelected(mainNodes)
                
                let showcase = tracklist[index - 1].dataset.url
                let artist = tracklist[index - 1].dataset.artist
                let title = tracklist[index - 1].dataset.title
                let album = tracklist[index - 1].dataset.album
                let s_id = tracklist[index - 1].dataset.s_id
                let fav = tracklist[index - 1].dataset.fav
                next(showcase, artist, title, album, s_id, fav)
                array[index - 1].classList.add('selected')
                status = false
            }
        })
    }
}

function gettingAllTracks () {

    let httpRequest = new XMLHttpRequest();
    httpRequest.open('GET', '/music');
    httpRequest.setRequestHeader("Accept", "application/json");
    httpRequest.onreadystatechange = function() {
    
        if(httpRequest.readyState == 4 && httpRequest.status == 200) {
            let data = JSON.parse(httpRequest.response)
            console.log(JSON.parse(httpRequest.response))
            generateTags(data)
        }
    }
    httpRequest.send();
}

function removeSelected (childrenList) {
    let arrayOfchildren = Array.from(childrenList);
    arrayOfchildren.forEach( function (item) {
        item.classList.remove('selected')
    })
}

function refreshMain (area) {
    if (area == '.left .scroll') {
        let htmlOftracks = document.querySelector(area).children
        let arrayOftracks = Array.from(htmlOftracks);
        arrayOftracks.map(function(item, index){
            if (index > 1) {
                item.remove()
            }
        })
    } else if (area == '.right .scroll') {
        let htmlOftracks = document.querySelector(area).children
        let arrayOftracks = Array.from(htmlOftracks);
        arrayOftracks.map(function(item){
            item.remove()
        })
    }
}

function onstart() {
    document.querySelector('.left .scroll > div').classList.add('selected')
}

function shuffleToggle () {
  let status = true
  if (!shuffle && status) {
      shuffleButton.setAttribute('src', 'icons/shuffle_on.svg')
      shuffle = true, status = false
  }
  if (shuffle && status) {
      shuffleButton.setAttribute('src', 'icons/shuffle.svg')
      shuffle = false, status = false
  }
}

function generateTags (musicdata) {
  let parent = document.querySelector('.right .scroll')
  musicdata.forEach(function (item, index){

      let div = document.createElement('div')
      if (`http://localhost:8080/music/${item.url}` === decodeURIComponent(audio.src)) {
        div.classList.add('selected')
      }
      let pOne = document.createElement('p')
      let pTwo = document.createElement('p')
      let aOne = document.createElement('a')
      let aTwo = document.createElement('a')

      aOne.textContent = index + 1 + '.'
      aTwo.textContent = item.title
      pTwo.textContent = setDuration(item.duration)
      div.dataset.s_id = item.s_id
      div.dataset.url = item.url
      div.dataset.artist = item.artist
      div.dataset.album = item.album
      div.dataset.title = item.title
      div.dataset.fav = item.fav
      div.addEventListener('click', next.bind(this, item.url, item.artist, item.title, item.album, item.s_id, item.fav))
      div.addEventListener('click', function (e) {
          removeSelected(e.target.parentNode.children)
          e.target.classList.add('selected')
      })
      pOne.appendChild(aOne)
      pOne.appendChild(aTwo)
      div.appendChild(pOne)
      div.appendChild(pTwo)
      parent.appendChild(div)
  })
}

function generatePlaylistTags(playlists) {
  let container = document.querySelector('.left .playlists .scroll')

  playlists.forEach( function (item) {
      let newDiv = document.createElement('div')
      let newA = document.createElement('a')
      let newImg = document.createElement('img')
      newImg.setAttribute('src', 'icons/cross.svg')
      newImg.setAttribute('style', 'width: 30px; height: 30px;')
      newImg.addEventListener('click', function (e) {

          e.stopPropagation()

          let objective = e.target.parentNode.dataset.p_id

          let httpRequest = new XMLHttpRequest();
          httpRequest.open('POST', `/delete/${objective}`);
          httpRequest.setRequestHeader("Accept", "application/json");
          httpRequest.onreadystatechange = function() {
          
              if(httpRequest.readyState == 4 && httpRequest.status == 200) {
                  let data = JSON.parse(httpRequest.response)
                  console.log(JSON.parse(httpRequest.response))
              }
          }
          httpRequest.send();

          e.target.parentNode.parentNode.removeChild(e.target.parentNode)

      })
      newA.textContent = item.name
      newA.style.pointerEvents = 'none'
      newDiv.dataset.p_id = item.name

      newDiv.appendChild(newA)
      newDiv.appendChild(newImg)
      container.appendChild(newDiv)
  })

  settingPlaylistEventListeners()  
}

function gettingALLPlaylists () {

  let httpRequest = new XMLHttpRequest();
  httpRequest.open('GET', '/playlists');
  httpRequest.setRequestHeader("Accept", "application/json");
  httpRequest.onreadystatechange = function() {
  
      if(httpRequest.readyState == 4 && httpRequest.status == 200) {
          let data = JSON.parse(httpRequest.response)
          console.log(JSON.parse(httpRequest.response))
          generatePlaylistTags(data)
      }
  }
  httpRequest.send();
}

function settingPlaylistEventListeners () {
  let playlistsNodes = document.querySelector('.left .playlists .scroll').children
  let playlists = Array.from(playlistsNodes)

  playlists.forEach( function (item, index) {

      item.addEventListener('click', function(e) {
          removeSelected(e.target.parentNode.children)
          e.target.classList.add('selected')

          let svgs = document.querySelectorAll('.playlists div > img')
          
          svgs.forEach(function (item, index) {
              item.src = 'icons/cross.svg'
          })
      })

      if (index == 0) {
          item.addEventListener('click', function() {

              refreshMain('.right .scroll')
              
              gettingAllTracks()
          })

      }
      if (index == 1) {
          item.addEventListener('click', function () {
              refreshMain('.right .scroll')

              let httpRequest = new XMLHttpRequest();
              httpRequest.open('GET', '/music/favourites');
              httpRequest.setRequestHeader("Accept", "application/json");
              httpRequest.setRequestHeader("favourites", "true");
              httpRequest.onreadystatechange = function() {
              
                  if(httpRequest.readyState == 4 && httpRequest.status == 200) {
                      let data = JSON.parse(httpRequest.response)
                      console.log(JSON.parse(httpRequest.response))
                      generateTags(data)
                  }
              }
              httpRequest.send();
          })
      }
      if (index > 1) {
          item.addEventListener('click', function (e) {
              refreshMain('.right .scroll')

              let objective = e.target.dataset.p_id

              let httpRequest = new XMLHttpRequest();
              httpRequest.open('GET', `/music/${objective}`);
              httpRequest.setRequestHeader("Accept", "application/json");
              httpRequest.onreadystatechange = function() {
              
                  if(httpRequest.readyState == 4 && httpRequest.status == 200) {
                      let data = JSON.parse(httpRequest.response)
                      console.log(JSON.parse(httpRequest.response))
                      generateTags(data)
                  }
              }
              httpRequest.send();

              e.target.children[1].setAttribute('src', 'icons/cross_black.svg')
          })
      }
  })
}

//eventlisteners

audio.addEventListener('ended', loadnext)
audio.addEventListener('loadstart', setCurrent)

let starButton = document.querySelector('.current img:last-of-type')
starButton.addEventListener('click', function () {
    let s_id = document.querySelector('audio').dataset.s_id
 
    let httpRequest = new XMLHttpRequest();
    httpRequest.open('PATCH', `/favourite?f=${s_id}`);
    httpRequest.setRequestHeader("Accept", "application/json");
    httpRequest.setRequestHeader("Content-Type", "application/json");
    
    if (starButton['src'].includes('fill')) {
        httpRequest.setRequestHeader("method", "undo");
    } else {
        httpRequest.setRequestHeader("method", "do");        
    }
    
    httpRequest.onreadystatechange = function() {
    
        if(httpRequest.readyState == 4 && httpRequest.status == 200) {
            let data = JSON.parse(httpRequest.response)
            console.log(JSON.parse(httpRequest.response))
            if (data) starButton.setAttribute('src', 'icons/star_fill.svg');
            if (!data) starButton.setAttribute('src', 'icons/star.svg');  
        }
    }
    httpRequest.send();
})

let trackCreateButton = document.querySelector('.notific > div:first-child > p > img:first-of-type')
trackCreateButton.addEventListener('click', function () {
    document.querySelector('.modal.create').classList.add('visible')
})

let unbutton1 = document.querySelector('.modal.create > img')
unbutton1.addEventListener('click', function () {
    document.querySelector('.modal.create').classList.remove('visible')
})

let trackAddButton = document.querySelector('.current img:first-of-type')
trackAddButton.addEventListener('click', function () {
    document.querySelector('.modal.add').classList.add('visible')
})

let unbutton2 = document.querySelector('.modal.add > img')
unbutton2.addEventListener('click', function () {
    document.querySelector('.modal.add').classList.remove('visible')
})

let modalAdd = document.querySelector('.modal.add button')
modalAdd.addEventListener('click', function () {
    let input = document.querySelector('.modal.add input').value.trim()

    let s_id = document.querySelector('audio').dataset.s_id
    if (input.length > 0) {
        let data = {
            "id": s_id
        }
        console.log(data)
        let httpRequest = new XMLHttpRequest();
        httpRequest.open('POST', `/addtrack/${input}`);
        httpRequest.setRequestHeader("Accept", "application/json");
        httpRequest.setRequestHeader("Content-Type", "application/json");        
        httpRequest.onreadystatechange = function() {
        
            if(httpRequest.readyState == 4 && httpRequest.status == 200) {
            }
        }
        httpRequest.send(JSON.stringify(data));
    }
})

let modalCreate = document.querySelector('.modal.create button')
modalCreate.addEventListener('click', function () {
    let input = document.querySelector('.modal.create input').value.trim()
    if (input.length > 0) {

        let httpRequest = new XMLHttpRequest();
        httpRequest.open('POST', `/playlist/${input}`);
        httpRequest.setRequestHeader("Accept", "application/json");
        httpRequest.onreadystatechange = function() {
        
            if(httpRequest.readyState == 4 && httpRequest.status == 200) {
                let data = JSON.parse(httpRequest.response)
                console.log(JSON.parse(httpRequest.response))
            }
        }
        httpRequest.send(JSON.stringify(input));

        refreshMain('.left .scroll')
        gettingALLPlaylists()
    }
})

let rightButton = document.querySelector('footer div:nth-of-type(2n)')
rightButton.addEventListener('click', loadnext)

let leftButton = document.querySelector('footer div:nth-of-type(1n)')
leftButton.addEventListener('click', loadprev)

let shuffleButton = document.querySelector('footer div:nth-of-type(3n) img')
shuffleButton.addEventListener('click', shuffleToggle)

window.onkeyup = function(e) {
    let key = e.keyCode
    if (key == 39) {
        loadnext()
    } else if (key == 37) {
        loadprev()
    } else if (key == 83) {
        shuffleToggle()
    }
}

gettingAllTracks()
gettingALLPlaylists()
onstart()

// experiments with p5.sound visualisation --- to connect it via MediaStream

let fft;

function setup(){
  let cnv = createCanvas(70,70);
  cnv.parent('visualisation')
  fft = new p5.FFT();
  
  let audioCtx = new (window.AudioContext || window.webkitAudioContext)();
  console.log(audioCtx)
  let source = audioCtx.createMediaElementSource(audio);
  console.log(source)
  let analyser = audioCtx.createAnalyser();
  console.log(analyser)

  source.connect(analyser)
  fft.analyser = analyser
  analyser.connect(audioCtx.destination)
}
  
function draw(){
  background(230, 182, 182);
  let waveform = fft.waveform();
  noFill();
  beginShape();
  stroke(160, 100, 164);
  strokeWeight(1);
  for (let i = 0; i < waveform.length; i++){
    let x = map(i, 0, waveform.length, 0, width);
    let y = map( waveform[i], -1, 1, 0, height);
    vertex(x,y);
  }
  endShape();
}
  