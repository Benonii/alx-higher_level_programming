#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filename = process.argv[3];

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
    process.exit(1);
  } else {
    fs.writeFile(filename, body, 'utf-8', (err) => {
      if (err) {
        console.log(err);
        process.exit(1);
      }
    });
  }
});
