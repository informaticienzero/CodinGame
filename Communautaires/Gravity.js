const inputs = readline().split(' ');
const width = parseInt(inputs[0]);
const height = parseInt(inputs[1]);

let lines = [];
for (let i = 0; i < height; i++) {
    lines.push(readline());
}

function first(i) {
    for (let j = 0; j < height; ++j) {
        if (lines[j][i] === '#') {
            return j;
        }
    }
    
    return -1;
}

for (let i = 0; i < width; ++i) {
    // Loop from the end.
    for (let j = height - 1; j >= 0; --j) {
        if (lines[j][i] === '.') {
            let index = first(i);
            if (index < j && index != -1) {
                lines[j] = lines[j].substr(0, i) + '#' + lines[j].substr(i + 1);
                lines[index] = lines[index].substr(0, i) + '.' + lines[index].substr(i + 1)
            }
        }
    }
}

lines.forEach((line) => {
   print(line); 
});
