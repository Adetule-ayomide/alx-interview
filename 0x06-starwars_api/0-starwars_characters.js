#!/usr/bin/node

const request = require('request');

function getMovieCharacters(movieId) {
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

function printMovieCharacters(movieId) {
  getMovieCharacters(movieId)
    .then(characters => {
      console.log(`Characters in Star Wars Episode ${movieId}:`);
      characters.forEach(characterUrl => {
        request(characterUrl, (error, response, body) => {
          if (error) {
            console.error(`Failed to retrieve character data for ${characterUrl}`, error);
          } else if (response.statusCode !== 200) {
            console.error(`Failed to retrieve character data for ${characterUrl}. Status code: ${response.statusCode}`);
          } else {
            const characterData = JSON.parse(body);
            console.log(characterData.name);
          }
        });
      });
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
