#!/usr/bin/node

let i;
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      return (null);
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
