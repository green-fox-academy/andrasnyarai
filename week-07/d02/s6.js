'use strict'; 

var out = "";
var notSoCrypticMessage = [1, 12, 1, 2, 11, 1, 7, 11, 1, 49, 1, 3, 11, 1, 50, 11];

var hashmap = {
    7: "run around and desert you ",
    50: "tell a lie and hurt you ",
    49: "make you cry, ",
    2: "let you down",
    12: "give you up, ",
    1: "Never gonna ",
    11: "\n",
    3: "say goodbye "
};

for (let num of notSoCrypticMessage) {
    for (let value in hashmap) {
        if (num == value) {
            out += hashmap[value];
        }
    }
}

console.log(out)