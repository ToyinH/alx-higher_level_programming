#!/usr/bin/node
/**
 * a script that gets the contents of a webpage and stores it in a file
 * The first argument is the URL to request
 * The second argument the file path to store the body response
 * The file must be UTF-8 encoded
 */

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filepath = process.argv[3];

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }

  fs.writeFile(filepath, body, (err) => {
    if (err) {
      console.log('error');
    }
  });
});
