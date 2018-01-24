'use strict'

class Counter {
    countLetters (string) {
        let object = {}
        string.split('').forEach(function (item) {
            object[item] = 0
        })
        string.split('').forEach(function (item) {
            object[item]++
        })
        return object
      }
}

class summing {
    sum(arr) {
      arr = arr.filter((item) => typeof item === 'number')
      return arr.reduce((a, b) => a + b, 0)
      }
  }

module.exports = Counter