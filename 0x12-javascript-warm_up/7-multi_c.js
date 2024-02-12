#!/usr/bin/node
// A Script that prints x times "C is fun" as x is the first argument
// Otherwise if it cant be converted print "Missing number of occurrences"
const { argv } = require('process');
if (!isNaN(parseInt(argv[2]))) {
  const x = parseInt(argv[2]);
  if (x >= 0) {
    for (let i = 0; i < x; i++) {
      console.log('C is fun');
    }
  } else {
    console.log('Missing number of occurrences');
  }
} else {
  console.log('Missing number of occurrences');
}
