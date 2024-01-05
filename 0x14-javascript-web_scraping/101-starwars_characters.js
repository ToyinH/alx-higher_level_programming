#!/usr/bin/node

const util = require('util');
const request = require('request');

const promisifiedRequestGet = util.promisify(request.get);

const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

async function fetchCharacterDetails (characterUrl) {
  try {
    const { body } = await promisifiedRequestGet(characterUrl);
    return JSON.parse(body);
  } catch (error) {
    console.error('Error fetching character details:', error);
    return null;
  }
}

async function main () {
  try {
    const { body } = await promisifiedRequestGet(url);
    const charactersList = JSON.parse(body).characters;

    // Fetch and print character names in order
    for (let index = 0; index < charactersList.length; index++) {
      const characterDetails = await fetchCharacterDetails(charactersList[index]);
      if (characterDetails !== null) {
        console.log(characterDetails.name);
      }
    }
  } catch (error) {
    console.error('Error:', error);
  }
}

main();
