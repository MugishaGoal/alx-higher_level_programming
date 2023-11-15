#!/usr/bin/node
const arg = process.argv[2];
const num = parseInt(arg);
if (isNaN(num) || num <= 0) {
    console.log('Missing number of occurrences');
} else {
    for (let x = 0; x < num; x++) {
        console.log('C is fun');
    }
}