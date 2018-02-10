'use strict';

let filter = document.querySelector('button')
let parent = document.querySelector('.main')

function generateTags(books) {
  books.forEach((book) => {
    parent.innerHTML +=
      `<tr><td>${book.aut_name}</td>
        <td>${book.book_name}</td>
        <td>${book.cate_descrip}</td>
        <td>${book.pub_name}</td>
        <td>${book.book_price}</td></tr>`
  })
}

filter.addEventListener('click', (e) => {
  let category = document.querySelector('#category_select').value
  let lower = document.querySelector('#price_lower').value
  let higher = document.querySelector('#price_higher').value
  e.preventDefault()
  fetch(`/filter?category=${category}&lower=${lower}&higher=${higher}`, { method: 'GET' }).then(function (response) {
    if (response.status !== 200) {
      console.log('Looks like there was a problem. Status Code: ' +
        response.status);
      return;
    }
    // Examine the text in the response
    response.json().then(function (data) {
      console.log(data);
      parent.innerHTML = ''
      generateTags(data)
    });
  }).catch(function (err) {
    console.log('Fetch Error :-S', err);
  })
})