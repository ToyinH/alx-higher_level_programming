#!/usr/bin/node

// /**
//  * script that prints all characters of a Star Wars movie
//  * The first argument is the Movie ID - example: 3 = “Return of the Jedi”
//  * Display one character name by line
//  * You must use the Star wars API
//  * You must use the module request
//  */

// const request = require('request-promise');

// const movieId = process.argv[2];
// const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

// async function fetchCharacterDetails (characterUrl) {
//   try {
//     const body = await request.get(characterUrl);
//     return JSON.parse(body);
//   } catch (error) {
//     console.error('Error fetching character details:', error);
//     return null;
//   }
// }

// async function main () {
//   try {
//     const body = await request.get(url);
//     const charactersList = JSON.parse(body).characters;

//     // Fetch and print character names in order
//     for (let index = 0; index < charactersList.length; index++) {
//       const characterDetails = await fetchCharacterDetails(charactersList[index]);
//       if (characterDetails !== null) {
//         console.log(characterDetails.name);
//       }
//     }
//   } catch (error) {
//     console.error('Error:', error);
//   }
// }

// main();


const util = require('util');
const request = require('request');

const promisifiedRequestGet = util.promisify(request.get);

const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

async function fetchCharacterDetails(characterUrl) {
  try {
    const { body } = await promisifiedRequestGet(characterUrl);
    return JSON.parse(body);
  } catch (error) {
    console.error('Error fetching character details:', error);
    return null;
  }
}

async function main() {
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
