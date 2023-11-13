#!/usr/bin/node
function add (a, b) {
  console.log(a + b);
}

const firstArg = parseInt(process.argv[2]);
const secondArg = parseInt(process.argv[3]);
add(firstArg, secondArg);
