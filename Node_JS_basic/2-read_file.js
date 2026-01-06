const fs = require('fs');
const { parse } = require('csv-parse/sync');


function countStudents(path) {
  try {
    let totalStudents = 0;
    const results = {};

    const data = fs.readFileSync(path, 'utf8');
    const records = parse(data, { columns: true, skip_empty_lines: true });

    for (const row of records) {
      totalStudents += 1;
      if (!(row.field in results)) {
        results[row.field] = { students_nb: 1, students_list: [row.firstname] };
      } else {
        results[row.field].students_nb += 1;
        results[row.field].students_list.push(row.firstname);
      }
    }
    console.log(`Number of students: ${totalStudents}`);
    for (const [key, value] of Object.entries(results)) {
      console.log(`Number of students in ${key}: ${value.students_nb}. List: ${value.students_list.join(', ')}`);
    }
  } catch (error) {
    console.log('Cannot load the database');
  }
}

module.exports = countStudents;
