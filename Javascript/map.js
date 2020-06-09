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

const xlocation = []
axios
    .get(url)
    .then((response) => { 
        xlocation.push(response.data.results);
        console.log(xlocation, 'line 18')
    })
    .catch((err) => console.log(err))

function getLocationOfUsers() {
    for (i = 0; i < xlocation.length; i++) {
        //loop through the xlocation array and extract the locations that you need for each map marker
    }
}

getLocationOfUsers();




    // async function getLocationOfUsers() {
    
    //   let res = await axios.get('https://randomuser.me/api/?results=10');
    
    //   let locOfusers = res.data.location;
    //   let location = res.data.location;
    
    //   console.log(`# of followers: ${nOfFollowers}`)
    //   console.log(`Location: ${location}`)
    // }
    
    // getNumberOfFollowers();


// // let marker = L.marker([51.5, -0.09]).addTo(mymap);