#!/usr/bin/node

/**
 * script that prints all characters of a Star Wars movie
 * The first argument is the Movie ID - example: 3 = “Return of the Jedi”
 * Display one character name by line
 * You must use the Star wars API
 * You must use the module request
 */

const request = require('request');

const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  }

  const charactersList = JSON.parse(body).characters;
  // console.log(charactersList);

  const listSize = charactersList.length;

  for (let index = 0; index < listSize; index++) {
    request.get(charactersList[index], (err, response, body) => {
      if (err) {
        console.log(err);
        return;
      }
      const characterDetail = JSON.parse(body);
      console.log(characterDetail.name);
    });
  }
});
