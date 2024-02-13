#!/usr/bin/node
// A Script that imports a dictionary of occurrences by user id and computes
// a dictionary of user ids by occurrences

const dict = require('./101-data.js').dict;
const newD = {};
for (const key in dict) {
  if (newD[dict[key]] === undefined) {
    newD[dict[key]] = [key];
  } else {
    newD[dict[key]].push(key);
  }
}
console.log(newD);
