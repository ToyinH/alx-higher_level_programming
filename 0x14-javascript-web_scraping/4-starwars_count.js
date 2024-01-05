#!/usr/bin/node
/**
 * a script that prints the number of movies
 * where the character “Wedge Antilles” is present
 */

const request = require('request');

const url = process.argv[2];

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }

  // convert from string to an object before you can access the body.
  const bodyObj = JSON.parse(body);

  // to access the title
  // console.log(bodyObj);
  // console.log(bodyObj.results[0].characters[15]);

  const newUrl = bodyObj.results[0].characters[15];
  request.get(newUrl, (err, response, body) => {
    if (err) {
      console.log(err);
      return;
    }
    const characterObj = JSON.parse(body);
    // console.log(characterObj);
    console.log(characterObj.films.length);
  });
});
