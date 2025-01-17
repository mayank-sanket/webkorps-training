// Destructuring in Objects

const person = {
    fName: "Mayank",
    lName: "Sanket",
    greet: function(){
        return `Hello, ${this.fName} ${this.lName}!`
    }
}

// const {fName, lName} = person
// console.log(fName) // Mayank
// console.log(lName) // Sanket

// -------------------------------



// const {fName, lName, greet} = person

// console.log(fName) // Mayank
// console.log(greet()) // Hello, undefined undefined!

// ---------------------------------------------------



// Destructuring in Arrays

const arr = [1, 3, 4, 5, 6]
const [firstElem, secondElem] = arr
console.log(firstElem) // 1



// using Rest operator in destructuring

const crr = [1, 3, 4, 56, 454, 4, 343, 344, 3434, 232]

const [a, b, c, ...lastelm] = crr
// here, the first 3 values represent the first 3 elements of the array crr but lastelm represents the other elements of the array (put together in an array named lastelm)





// Destructuring nested arrays

const brr = [1, [1, 3, 45454, 454] , [3, 2, 1], [1, 3], 4]

const [firstArr, secondArr, thirdArr, fourthArr] = brr
console.log(secondArr) // [ 1, 3, 45454, 454 ]
console.log(secondArr[1]) // 3


// ----------------------------------------------------


// Destructuring in nested Objects

let address = {locality: "Vijay Nagar", city: "Indore", state: "Madhya Pradesh"}
let user = {
    name: "Mayank Sanket",
    age: 23,

    address
}

let {name, age, address: {city}} = user  // city is being unpacked here

console.log(name)
console.log(age)
console.log(city)



// Default values

let {isRemote = false, isAvailable = false} = person

console.log(isRemote) // prints false




// Mixed Destructuring

const usr = {
    name: "William Benson",
    age: 20,
    address: {
      town: "Maryland",
      state: "Lagos"
    },
    hobbies: ["Swimming", "Golf", "Writing"]
  };
  
  const { nm, ag, address: { town, state }, hobbies: [firstHobby] } = usr;




// Destructuring function parameters

function greet({ name, age }) {
    console.log(`Hello, ${name}. You are ${age} years old.`);
  }
  
  greet({ name: "Peter", age: 50 }); 




//   Destructuring in Strings

let str = "W3Schools";

// 
let [a1, a2, a3, a4, a5] = str;
console.log(a1)


// Skipping array elements


const fruits = ["Bananas", "Oranges", "Apples", "Mangos", "Pineapples"];


let [fruit1,,,fruit2] = fruits;
console.log(fruit2) // Mangos



// array position values



const frts = ["Bananas", "Oranges", "Apples", "Mangos"];
// Destructuring
let {[0]:frt1 ,[1]:frt2} = frts;

console.log(frt1) // Bananas


// Swapping javascript values

let firstName = "John";
let lastName = "Doe";


[firstName, lastName] = [lastName, firstName];
console.log(firstName)  // Doe



// DESTRUCTURING MAPS

const price = new Map();
price.set('Apples', 200);
price.set('Bananas', 60);
price.set('Grapes', 130)

for([k,v] of price){
  console.log(`${k} : ${v}`) 
}