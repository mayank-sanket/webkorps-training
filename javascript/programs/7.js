// create a function that returns the largest string among two or more strings



let returnLargestString = function(...str){
        let strArray = [];
        for(let i=0; i<str.length; i++){
            strArray.push(str[i]);
        }

        let sortedLengthArray = strArray.map((a) => a.length).atsort((a, b) => a - b);
        
        
}



console.log(returnLargestString("a", "abadefghi", "stem", "abc", "ax", "kfdfjdklfjdk;fjdkfl", "bcedf")
)