const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();

app.get('/', (req, res) => {
  res.type('text');
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  res.type('text');
  res.write('This is the list of our students\n');

  const database = process.argv[2];

  try {
    const output = await countStudents(database);
    res.end(output);
  } catch (error) {
    res.end(error.message);
  }
});

app.listen(1245);

module.exports = app;
