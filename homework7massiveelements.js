const arr = [4, 4, 8, 3, 3, 3, 2, 4, 4];

arr.forEach((num, i) => console.log(`Element ${i}: ${num}`));

console.log("First 3 elements:", arr.slice(0, 3));

const total = arr.reduce((a, b) => a + b, 0);
console.log("Total sum:", total);

const filtered = arr.filter(x => x !== 4).reduce((a, b) => a + b, 0);
console.log("Sum without 4s:", filtered);