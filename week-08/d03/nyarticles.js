'use strict'

// let httpRequest = new XMLHttpRequest();
// httpRequest.open('GET', 'https://api.nytimes.com/svc/search/v2/articlesearch.json?51811de36a564468a559415358187f4e', true); // Also try http://444.hu/feed
// httpRequest.send(null);
// httpRequest.onreadystatechange = console.log;
// httpRequest.onload = function() {
//     var articles = JSON.parse(httpRequest.responseText);
//     console.log(articles.data)
// }





// Built by LucyBot. www.lucybot.com
var url = "https://api.nytimes.com/svc/search/v2/articlesearch.json";
url += '?' + $.param({
  'api-key': "51811de36a564468a559415358187f4e",
  'q': "Apollo 11 moon landing"
});
$.ajax({
  url: url,
  method: 'GET',
}).done(function(result) {
  var data = result.response.docs

  console.log(data);

  let theBody = document.querySelector('body')
  for (let i = 0; data.length; i++) {
      if (i == data.length) {
        return
      }
      console.log(data[i]);
      let newDiv = document.createElement('div')
      let newH1 = document.createElement('h1')
      let newH2 = document.createElement('h2')
      let newP = document.createElement('p')
      let newA = document.createElement('a')
  
      newH2.textContent = data[i].headline.main
      newP.textContent = data[i].snippet
      newH2.textContent = data[i].pub_date
      newA.textContent = 'link'
      newA.setAttribute('href', data[i].web_url) 

      newDiv.appendChild(newH1)
      newDiv.appendChild(newH2)
      newDiv.appendChild(newP)
      newDiv.appendChild(newA)
      theBody.appendChild(newDiv)
  }


}).fail(function(err) {
  throw err;
});


// Display the following fields in a list
// Headline
// Snippet
// Publication date
// Create a permalink to that article