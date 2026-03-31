
const fs = require('fs');
const path = require('path');
let stdinCache = null;
function readLines(file) {
	if (file === '-') {
		if (stdinCache === null) {
			const data = fs.readFileSync(0, { encoding: 'utf-8' });
			stdinCache = data.split(/\r?\n/);
		}
		return stdinCache;
	}
	try {
		const data = fs.readFileSync(path.resolve(file), { encoding: 'utf-8' });
		return data.split(/\r?\n/);
	} catch (err) {
		console.error(`Error reading file ${file}:`, err.message);
		process.exit(2);
	}
}
const ARGS = process.argv.slice(2);
const rawFlags = ARGS.filter((arg) => arg.startsWith('-'));
const flagsSet = new Set();
rawFlags.forEach((flag) => {
	if (flag.startsWith('--') || flag.length === 2) {
		flagsSet.add(flag);
	} else {
		for (const ch of flag.slice(1)) flagsSet.add('-' + ch);
	}
});
const nonFlags = ARGS.filter((arg) => !arg.startsWith('-'));
const pattern = nonFlags[0];
const files = nonFlags.slice(1);
function hasFlag(f) {
	return flagsSet.has('-' + f);
}
if (!pattern) {
	console.error('Usage: exercism-grep [-ixlnv] <pattern> [files...]');
	process.exit(1);
}
if (files.length === 0) files.push('-');
const printedFiles = new Set();
files.forEach(function (file) {
	const lines = readLines(file);
	lines.forEach(function (line, index) {
		if (index === lines.length - 1 && line === '') return;
		const lineToCompare = hasFlag('i') ? line.toLowerCase() : line;
		const patternToCompare = hasFlag('i') ? pattern.toLowerCase() : pattern;
		let isMatch =
			hasFlag('x') ?
				lineToCompare === patternToCompare
			:	lineToCompare.indexOf(patternToCompare) !== -1;
		if (hasFlag('v')) isMatch = !isMatch;
		if (isMatch) {
			if (hasFlag('l')) {
				if (!printedFiles.has(file)) {
					console.log(file);
					printedFiles.add(file);
				}
				return;
			}
			let output = '';
			if (files.length > 1) output += file + ':';
			if (hasFlag('n')) output += `${index + 1}:`;
			output += line;
			console.log(output);
		}
	});
});
// resubmit
// resubmitted
