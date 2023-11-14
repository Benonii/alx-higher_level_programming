#!/usr/bin/node

const argv = process.argv;
const size = Number(argv[2]);
let i;

if (size) {
  for (i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
} else {
  console.log('Missing size');
}
