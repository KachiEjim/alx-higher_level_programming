#!/usr/bin/node
const fileS = require('fs');
const src1 = fileS.readFileSync(process.argv[2], 'utf8');
const src2 = fileS.readFileSync(process.argv[3], 'utf8');
fileS.writeFileSync(process.argv[4], src1 + src2);
