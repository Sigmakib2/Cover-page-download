#!/usr/bin/env node
const fs = require('fs');
const vm = require('vm');
const path = require('path');

const inputPath = process.argv[2] || path.join(__dirname, 'students.js');
const outputPath = process.argv[3] || path.join(process.cwd(), 'students.csv');

function csvEscape(value) {
  if (value === null || value === undefined) return '';
  const s = String(value);
  // Escape only when necessary
  if (/[",\n\r]/.test(s)) return '"' + s.replace(/"/g, '""') + '"';
  return s;
}

try {
  const code = fs.readFileSync(inputPath, 'utf8');

  // Wrap the file so we can return the studentsData variable if present.
  const wrapped = `(function(){\n${code}\nreturn typeof studentsData !== 'undefined' ? studentsData : null;\n})()`;

  // Run in a fresh VM context to avoid polluting the current environment.
  const data = vm.runInNewContext(wrapped, {}, { timeout: 2000 });

  if (!Array.isArray(data)) {
    console.error('Could not find studentsData array in', inputPath);
    process.exit(2);
  }

  const header = ['name', 'regNo', 'session'];
  const rows = [header.join(',')];

  for (const student of data) {
    rows.push([
      csvEscape(student.name),
      csvEscape(student.regNo),
      csvEscape(student.session)
    ].join(','));
  }

  fs.writeFileSync(outputPath, rows.join('\n'), 'utf8');
  console.log(`Wrote ${data.length} rows to ${outputPath}`);
} catch (err) {
  console.error('Error:', err.message);
  process.exit(1);
}