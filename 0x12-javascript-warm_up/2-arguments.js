#!/usr/bin/node
/* prints a message depending on the number of arguments passed */
const argCount = process.argv.length;
console.log(argCount === 2 ? 'No argument' : argCount === 3 ? 'Argument found' : 'Arguments found');
