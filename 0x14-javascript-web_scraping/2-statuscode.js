#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
    process.exit(1);
  } else {
    console.log('code:', response.statusCode);
  }
});
