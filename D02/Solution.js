const filePath = 'D2/input.txt';
//const filePath = 'D2/test.txt';

fs = require('fs');
const data = fs.readFileSync(filePath,
            {encoding:'utf8', flag:'r'});
const dataArray = data.split('\n');


function inter_line(lines) {
    var result = []
    for (let i = 0; i < dataArray.length; i++) { 
        result.push(dataArray[i].replace('\r', '').split(' '));
    }
    var forward = 0;
    var depth = 0;

    for (let j = 0; j < result.length; j++) { 
        if (result[j][0] == 'forward') {
            forward += parseInt(result[j][1]);

        } else if (result[j][0] == 'up') {
            depth -= parseInt(result[j][1]);

        } else { //Implied Down
            depth += parseInt(result[j][1]);
        };}
    return forward*depth;   
  }

function back_at_it_again(lines) {
    var result = []
    for (let i = 0; i < dataArray.length; i++) { 
        result.push(dataArray[i].replace('\r', '').split(' '));
    }
    var forward = 0;
    var depth = 0;
    var aim = 0;
    for (let j = 0; j < result.length; j++) { 
        if (result[j][0] == 'down') {
            aim += parseInt(result[j][1]);

        } else if (result[j][0] == 'up') {
            aim -= parseInt(result[j][1]);

        } else { //Implied Forward
            forward += parseInt(result[j][1]);
            depth += aim*parseInt(result[j][1]);
        };}
    return forward*depth
}


console.log('Answer 1: ' + inter_line(dataArray));
console.log('Answer 2: ' + back_at_it_again(dataArray));