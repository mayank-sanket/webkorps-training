// create a terminal clock

setInterval(()=>{
    let date = new Date();
console.log(date.toLocaleTimeString())
}, 1000)