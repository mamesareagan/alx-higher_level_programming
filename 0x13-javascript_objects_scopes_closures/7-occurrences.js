#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  list.forEach((value, index) => {
   if (value === searchElement) {
     i++;
   }
  });
  return i;
};
