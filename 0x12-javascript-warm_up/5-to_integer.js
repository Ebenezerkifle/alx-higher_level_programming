#!/usr/bin/node
// My number: <first argument converter in integer>
if (process.argv[2]!== undefined){
    if (parseInt(process.argv[2], 10) === NaN){
        console.log('Not a number');
    }
    else{
        console.log('My number: '+parseInt(process.argv[2], 10));
    }
}
else{
    console.log('Not a number');
}