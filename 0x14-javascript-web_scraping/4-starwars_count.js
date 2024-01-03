#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const charId = 'https://swapi-api.alx-tools.com/api/people/18/';
let count = 0;

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
    process.exit(1);
  } else {
    const movies = JSON.parse(body);
    for (const movie of movies.results) {
      if (movie.characters.includes(charId)) {
        count++;
      }
    }
    console.log(count);
  }
});
