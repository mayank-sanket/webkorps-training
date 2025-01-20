
const API_KEY = '8af9d4a757d541afa7573534252001';
const URL = 'http://api.weatherapi.com/v1/current.json?';

window.onload = function(){
    // WeatherDetailsByCity("Indore");

    // fetchPIN(852201);

    document.getElementById('details_container').innerHTML = `<h1>Please select the query type from the above menu!</h1>`;
    document.getElementById('request_btn').style.display = 'none';
}
async function fetchPIN(pincode) {
    const response = await fetch(`https://api.postalpincode.in/pincode/${pincode}`);
    const data = await response.json();
    pinToCity = await data[0].PostOffice[0].District.toLowerCase();
    return pinToCity;

}
async function WeatherDetailsByCity(city){
    const response = await fetch(`${URL}key=${API_KEY}&q=${city}&aqi=no`)
    const data = await response.json();
    // console.log(data);
    const cityName = data.location.name;
    const feelsLike = data.current.feelslike_c;
    const actualTemp = data.current.temp_c;
    const windSpeed = data.current.gust_kph;
    const icon = data.current.condition.icon;
    const condition = data.current.condition.text;
    
    document.getElementById('details_container').innerHTML = '';
    document.getElementById('details_container').innerHTML  += `<h1 class="city" id="city"></h1> 
            <br>
            <h2 class="condition" id="condition"></h2>
            <br>
            <h2 class="temp-actual" id="temp_actual"></h2>
            <br>
            <h2 class="temp" id="temp"></h2>
            <br>

            <img src="" alt="" id="weather_icon">`


    document.querySelector("#city").innerHTML = cityName;
    document.querySelector("#temp").innerHTML = `Feels Like: ${feelsLike}`
    document.querySelector('#weather_icon').src = `https:${icon}`;
    document.querySelector('#condition').innerHTML = condition;
    document.querySelector('#temp_actual').innerHTML = actualTemp;
}








const dropdown = document.getElementById('dropdown');
dropdown.addEventListener('change', function(){
    
    if(dropdown.value =='city'){
        

        document.querySelector(".form_container").innerHTML = `  <div id="one" class="choice">
        <label for="input_city"><h2>Enter City Name</h2></label>
        <br>
        <input type="text" name="" id="input_city">
        
        <br>
       </div>`;

       document.getElementById('request_btn').style.display = 'block';
       
    }

    if(dropdown.value == 'pin'){
        
        document.querySelector(".form_container").innerHTML = ''
        document.querySelector(".form_container").innerHTML += `
        <div id="two" class="choice">
        <label for="city_pin">Enter City PIN</label> <br>
        <input type="number" name="" id="input_pin">
        
       </div>
        `

        document.getElementById('request_btn').style.display = 'block';
    }

    if(dropdown.value == 'coordinates'){
        
        document.querySelector(".form_container").innerHTML = '';
        document.querySelector(".form_container").innerHTML += `
         <div id="three" class="choice" style = "display: flex; flex-direction: column; gap: 8px">
            <label for="latitute">Enter latitute</label> 
            <input type="number" name="" id="input_"latitude>
            <label for="longitude">Enter longitude</label>
            <input type="number" name="" id="input_longitude"> 
            
           </div>
        `
        document.getElementById('request_btn').style.display = 'block';
    }
})




document.querySelector('#request_btn').addEventListener('click', function(e){
    
    if(dropdown.value === 'city'){
        const city_value = document.getElementById('input_city').value
        WeatherDetailsByCity(city_value)
    }

   

   if(dropdown.value === 'pin'){

    const pin_value = document.getElementById('input_pin').value
    const pr = new Promise((resolve, reject)=>{
        const result = fetchPIN(pin_value);
        resolve(result)
    })

    pr.then((result)=>{
        WeatherDetailsByCity(result);
    })
    
   }

});























