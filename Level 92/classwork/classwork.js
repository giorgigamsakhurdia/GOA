let a = document.getElementById("number");
let b = document.getElementById("input");
let c = document.getElementById("error")
let allLetters = /^[a-zA-Z]*$/;


b.oninput = function () {
    a.textContent = b.value.length;
};

b.oninput = function () {
    if(!allLetters.test(b.value)) {
        c.style.opacity = "1"
        c.style.color = "red"
    }
};