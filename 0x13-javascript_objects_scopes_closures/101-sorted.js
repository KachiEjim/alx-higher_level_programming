#!/usr/bin/node

const dict = require('./101-data').dict;
const dictNew = {};
for (const key in dict) {
  if (dictNew[dict[key]] === undefined) {
    dictNew[dict[key]] = [key];
  } else {
    dictNew[dict[key]].push(key);
  }
}
console.log(dictNew);
