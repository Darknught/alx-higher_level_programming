#!/usr/bin/node
// A Script that finds and prints the second largest int passed

const { argv } = require('process');

const integers = argv.slice(2).filter(arg => !isNaN(parseInt(arg)));

if (integers.length >= 2) {
  console.log(integers[1]);
} else {
  console.log(0);
}
