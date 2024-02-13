#!/usr/bin/node
// A Script that defines a class Square that inherits from Square of 5-square
// Create an instance method charPrint(c) that prints rectangle using char c
// if c is undefined, use the char 'X'
module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
