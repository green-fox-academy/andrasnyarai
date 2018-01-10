'use strict'; 

var girls = ["Eve","Ashley","Bözsi","Kat","Jane"];
var boys = ["Joe","Fred","Béla","Todd","Neef","Jeff"];
var order = [];

function _longer_ (a, b) {
    if (a.length > b.length) {
        return a.length;
    } else if (b.length > a.length) {
        return b.length;
    } else {
        return a.length;
    }
}

for (let index = 0; index <= _longer_(girls, boys); index++) {
    if (girls.length <= boys.length) {
        order.push(boys[index]);
        order.push(girls[index]);
    } else if (girls.length >= boys.length) {
        order.push(girls[index]);
        order.push(boys[index]);
    }
}

order = order.filter(item => typeof item == 'string');

console.log(order);