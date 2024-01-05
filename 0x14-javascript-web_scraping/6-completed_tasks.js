#!/usr/bin/node
/**
 * script that computes the number of tasks completed by user id.
 * The first argument is the
 * API URL: https://jsonplaceholder.typicode.com/todos
 * Only print users with completed task
 *
 */

const request = require('request');

const url = process.argv[2];

// const url = 'https://jsonplaceholder.typicode.com/todos';

const newDict = {};

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const list = JSON.parse(body);

  const listSize = list.length;
  // console.log(list);
  // console.log(listSize);

  let count = 0;
  let trackId = 1;

  for (let index = 0; index < listSize; index++) {
    if (list[index].userId === trackId) {
      if (list[index].completed === true) {
        count++;
      }
    } else {
      if (count !== 0) {
        newDict[String(trackId)] = count;
      }

      if (list[index].completed === true) {
        count = 1;
      } else {
        count = 0;
      }
      trackId++;
    }
  }
  const lastKey = list[listSize - 1].userId;
  if (count !== 0) {
    newDict[String(lastKey)] = count;
  }
  console.log(newDict);
});
