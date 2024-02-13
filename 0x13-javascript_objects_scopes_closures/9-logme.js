#!/usr/bin/node
// A Script that prints number of arguments already printed and the new
// argument value
// output format: <number atguments already printed>: <current arg value>

let count = 0;

exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count++;
};
