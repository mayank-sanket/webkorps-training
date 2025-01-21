const fetchBtn = document.getElementById('fetchBtn')

fetchBtn.addEventListener('click', fetchBtnHandler)

function fetchBtnHandler(){
    console.log('You have clicked the button!')

    // instantiate an xhr object
    const xhr = new XMLHttpRequest();


    // open the object
    xhr.open('GET', './mayank.txt', true)



    // What to do on progress (optional)

    xhr.onprogress = function(){
        console.log('Progressing ...')

    }

    // what to do when response is ready

    xhr.onload = function(){

       if(this.status === 200){
        console.log(this.responseText)
       }
       else{
        console.log('some error occured')
       }
    }


    // note: earlier syntax

    // xhr.onreadystatechange = function(){
    //     // console.log(this.readyState)  
    //     // refer MDN docs for more info
    //    if(this.readyState == 4){
    //     console.log(this.responseText)
    //    }
    // }

    // but in order to to all this, you need to send the request also

    // send the request

    xhr.send()


    // console.log("We are done!")

}