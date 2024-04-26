#!/usr/bin/node

const request = require('request');

<<<<<<< HEAD
function getMovieCharacters (movieId) {
  return new Promise((resolve, reject) => {
    const url = `https://swapi.dev/api/films/${movieId}/`;
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode !== 200) {
        reject(new Error(`Failed to retrieve data for movie ${movieId}`));
      } else {
        const movieData = JSON.parse(body);
        resolve(movieData.characters);
      }
    });
  });
}


function printMovieCharacters (movieId) {
  getMovieCharacters(movieId)
    .then(characters => {
      characters.forEach(characterUrl => {
        request(characterUrl, (error, response, body) => {
          if (error) {
            console.error(`Failed to retrieve character data for ${characterUrl}`, error);
          } else if (response.statusCode !== 200) {
            console.error(`Failed to retrieve character data for ${characterUrl}. Status code: ${response.statusCode}`);
=======
const episodeNumber = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${episodeNumber}`;

request(url, async (error, response, body) => {
  if (!error) {
    const movieData = JSON.parse(body);
    const characters = movieData.characters;

    for (const character of characters) {
      const promise = new Promise((resolve, reject) => {
        request(character, (error, response, names) => {
          if (!error) {
            resolve(JSON.parse(names).name);
>>>>>>> 0041d3ec4b323eb4cb98a82683cfb6165edbfebf
          } else {
            reject(error);
          }
        });
      });
<<<<<<< HEAD
    })
    .catch(error => {
      console.error(error.message);
    });
}


const movieId = process.argv[2];

if (!movieId) {
  console.error("Usage: node script.js <movie_id>");
  process.exit(1);
}

printMovieCharacters(movieId);
=======
      console.log(await promise);
    }
  }
});
>>>>>>> 0041d3ec4b323eb4cb98a82683cfb6165edbfebf
