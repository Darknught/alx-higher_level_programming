#!/usr/bin/node
// A Script that prints reverse of a list without using the built in reverse

exports.esrever = function (list) {
  const rev = [];
  for (let i = list.length - 1; i >= 0; i--) {
    rev.push(list[i]);
  }
  return rev;
};
