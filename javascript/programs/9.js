const arr = [1, 3, 5, 65, 54, 21]

const someOver34 = arr.some((val, ind,arr )=> val>34 )

console.log(typeof someOver34); // boolean
console.log(someOver34); // true