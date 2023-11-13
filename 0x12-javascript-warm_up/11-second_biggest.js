#!/usr/bin/node

const findSecondLargest = (numbers) => {
  const uniqueNumbers = [...new Set(numbers)]; // Remove duplicates
  const sortedNumbers = uniqueNumbers.sort((a, b) => b - a);

  if (sortedNumbers.length >= 2) {
    return sortedNumbers[1];
  } else {
    return 0;
  }
};

// Get the command-line arguments as integers
const numbers = process.argv.slice(2).map(Number);

// Find and print the second biggest integer
console.log(findSecondLargest(numbers));
