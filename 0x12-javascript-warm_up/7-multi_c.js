#!/usr/bin/node
let argv = process.argv;
let occur = Number(argv[2]);

if (isNaN(occur)) {
    console.log('Missing number of occurrences');
} else {
    for (let i = 0; i < occur; i++) {
        console.log('C is fun');
    }
}
