


const API_KEY = '8af9d4a757d541afa7573534252001';
const URL = 'http://api.weatherapi.com/v1/current.json?'

async function WeatherDetails(city){
    const response = await fetch(`${URL}key=${API_KEY}&q=${city}&aqi=no`)
    const data = await response.json();
    console.log(data);
    const cityName = data.location.name;
    const feelsLike = data.current.feelslike_c;
    const actualTemp = data.current.temp_c;
    const windSpeed = data.current.gust_kph;
    const icon = data.current.condition.icon;
    const condition = data.current.condition.text;
    


    document.querySelector("#city").innerHTML = cityName;
    document.querySelector("#temp").innerHTML = `Feels Like: ${feelsLike}`
    document.querySelector('#weather_icon').src = `https:${icon}`;
    document.querySelector('#condition').innerHTML = condition;
    document.querySelector('#temp_actual').innerHTML = actualTemp;
}


window.onload = function(){
    WeatherDetails("Indore")
}
document.querySelector('#request_btn').addEventListener('click', function(e){
    const city = document.getElementById('input_city').value.toLowerCase();
    WeatherDetails(city);
})














