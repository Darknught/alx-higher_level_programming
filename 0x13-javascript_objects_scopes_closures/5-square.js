#!/usr/bin/node
// A module that defines a class Square that inherits from Rectangle
// constructor must take 1 arg: size, and must be called using super()
module.exports = class Square extends require('./4-rectangle.js') {
  constructor (size) {
    super(size, size);
  }
};
