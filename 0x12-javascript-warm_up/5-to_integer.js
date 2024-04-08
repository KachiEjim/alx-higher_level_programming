#!/usr/bin/node

let argv = process.argv;
let num = Number(argv[2]);

if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: ${num}');
}
