#!/usr/bin/node
/**
 * script that prints the title of a star wars movie
 * where the episode number matches a given integer
 */

const request = require('request');

const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }

  // convert from string to an object before you can access the body.
  const bodyObj = JSON.parse(body);

  // to access the title
  console.log(bodyObj.title);
});
