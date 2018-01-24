'use strict';

// Handle the exceptions in the addString() function. It should check the type of the
// arguments, throw the right error and write it to the console.
// It should add the strings too if the arguments are appropriate.

let  addString = function(str1, str2, printStr){

    try {
        if (typeof str1 == 'string' && typeof str2 == 'string' && typeof printStr == 'function') {
            let newStr = str1 + str2;
            printStr(newStr);
      
        } else {
            throw Error('hajhaj')
        }

    } catch (err) {
        console.log(err)
    }

}

let printStr = function(str) {
  console.log(str);
}

addString(1234, 56789, 'printStr');

console.log('\nit will run')