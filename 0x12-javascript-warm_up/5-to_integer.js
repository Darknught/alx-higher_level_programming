#!/usr/bin/node
// A Script that prints My number: <first argument converted in integer>
// If the first argument can be converted to an integer
const { argv } = require('process');
if (!isNaN(parseInt(argv[2]))) {
  console.log('My number: ' + parseInt(argv[2]));
} else {
  console.log('Not a number');
}
