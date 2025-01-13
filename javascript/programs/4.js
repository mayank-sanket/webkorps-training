// write a program that prints the time in HH:MM:SS format (without using the toLocaleString() method) and also stop the counter if seconds value reaches 30

let checkTime = function(num){
    return (num<10)? "0"+num : num;

}


function printTime(){
    

    

    let interval = setInterval(()=>{
        let t = new Date();
        let h = checkTime(t.getHours());
    let m = checkTime(t.getMinutes());
    let s = checkTime(t.getSeconds());
        if(s == 30) clearInterval(interval);
        console.log(`${h}:${m}:${s}`)
    }, 1000)
    
}

printTime()
