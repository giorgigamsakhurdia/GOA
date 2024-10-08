const a = document.getElementById("f").value;
const b = document.getElementById("s").value;
const c = document.getElementById("t").value;
const d = document.getElementById("r").value;

function check() {
    if (a.length === 0 || b.length === 0 || c.length === 0 || d.length === 0) {
        alert("FILL YOUR EVERYTHING")
    } else {
        return
    }
}

function check2() {
    if (a.length <= 8) {
        alert("Passwork is too short")
    }
}

console.log("a:", a, "b:", b, "c:", c, "d:", d); 

