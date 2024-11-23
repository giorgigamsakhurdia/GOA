let i = 1;

function fade() {
    const f = document.getElementById("fadei");
    i -= 0.1;
    f.style.opacity = i
    setInterval(fade, 100)
}

