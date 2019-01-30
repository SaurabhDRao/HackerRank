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

const getMaxLessThanK = (n, k) => {
    var i, j;
    var max = 0;
    for (i = 1; i < n; i++){
        for (j = i + 1; j <= n; j++){
            var and = i & j;
            if (and > max && and < k)
                max = and;
        }
    }
    return max;
}


function main() {
    const q = +(readLine());
    
    for (let i = 0; i < q; i++) {
        const [n, k] = readLine().split(' ').map(Number);
        
        console.log(getMaxLessThanK(n, k));
    }
}