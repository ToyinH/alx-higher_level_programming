#!/usr/bin/node
const argCount = process.argv.length;
if (argCount === 2) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
