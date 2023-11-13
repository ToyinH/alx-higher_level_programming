#!/usr/bin/node
const element = process.argv.length;
if (element === 2) {
  console.log('No argument');
} else if (element === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
