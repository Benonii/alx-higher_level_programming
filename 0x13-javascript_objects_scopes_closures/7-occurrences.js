#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.forEach((element, index) => {
    if (element === searchElement) {
      count++;
    }
  });

  return (count);
};
