#!/usr/bin/node
// A Script that returns number of occurrences in a list

exports.nbOccurences = function (list, searchElement) {
  let count = 0;

  // loop through each element in the list
  for (let i = 0; i < list.length; i++) {
    // check  if the current element is equal to searchElement
    if (list[i] === searchElement) {
      count++;
    }
  }
  return count;
};
