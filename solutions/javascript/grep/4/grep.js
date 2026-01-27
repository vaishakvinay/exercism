// Completed Grep exercise 


const fs = require("fs");
const path = require("path");


function readLines(file) {
  const data = fs.readFileSync(path.resolve(file), { encoding: "utf-8" });
  return data.split(/\r?\n/);
}


const VALID_OPTIONS = ["n", "l", "i", "v", "x"];
const ARGS = process.argv.slice(2);


const flags = new Set();
let pattern;
let inputs = [];

for (const arg of ARGS) {
  if (arg.startsWith("-")) {
    const opt = arg[1];
    if (!VALID_OPTIONS.includes(opt)) {
      throw new Error(`Invalid option: ${opt}`);
    }
    flags.add(opt);
  } else if (pattern === undefined) {
    pattern = arg;
  } else {
    inputs.push(arg);
  }
}


if (flags.has("x")) {
  pattern = `^${pattern}$`;
}

pattern = new RegExp(pattern, flags.has("i") ? "i" : "");


for (const input of inputs) {
  const lines = readLines(input);

  for (const [lineNumber, line] of lines.entries()) {
    let matches = line.match(pattern);

   
    if (flags.has("v")) {
      matches = !matches;
    }

    if (matches) {
     
      if (flags.has("l")) {
        console.log(input);
        break;
      }

      let prefix = "";

     
      if (inputs.length > 1) {
        prefix += `${input}:`;
      }

   
      if (flags.has("n")) {
        prefix += `${lineNumber + 1}:`;
      }

      console.log(prefix + line);
    }
  }
}

