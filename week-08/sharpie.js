// We should know about each sharpie:
// color (which should be a string)
// width (which will be a number)
// inkAmount (another number)
// When instantiating a Sharpie, we need to specify the color and the width
// Every sharpie is created with a default 100 as inkAmount
// We can use() the sharpie objects
// which decreases inkAmount by the width
// Write a loop that consumes all the sharpie's ink.
// Make sure your loop works with any inkAmount, so your code figures out when it's out of ink.

class Sharpie {
    constructor(color, width) {
        this.color = color
        this.width = width
        this.inkAmount = 100  
    }
    use () {
        if (this.inkAmount <= this.width) {
            console.log('empty')
            this.inkAmount = 0
        } else {
            this.inkAmount -= this.width
        }
    }
}

function useAll (item) {
    let originalAmount = item.inkAmount
    for (let i = 0; i <= (originalAmount / item.width); i++) {
        console.log(item.inkAmount)
        item.use()
    }
}

let mySharpie = new Sharpie ('pink', 3)

console.log(mySharpie.inkAmount)
useAll(mySharpie)
console.log(mySharpie.inkAmount)