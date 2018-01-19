'use strict'

var container = document.querySelector('.main-container')

function deletePost (e) {
    let id = e.target.dataset.id
    let httpRequest = new XMLHttpRequest();
    httpRequest.open('DELETE', 'https://time-radish.glitch.me/posts/' + id, true);
    
    httpRequest.setRequestHeader("Accept", "application/json");
    httpRequest.setRequestHeader("Content-Type", "application/json");
    
    httpRequest.onreadystatechange = console.log
    httpRequest.onreadystatechange = function() {
        // console.log(httpRequest.readyState)
    
        // console.log(httpRequest.status)
    
        // console.log(httpRequest.responseText)
        
        if(httpRequest.readyState == 4 && httpRequest.status == 200) {
        }
    }
    console.log(e.target.parentNode.parentNode.parentNode)

    let item = e.target.parentNode.parentNode.parentNode
    let parent = item.parentNode
    parent.removeChild(item)

    httpRequest.send(null);

    // let v = document.querySelector('.main-container').children
    // var arr = Array.from(v);
    // arr.map(function(item){
    //     item.remove()
    // })
    
    // start()
}

function relocateToModify(e) {

    
    console.log(e.target.parentNode.parentNode.children[0])
    let url = e.target.dataset.url
    let title = e.target.parentNode.parentNode.children[0].textContent
    let id = e.target.dataset.id

    let queryString = "?para1=" + url + "&para2=" + title + '&para3' + id;
    window.location.href = "file:///C:/Users/Andras/greenfox/andrasnyarai/week-08/reddit/modify.html" + queryString;

    // e.target.setAttribute('href', "file:///C:/Users/Andras/greenfox/andrasnyarai/week-08/reddit/modify.html")
}

function fillMain (onePost) {
    settingData(onePost)

}

function upVote (e) {
    let currentId = e.target.dataset.id
    let httpRequest = new XMLHttpRequest();
    // console.log(e)
    // httpRequest.open('PUT', 'http://secure-reddit.herokuapp.com/simple/posts/'+currentId+'/upvote', true);
    httpRequest.open('PUT', 'https://time-radish.glitch.me/posts/'+currentId+'/upvote', true);
    
    httpRequest.setRequestHeader("Accept", "application/json");
    
    httpRequest.onreadystatechange = function() {
        
                
        if(httpRequest.readyState == 4 && httpRequest.status == 200) {

            let newScore = JSON.parse(httpRequest.response).score
            e.target.parentNode.children[1].textContent = newScore
            e.target.parentNode.children[1].dataset.score = newScore
        }
    }
    httpRequest.send(null);

    // let v = document.querySelector('.main-container').children
    // var arr = Array.from(v);
    // arr.map(function(item){
    //     item.remove()
    // })
    // start()
    // location.hash = "id42"; 
    
}
function downVote (e) {
    let currentId = e.target.dataset.id
    let httpRequest = new XMLHttpRequest();
    // httpRequest.open('PUT', 'http://secure-reddit.herokuapp.com/simple/posts/'+currentId+'/downvote', true);
    httpRequest.open('PUT', 'https://time-radish.glitch.me/posts/'+currentId+'/downvote', true);
    
    httpRequest.setRequestHeader("Accept", "application/json");
    

    httpRequest.onreadystatechange = function() {
        
                
        if(httpRequest.readyState == 4 && httpRequest.status == 200) {

            let newScore = JSON.parse(httpRequest.response).score
            e.target.parentNode.children[1].textContent = newScore
            e.target.parentNode.children[1].dataset.score = newScore
        }
    }
    httpRequest.send(null);
    
    // let v = document.querySelector('.main-container').children
    // var arr = Array.from(v);
    // arr.map(function(item){
    //     item.remove()
    // })
    
    // start()
}

function refresh () {
    let v = document.querySelector('.main-container').children
    var arr = Array.from(v);
    arr.map(function(item){
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
    
    let list0 = [a0,a1,a2]
    let div1Fill = append(div1, list0)
    
    let div2 = document.createElement('div')
    
    let h2 = document.createElement('a')
    let p0 = document.createElement('p')
    let p1 = document.createElement('p')
    
    let a3 = document.createElement('a')
    let a4 = document.createElement('a')
    let a5 = document.createElement('a')

    a5.dataset.id = onePost.id
    a5.addEventListener('click', deletePost)

    a3.textContent = '⨕'
    a4.textContent = 'modify'
    a4.dataset.url = onePost.url
    a4.dataset.id = onePost.id
    a4.addEventListener('click', relocateToModify)
    a5.textContent = 'remove'
    
    h2.textContent = onePost.title
    h2.setAttribute('href', onePost.url)
    
    if (onePost.owner == null) {
        onePost.owner = 'anonymous'
    }
        
    let date = new Date(onePost.timestamp * 1000)

    p0.innerHTML = date + ' | ' + '<strong>' + onePost.owner + '</strong>'

    let list1 = [a3,a4,a5]
    let p1Fill = append(p1, list1)

    let list2 = [h2,p0,p1Fill]
    let div2Fill = append(div2, list2)

    post.appendChild(div1Fill)
    post.appendChild(div2Fill)
    container.appendChild(post)

}



function start () {
    
    let httpRequest = new XMLHttpRequest();
    httpRequest.open('GET', 'https://time-radish.glitch.me/posts', true);
    httpRequest.setRequestHeader("Accept", "application/json");
    httpRequest.setRequestHeader("Content-Type", "application/json");
    
    httpRequest.onreadystatechange = console.log;
    console.log(httpRequest)
    httpRequest.send();
    httpRequest.onload = function() {
        var data = JSON.parse(httpRequest.responseText);
        console.log(data)
        for (let i = data.posts.length - 1; i >= 0; i--) {
            console.log(data.posts[i])
            fillMain(data.posts[i])
    
    
        }
    
    
    }
}

start ()


// setInterval(refresh, 1000)

// var storage = window.localStorage
// window.localStorage.user = 'ras'
// window.localStorage.owner = 'ras'

