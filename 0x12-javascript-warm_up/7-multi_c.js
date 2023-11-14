#!/usr/bin/node

const argv = process.argv;
const firstArg = argv[2];
let i = 0;

if (firstArg) {
  for (i = 0; i < firstArg; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurences');
}
