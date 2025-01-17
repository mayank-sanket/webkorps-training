// THIS

/*

The handling of this is also different in arrow functions compared to regular functions.

In short, with arrow functions there are no binding of this.

In regular functions the this keyword represented the object that CALLED the function, which could be the window, the document, a button or whatever.

With arrow functions the this keyword always represents the object that DEFINED the arrow function.

*/


let person = {
    name : "mayank",
    greet: function() {
        return this.name;
    }
}

console.log(person.greet()) // mayank

let person2 = {
    name: "sanket",
    greet: ()=> this.name // undefined
} 

console.log(person2.greet())



