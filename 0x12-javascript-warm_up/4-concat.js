#!/usr/bin/node
// A Script that prints two arguments passed to it with "is" in middle
const { argv } = require('process');
if (argv[2]) {
  console.log(argv.slice(2).join(' is '));
}
