let header = document.querySelector("header");
let toggle = document.querySelector("#toggle_header");

function toggleColor(a, b) {
    header.classList.remove(a);
    header.classList.add(b);
}

toggle.addEventListener('click', function() { header.classList.contains("green") ? toggleColor("green", "red") : toggleColor("red", "green") });