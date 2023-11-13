#!/usr/bin/node
function factorial (a) {
  if (a === 1 || a === 0) {
    return 1;
  } else if (isNaN(a)) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}
const firstArg = parseInt(process.argv[2]);
const num = factorial(firstArg);
console.log(num);
