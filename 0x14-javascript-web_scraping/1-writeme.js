const fs = require('fs');
const file = 'output.txt';
const data = 'Hello, World!';

fs.writeFile(file, data, 'utf8', (err) => {
  if (err) {
    console.log('Error:', err);
  } else {
    console.log('File written successfully');
  }
});

console.log('This line runs immediately after fs.writeFile is called, not after it completes.');