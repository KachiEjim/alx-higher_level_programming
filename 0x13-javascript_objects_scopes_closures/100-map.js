#!/usr/bin/node

const listData = require('./100-data').list

console.log(list);
console.log(list.map((x, xI) => x * xI));