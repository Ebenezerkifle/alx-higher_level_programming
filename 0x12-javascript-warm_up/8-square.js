#!/usr/bin/node
let argument = process.argv[2];
if ( argument !== undefined && parseInt(argument, 10) !== NaN){
    for (let i = 0; i < parseInt(argument, 10); i++){
        let output='';
        for (let j = 0; j < parseInt(argument,10); j++){
            output += 'X';
        }
        console.log(output);
    }
}
else{
    console.log('Missing size');
}