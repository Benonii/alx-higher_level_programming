#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
    process.exit(1);
  } else {
    const movie = JSON.parse(body);
    for (const character of movie.characters) {
      request.get(character, (err, response, body) => {
        if (err) {
          console.log(err);
          process.exit(1);
        }
        const characterObj = JSON.parse(body);
        console.log(characterObj.name);
      });
    }
    // console.log(character);
  }
});
