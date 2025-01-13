// create a counter that counts from 1 to 30 every second

function print(number){
    let count = 1;

    let interval = setInterval(function(){
        console.log(count);
        if(count === 30) {
            clearInterval(interval)
            console.log("Counting Completed!")
        }
        count++;
    }, 1000);
    
    
}

print(30)