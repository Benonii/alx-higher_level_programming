#!/usr/bin/node

const argv = process.argv;
const firstArg = argv[2];
const x = Math.floor(Number(firstArg));

if (firstArg) {
  console.log('My number: ' + x);
} else {
  console.log('Not a number');
}
