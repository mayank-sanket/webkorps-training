// calculate the time it takes between a setTimeOut call and the inner function actually running

// let t = Date.now();
// let doSomething = function(){
    

//     setTimeout(function(){
//         console.log(`Time Taken: ${(Date.now() - t)/1000}s`)
//     }, 1000)
// }

// doSomething()


const start = Date.now();

setTimeout(()=>{
    const end = Date.now();
    const elapsed = end -start;

    console.log(`Expected delay: 1s`)
    console.log(`Actual delay: ${elapsed/1000}s`)

}, 1000)