#!/usr/bin/node
// A script that prints the number of movies where the character
// Wedge Antilles is present. The char ID is 18
const request = require('request');
const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.log('Error:', error);
  } else {
    const films = JSON.parse(body).results;
    let count = 0;

    films.forEach(film => {
      if (film.characters.includes(
        'https://swapi-api.alx-tools.com/api/people/18/'
      )) {
        count++;
      }
    });
    console.log(`${count}`);
  }
});
