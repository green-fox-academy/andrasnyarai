'use strict'; 

var url = "https//www.reddit.com/r/nevertellmethebots";

url = url.slice(0,url.search('bots')).split('')
url.push('odds/')
url = url.join('')

console.log(url);