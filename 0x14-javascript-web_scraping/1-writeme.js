#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2];

try {
  fs.writeFileSync(file, data, 'utf8');
  console.log('File written successfully');
} catch (err) {
  console.log(err);
}
