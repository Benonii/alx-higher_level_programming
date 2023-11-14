#!/usr/bin/node

const argv = process.argv;
const firstArg = argv[2];
const x = Math.floor(Number(firstArg));

if (Number.isNaN(x)) {
	console.log('Not a number');
} else {
	console.log('My number: ' + x);
}
