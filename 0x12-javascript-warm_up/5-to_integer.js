#!/usr/bin/node
const arg = process.argv[2];
if (parseInt(arg)) {
    console.log('My number:', process.argv[2]);
} else {
    console.log('Not a number');
}
