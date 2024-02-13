#!/usr/bin/node
// A Script that converts a number from base 10 to another base passed as arg

exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
