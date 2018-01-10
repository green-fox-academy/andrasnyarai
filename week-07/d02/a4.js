'use strict'; 

var shop_items = ["Cupcake", 2, "Brownie", false]

shop_items.map(function(item, index) {
    if (item == 2) {
        shop_items[index] = 'Croissant';
    } else if (item == false) {
        shop_items[index] = 'Ice cream';
    }
})

console.log(shop_items)