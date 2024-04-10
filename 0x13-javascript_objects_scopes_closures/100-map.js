#!/usr/bin/node
let list = require('./100-data.js').list;
console.log(list);
console.log(list.map((value, index) => value * index));
