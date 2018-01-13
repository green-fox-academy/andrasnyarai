'use strict';

const listOfPictures = [
    {'i': 0,
     'picture': 'p0.jpg',
     'title': 'Jackson Pollock',
     'text': 'Blue Poles / Number 11'},
    {'i': 1,
     'picture': 'p1.jpg',
     'title': 'Jackson Pollock',
     'text': 'No. 5'},
    {'i': 2,
     'picture': 'g0.jpg',
     'title': 'Philip Guston',
     'text': 'city limits'},
    {'i': 3,
     'picture': 'b0.jpg',
     'title': 'Francis Bacon',
     'text': '-'},
    {'i': 4,
     'picture': 'b1.jpg',
     'title': 'Francis Bacon',
     'text': '-'},
    {'i': 5,
     'picture': 'm0.jpg',
     'title': 'Claude Monet',
     'text': 'waterlilies'},
    {'i': 6,
     'picture': 'm1.jpg',
     'title': 'Claude Monet',
     'text': 'windmill'},
    {'i': 7,
     'picture': 'v0.jpg',
     'title': 'Van Gogh',
     'text': 'prison'},
    {'i': 8,
     'picture': 'r0.jpg',
     'title': 'Mark Rothko',
     'text': '-'},
    {'i': 9,
     'picture': 'k0.jpg',
     'title': 'Franz Klein',
     'text': '-'},
    {'i': 10,
     'picture': 'h0.jpg',
     'title': 'Edward Hopper',
     'text': 'gas station'},
    {'i': 11,
     'picture': 'w0.jpg',
     'title': 'Willem de Kooning',
     'text': '-'},
    {'i': 12,
     'picture': 'c0.jpg',
     'title': 'Giorgio de Chirico',
     'text': '-'},
    {'i': 13,
     'picture': 'rm0.jpg',
     'title': 'René Magritte',
     'text': '-'},
    {'i': 14,
     'picture': 'd0.jpg',
     'title': 'David Lynch',
     'text': '-'},
]

function clear () {
    let listOfImages = document.querySelectorAll('img')
    for (let img of listOfImages) {
        if (img.classList.contains('selected') == true) {
            img.classList.remove('selected')
        }
    }
    let listOfContainers = document.querySelectorAll('.scroll div')
    for (let img of listOfContainers) {
        if (img.classList.contains('selected') == true) {
           img.classList.remove('selected')
        }
    }
}

function goLeft (e) {

    clear()
    let status = true
    for (let item of listOfPictures) {
        if (document.querySelector('.main img').dataset.index == item.i && status) {
            let indicator = item.i - 1
            if (indicator == -1) {
                indicator = listOfPictures.length -1
            }
            
            document.querySelector('.main img').setAttribute('src', listOfPictures[indicator].picture)
            document.querySelector('.main h1').textContent = listOfPictures[indicator].title
            document.querySelector('.main p').textContent = listOfPictures[indicator].text
            document.querySelector('.main img').dataset.index = indicator
            status = false
            indicator += 1
            document.querySelector('.scroll div:nth-of-type(' + indicator + ') img').classList.add('selected')
            
            document.querySelector('.selected ~ div').classList.add('circleLeft')
            document.querySelector('.selected ~ div').classList.remove('circleRight')
            document.querySelector('.selected ~ div').classList.remove('circle')

            document.querySelector('.main div').classList.toggle('cover')
            document.querySelector('.main div').classList.toggle('coverTwo')
        }
    } 
}
function goRight (e) {

    clear()
    let status = true
    for (let item of listOfPictures) {
        if (document.querySelector('.main img').dataset.index == item.i && status) {
            let indicator = item.i + 1
            if (indicator == listOfPictures.length) {
                indicator = 0
            }
            document.querySelector('.main img').setAttribute('src', listOfPictures[indicator].picture)
            document.querySelector('.main h1').textContent = listOfPictures[indicator].title
            document.querySelector('.main p').textContent = listOfPictures[indicator].text
            document.querySelector('.main img').dataset.index = indicator
            status = false
            indicator += 1
            document.querySelector('.scroll div:nth-of-type(' + indicator + ') img').classList.add('selected')   
            
            document.querySelector('.selected ~ div').classList.add('circleRight')
            document.querySelector('.selected ~ div').classList.remove('circleLeft')
            document.querySelector('.selected ~ div').classList.remove('circle')

            document.querySelector('.main div').classList.toggle('cover')
            document.querySelector('.main div').classList.toggle('coverTwo')
        }
    }
}
let thumbnail = document.querySelector('.scroll');

thumbnail.addEventListener('click', function(event) {

    document.querySelector('.selected ~ div').classList.remove('circleLeft')
    document.querySelector('.selected ~ div').classList.remove('circleRight')
    document.querySelector('.selected ~ div').classList.add('circle')
    
    if (event.target.tagName == 'DIV') {        

        let parentElement = event.target.parentElement
        let childImg = parentElement.querySelector('img')
        document.querySelector('.main img').setAttribute('src' , childImg.src)
        document.querySelector('.main h1').textContent = childImg.dataset.title
        document.querySelector('.main p').textContent = childImg.dataset.text
        document.querySelector('.main img').dataset.index = childImg.dataset.index

        clear()
        childImg.classList.add('selected')

        document.querySelector('.main div').classList.toggle('cover')
        document.querySelector('.main div').classList.toggle('coverTwo')

    } else if (event.target.tagName == 'SPAN') {
        
        let parentElement = event.target.parentElement.parentElement
        let childImg = parentElement.querySelector('img')
        document.querySelector('.main img').setAttribute('src' , childImg.src)
        document.querySelector('.main h1').textContent = childImg.dataset.title
        document.querySelector('.main p').textContent = childImg.dataset.text
        document.querySelector('.main img').dataset.index = childImg.dataset.index

        clear()
        childImg.classList.add('selected')

        document.querySelector('.main div').classList.toggle('cover')
        document.querySelector('.main div').classList.toggle('coverTwo')

    }
});

document.querySelector('.left').addEventListener('click', goLeft);
document.querySelector('.right').addEventListener('click', goRight);

window.addEventListener('keyup', (e) => {
    if (e.keyCode == 37) {
        goLeft()
    } else if (e.keyCode == 39) {
        goRight()
    }
})

let newpicture = document.createElement('img');
document.querySelector('.main > img').setAttribute('src', listOfPictures[0].picture)
document.querySelector('.main h1').textContent = listOfPictures[0].title
document.querySelector('.main p').textContent = listOfPictures[0].text

for (let item of listOfPictures) {
    
    let newdiv = document.createElement('div');
    let newpicture = document.createElement('img');
    newpicture.setAttribute('src', item.picture)
    newpicture.setAttribute('data-title', item.title)
    newpicture.setAttribute('data-text', item.text)
    newpicture.setAttribute('data-index', item.i)

    let otherdiv = document.createElement('div')
    let newSpan = document.createElement('span')
    newSpan.textContent = item.title
    otherdiv.appendChild(newSpan)
    otherdiv.classList.add('hidden')
    
    let stylediv = document.createElement('div')
    stylediv.classList.add('circle')

    newdiv.appendChild(newpicture);
    newdiv.appendChild(stylediv);
    newdiv.appendChild(otherdiv);
    document.querySelector('.scroll').appendChild(newdiv);
}
document.querySelector('.scroll img').classList.add('selected')