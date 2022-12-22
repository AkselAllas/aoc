import fs from 'fs'
import readline from 'readline'
import path from 'path'

async function processLineByLine() {
  const fileStream = fs.createReadStream(path.resolve(__dirname, './in'));

  const rl = readline.createInterface({
    input: fileStream,
    crlfDelay: Infinity
  });

  for await (const line of rl) {
    console.log(`Line from file: ${line}`);
  }
}

processLineByLine();