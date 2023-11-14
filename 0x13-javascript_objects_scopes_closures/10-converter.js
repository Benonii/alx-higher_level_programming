#!/usr/bin/node

exports.converter = function (base) {
  const symbols = '0123456789abcdef';

  const convertToBase = number =>
    number < base
      ? symbols[number]
      : convertToBase(Math.floor(number / base)) + symbols[number % base];

  return convertToBase;
};
