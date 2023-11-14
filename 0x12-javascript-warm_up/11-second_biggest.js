#!/usr/bin/node

const argv = process.argv;
const arr = [];
let i;

if (argv.length > 3) {
  for (i = 2; i < argv.length; i++) {
    arr.push(Number(argv[i]));
  }
  arr.sort((a, b) => b - a);
  console.log(arr[1]);
} else {
  console.log(0);
}
