function factorial(n) {
  if (n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

// Prompt the user to enter a number
const num = parseInt(prompt("Enter a number:"));

// Calculate the factorial
const result = factorial(num);

// Display the result
console.log(`The factorial of ${num} is ${result}`);

