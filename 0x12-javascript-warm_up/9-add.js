#!/usr/bin/node

const argv = process.argv;
const a = argv[2];
const b = argv[3];

function add (a, b) {
  return (Number(a) + Number(b));
}

console.log(add(a, b));
