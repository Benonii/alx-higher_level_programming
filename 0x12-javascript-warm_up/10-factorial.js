#!/usr/bin/node

const argv = process.argv;
const firstArg = Number(argv[2]);

function factorial (num) {
  if (!num) {
    return (1);
  }
  if (num === 0 || num === 1) {
    return (1);
  } else {
    num = num * factorial(num - 1);
  }
  return (num);
}

console.log(factorial(firstArg));
