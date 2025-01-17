const obj1 = {
name: "Mayank",
age: 23
}

const obj2 = Object.assign(obj1)

obj2.name = "Sanket";

console.log(obj1)


// obj2 = obj1 -> shallow copy | memory reference
// obj2 = Object.assign(obj1)  -> shallow copy
// obj2 = JSON.parse(JSON.stringify(obj1))   -> deep copy (but lossy, date, functions, null, etc are lost)
// obj2 = {...obj1} => deep copy at 1 level of nesting only


const abc = {
    name: "abc"
}

const def = {...abc}

def.name = "def"

console.log(`abc: ${abc.name}`)
console.log(`def: ${def.name}`)


let o1 = {
    name: "object 1",
    minutes: new Date().getMinutes(),
    greet: function(){
        console.log(`hello ${this.name}`)
    }
}

let o2 = {...o1}

o2.name = "object 2"
o2.greet();



// testing level of deep copy using spread operator (deep copy at ONE LEVEL only, at other levels it behaves like shallow copy)

let wk1 = {
    name: "mayank",
    details: {
        location: "Indore", 
        shift: {
            normal: "day",
            monthend: "night"
        }
    }
}

let wk2 = {...wk1}
wk2.details.location = "Delhi"
// console.log(wk1.details.location); // prints Delhi



// HOW TO DEEP CLONE AT MULTIPLE LEVELS OF NESTING? USE LODASH library

const lodash = require('lodash')

const em1 = {
    name: "mayank",
    details: {
        location: "Indore", 
        shift: {
            normal: "day",
            monthend: "night"
        }
    }
}

const em2 = lodash.cloneDeep(em1)
em2.details.location = "New York"

console.log(em1.details.location) // prints Indore : deep clone at multiple levels





