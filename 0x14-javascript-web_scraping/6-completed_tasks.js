#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const userTaskDict = {
  1: 0,
  2: 0,
  3: 0,
  4: 0,
  5: 0,
  6: 0,
  7: 0,
  8: 0,
  9: 0,
  10: 0
};

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
    process.exit(1);
  } else {
    const allTasks = JSON.parse(body);

    for (const task of allTasks) {
      if (task.completed === true) {
        userTaskDict[task.userId] += 1;
      }
    }
    console.log(userTaskDict);
  }
});
