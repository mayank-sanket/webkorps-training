// create a function that return the sum of the input numbers (the number of arguments is not fixed, it is variable)

let generalSum  = function(...str){
    let sum = 0;
    for(let i=0; i<str.length; i++){
        sum += str[i];
    }

    return sum;
}



console.log(generalSum(1, 2, 3, 4))