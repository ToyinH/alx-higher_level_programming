#!/usr/bin/node

/*
script that display the status code of a get request */

const request = require('request');

const url = process.argv[2];

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log('code:', response.statusCode);
  // to convert response to json and index. use below
  // console.log(JSON.stringify(response, null, 2));
});
