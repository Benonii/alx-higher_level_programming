#!/usr/bin/node

exports.esrever = function (list) {
  let i, j;
  const reversedList = [];

  for (i = 0, j = list.length - 1; i < list.length && j >= 0; i++, j--) {
    reversedList[i] = list[j];
  }

  return (reversedList);
};
