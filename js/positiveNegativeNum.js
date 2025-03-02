/* Find Positive or Negative Number */

function checkNumber(num) {
  if (num > 0) {
    console.log(`${num} is a positive number`);
  } else if (num < 0) {
    console.log(`${num} is a negative number`);
  } else {
    console.log(`${num} is zero`);
  }
}

// Test the function
checkNumber(10);   // Output: 10 is a positive number
checkNumber(-5);   // Output: -5 is a negative number
checkNumber(0);    // Output: 0 is zero