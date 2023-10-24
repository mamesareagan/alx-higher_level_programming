#!/usr/bin/node

/*
 * display status code of a get request
 */
const request = require('request');

request.get(process.argv[2], (error, response) => {
  if (error) {
    console.log(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
