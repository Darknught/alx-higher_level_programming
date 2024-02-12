#!/usr/bin/node
// Script that prints command line Arguments
const { argv } = require('process');
if (argv.length <= 2) {
  console.log('No argument');
} else {
  console.log('Argument found');
}
