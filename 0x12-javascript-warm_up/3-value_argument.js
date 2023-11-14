#!/usr/bin/node

const argv = process.argv;
let count = 0;

argv.forEach((val, index) => {
  count++;
});

if (count < 3) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
