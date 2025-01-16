const arr = [1, 3, 4545, 6464, 4645, 343]
const keys = arr.keys();

for (let key of keys){
    console.log(key) // prints 0 to 5
}


const ent = arr.entries();

for(i of ent){
    console.log(i); // [0,1]   [1,3] [2, 4545] and so on  
}