
let mymap = L.map('mapid').setView([51.505, -0.09], 13);
const url = 'https://randomuser.me/api/?results=10';

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1Ijoiam5hZDY2NjkiLCJhIjoiY2tiMW8wYW11MDJ4cDJ0bXlsem14b210NyJ9.J97-mQdVpCL9L9ORqe7Q9Q'
}).addTo(mymap);

// const xlocation = []
// axios
//     .get(url)
//     .then((response) => { 
//         for (i = 0; i < xlocation.length; i++) {
//         data = xlocation.push(response.data.results);
//         }
//     })
//     .catch((err) => console.log(err))

// function getLocationOfUsers() {
//     for (i = 0; i < xlocation.length; i++) {
//         //loop through the xlocation array and extract the locations that you need for each map marker
//     }
// }

// getLocationOfUsers();


// axios get request and response to display data on html page
axios.get(url)
    .then((response) => { 

        // for loop iterates through data asigning the data to variables.
        for (i = 0; i < 11; i++) {
            const data = response.data.results[i];
            const latitude = data.location.coordinates.latitude;
            const longitude = data.location.coordinates.longitude;
            const first_name = data.name.first;
            const last_name = data.name.last;
            const country = data.location.country;
            const state = data.location.state;
            const city = data.location.city;
            const street_name = data.location.street.name;
            const street_number = data.location.street.number;
            const username = data.login.username;
            const email = data.email;

            // Displays the data in the console
            console.log(data)

            // Markers according to each user's latitude and longitude. .bindPopup adds the data in the above variables to a new location marker each time the for loop runs
            L.marker([latitude, longitude]).addTo(mymap)
            .bindPopup(`<b>${first_name} ${last_name}</b> <br> ${country} <br> ${state} <br> ${city} <br> ${street_name} <br> ${street_number}`)
            .openPopup();

            // DOM Manipulation to alter text inside of 'users' <div> to display user information on the page outside of the map.
            document.getElementById('users').innerHTML += '<br><b>Name:</b>'+first_name+' '+last_name+' <b>Username:</b>'+username+' <b>Email:</b>'+email;
    }
})
    // logs errors in the console to help with debugging
    .catch((err) => console.log(err))