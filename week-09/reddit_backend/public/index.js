'use strict'

var container = document.querySelector('.main-container')

function deletePost (e) {
    let id = e.target.dataset.id
    if (userName === allUsers[`${id}`]) {
        let httpRequest = new XMLHttpRequest();
        httpRequest.open('DELETE', 'posts/' + id, true);
        
        httpRequest.setRequestHeader("Accept", "application/json");
        httpRequest.setRequestHeader("Content-Type", "application/json");
        
        httpRequest.onreadystatechange = function() {
            
            if(httpRequest.readyState == 4 && httpRequest.status == 200) {
                let item = e.target.parentNode.parentNode.parentNode
                let parent = item.parentNode
                item.classList.add('remove')
                setTimeout(() => {
                    parent.removeChild(item)
                }, 2000);
            }
        }
        httpRequest.send(null);
    } else {
        alert('no restrictions')
    }
}

function relocateToModify(e) {
    
    let url = e.target.dataset.url
    let title = e.target.parentNode.parentNode.children[0].textContent
    let id = e.target.dataset.id
    if (userName === allUsers[`${id}`]) {
        let queryString = "?para1=" + url + "&para2=" + title + '&para3=' + id + '&para4=' + userName;
        window.location.href = "modify.html" + queryString;
    } else {
        alert('no restrictions')
    }

}

function fillMain (onePost) {
    settingData(onePost)
}

function upVote (e) {
    let currentId = e.target.dataset.id
    let httpRequest = new XMLHttpRequest();
    httpRequest.open('PATCH', 'posts/'+currentId+'/upvote', true);
    
    httpRequest.setRequestHeader("Accept", "application/json");
    
    httpRequest.onreadystatechange = function() {
        
        if(httpRequest.readyState == 4 && httpRequest.status == 200) {

            let newScore = JSON.parse(httpRequest.response)
            e.target.parentNode.children[1].textContent = newScore[0].score
            e.target.parentNode.children[1].dataset.score = newScore[0].score
        }
    }
    httpRequest.send(null);
}

function downVote (e) {
    let currentId = e.target.dataset.id
    let httpRequest = new XMLHttpRequest();
    httpRequest.open('PATCH', 'posts/'+currentId+'/downvote', true);
    
    httpRequest.setRequestHeader("Accept", "application/json");
    
    httpRequest.onreadystatechange = function() {

        if(httpRequest.readyState == 4 && httpRequest.status == 200) {

            let newScore = JSON.parse(httpRequest.response)
            e.target.parentNode.children[1].textContent = newScore[0].score
            e.target.parentNode.children[1].dataset.score = newScore[0].score
        }
    }
    httpRequest.send(null);
}

function refresh () {
    let htmlOfPosts = document.querySelector('.main-container').children
    let arrayOfPosts = Array.from(htmlOfPosts);
    arrayOfPosts.map(function(item){
        item.remove()
    })
    start()
}

function append(parent, childList) {
    for (let i = 0; i < childList.length; i++) {
        parent.appendChild(childList[i])
    }
    return parent
}

function settingData (onePost) {
    let post = document.createElement('div')
    post.classList.add('post')
    post.setAttribute('id', 'id' + onePost.id)
    
    let div1 = document.createElement('div')
    
    let a0 = document.createElement('a')
    let a1 = document.createElement('a')
    let a2 = document.createElement('a')
    a0.innerHTML = '&#8679;'
    a0.dataset.id = onePost.id
    a0.addEventListener('click', upVote)
    a1.dataset.score = onePost.score
    a1.innerHTML = a1.dataset.score
    a2.innerHTML = '&#8681;'
    a2.dataset.id = onePost.id
    a2.addEventListener('click', downVote)
    
    let div1Fill = append(div1, [a0,a1,a2])
    
    let div2 = document.createElement('div')
    
    let h2 = document.createElement('a')
    let p0 = document.createElement('p')
    let p1 = document.createElement('p')
    
    let a3 = document.createElement('a')
    let a4 = document.createElement('a')
    let a5 = document.createElement('a')
    
    a3.textContent = '⨕'
    a4.textContent = 'modify'
    a4.dataset.url = onePost.url
    a4.dataset.id = onePost.id
    a4.addEventListener('click', relocateToModify)
    a5.textContent = 'remove'
    a5.dataset.id = onePost.id
    a5.addEventListener('click', deletePost)
    
    h2.textContent = onePost.title
    h2.setAttribute('href', onePost.url)
    
    if (onePost.owner == null) {
        onePost.owner = 'anonymous'
    }
    
    let date = new Date(onePost.timestamp * 1000)
    
    p0.innerHTML = date + ' | ' + '<strong>' + onePost.owner + '</strong>'

    if (onePost.owner !== userName) {
        a4.classList.add('invalid')
        a5.classList.add('invalid')
    }
    allUsers[`${onePost.id}`] = onePost.owner
    
    let p1Fill = append(p1, [a3,a4,a5])
    
    let div2Fill = append(div2, [h2, p0, p1Fill])
    
    post.appendChild(div1Fill)
    post.appendChild(div2Fill)

    container.appendChild(post)
}

function start () {
    
    let httpRequest = new XMLHttpRequest();
    httpRequest.open('GET', '/posts', true);
    httpRequest.setRequestHeader("Accept", "application/json");
    httpRequest.setRequestHeader("Content-Type", "application/json");
    
    httpRequest.onreadystatechange = console.log;
    httpRequest.send();
    httpRequest.onload = function() {
        var data = JSON.parse(httpRequest.responseText);
        console.log(data)

        data.sort(function (a, b) {
            return a.score - b.score;
        })

        for (let i = data.length - 1; i >= 0; i--) {
            fillMain(data[i])
        }
    }
}

let userName = window.location.href.split('para1=')
userName = decodeURIComponent(userName[1])
let allUsers = {}

start ()

console.log(allUsers)

document.querySelector('.button').href = `submit.html?para1=${userName}`
document.querySelector('header p').innerHTML = `logged in as <em>${userName}</em>`

// setInterval(refresh, 40000)