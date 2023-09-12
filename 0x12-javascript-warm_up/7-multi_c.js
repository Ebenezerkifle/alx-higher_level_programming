#!/usr/bin/node
if(process.argv[2] !== undefined && parseInt(process.argv[2], 10) !== NaN){
    for (let i=0; i<parseInt(process.argv[2], 10); i++){
        console.log('C is fun');
    }
}
else{
    console.log('Missing number of occurrences');
}