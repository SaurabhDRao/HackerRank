'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

function getLetter(s) {
    const firstChar = s[0];
    let letter;
    // Write your code here
    let a = ["a", "e", "i", "o", "u"]
    let b = ["b", "c", "d", "f", "g"]
    let h = ["h", "j", "k", "l", "m"]
    switch (firstChar) {
        case (a.includes(firstChar) ? firstChar : null):
            letter = "A";
            break;
        case (b.includes(firstChar) ? firstChar : null):
            letter = "B";
            break;
        case (h.includes(firstChar) ? firstChar : null):
            letter = "C";
            break;
        default:
            letter = "D";
            break;
    }
    return letter;
}


function main() {
    const s = readLine();
    
    console.log(getLetter(s));
}