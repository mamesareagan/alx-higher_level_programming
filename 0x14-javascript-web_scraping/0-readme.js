#!/usr/bin/node

/*
 * reads from a file and prints it's content
 */
const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', (err, data) => {
  console.log(err || data);
});
