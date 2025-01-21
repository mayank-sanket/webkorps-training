const fetchBtn = document.getElementById('fetchBtn')

fetchBtn.addEventListener('click', fetchBtnHandler)

function fetchBtnHandler(){
    console.log('You have clicked the button!')

    // instantiate an xhr object
    const xhr = new XMLHttpRequest();


    // open the object
    xhr.open('POST', 'http://dummy.restapiexample.com/api/v1/create', true)
    xhr.getResponseHeader('Content-type', 'application/x-www-form-url-encoded')



    // What to do on progress (optional)

    xhr.onprogress = function(){
        console.log('Progressing ...')

    }

    // what to do when response is ready

    xhr.onload = function(){

    //    if(this.status === 200){
    //     console.log(this.responseText)
    //    }
    //    else{
    //     console.log('some error occured')
    //    }
    }


    let params = 'orem=ipsum&name=binny'
    xhr.send(params)


    

}