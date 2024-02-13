#!/usr/bin/node
// A Script that defines a Rectangle class
// Constructor that takes two arguments, if w or h is equal to 0 or not "+"
// create an empty object
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) { [this.width, this.height] = [w, h]; }
  }
};
