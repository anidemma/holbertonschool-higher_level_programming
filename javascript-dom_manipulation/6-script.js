const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json'

function fetchData() {
    fetch(url)
    .then(response => {
      if(!response.ok) throw new Error("Error");
      return response.json();
    })
    .then(data => {
      let display_character = document.querySelector("#character");
      display_character.innerHTML = data.name;
    })
    .catch(error => {console.log("error", error);});
  }
  
  fetchData();