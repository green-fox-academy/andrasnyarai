'use strict'; 

var lineCount = 20;

for (let a = 0; a <= lineCount; a++) {
    if (a == 0) {
        console.log();
    } else if (a == 1) {
        console.log('┌' + '─'.repeat(lineCount) + '┐');
    } else if (a == lineCount) {
        console.log('└' + '─'.repeat(lineCount) + '┘');
    } else if (a % 2 == 0) {
        console.log('│'+ ' □'.repeat(lineCount / 2) + '│');
    } else {
        console.log('│'+ '□ '.repeat(lineCount / 2) + '│');
    }
}
// ◊ ▓