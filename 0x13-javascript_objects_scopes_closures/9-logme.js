#!/usr/bin/node

let count = 0;
exports.logMe = function (items) {
  console.log(`${count}: ${items}`);
  count++;
};
