fs = require('fs');
//Synchronously read file because my brain is too small for Async
const data = fs.readFileSync('D1/input.txt',
            {encoding:'utf8', flag:'r'});

const dataArray = data.split('\n');

var solution = 0;

for (let i = 1; i <= dataArray.length; i++) { //Skip first Iteration intentionally
    if (parseInt(dataArray[i]) > parseInt(dataArray[i-1])) {
        solution +=1;
    }
};

console.log("Question 1: " + solution );


var solution_2 = 0;
let rollingSum = []; 
for (let i = 2; i <= dataArray.length-1; i++) { //Skip first two iterations intentionally
    rollingSum[i-2] = parseInt(dataArray[i])+parseInt(dataArray[i-1])+parseInt(dataArray[i-2]);
    
};


for (let i = 0; i <= rollingSum.length; i++) { //Loop through array of rolling sums and compares
    if (rollingSum[i] > rollingSum[i-1]) {
        solution_2 +=1;
    }
};

console.log("Question 2: " + solution_2 );

