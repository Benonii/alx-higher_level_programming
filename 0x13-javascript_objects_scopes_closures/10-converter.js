#!/usr/bin/node

exports.converter = function (base) {
  const symbols = '0123456789abcdef';

  function convertToBase (number) {
    if (number < base) {
      return symbols[number];
    } else {
      const quotient = Math.floor(number / base);
      const remainder = number % base;
      return convertToBase(quotient) + symbols[remainder];
    }
  }

  return (convertToBase);
};
