// given an array of objects, sort the elements based on a particular property (descending order as well as ascending order)

let users = [
    {name: "mayank", age: 23}, {name: "rahul", age: 22}, {name: "ram", age: 49}]
    
let sortedUsers = users.sort((a, b)=> a.age - b.age);
console.log(sortedUsers)