const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

function fetchLang() {
  fetch(url)
  .then(response=> {
    if(!response.ok) throw new Error('Error');
    return response.json();
  })
  .then(data => {
    let text = document.querySelector('#hello');
    text.innerHTML = data.hello;
  })
  .catch(error => { console.log('error', error);})
}

fetchLang();