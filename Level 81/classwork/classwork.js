// let t = document.getElementById("yes");
// let x = 0;
// let y = 0;
// let direction = "r";

// function anime() {
//     const width = document.documentElement.clientWidth;
//     const height = document.documentElement.clientHeight;

//     if (direction === "r") {
//         x += 1;
//         if (x >= width) {
//             direction = "d";
//         }
//     } else if (direction === "d") {
//         y += 1;
//         if (y >= height) {
//             direction = "l";
//         }
//     } else if (direction === "l") {
//         x -= 1;
//         if (x <= 0) {
//             direction = "u";
//         }
//     } else if (direction === "u") {
//         y -= 1;
//         if (y <= 0) {
//             direction = "r";
//         }
//     }

//     t.style.transform = `translate(${x}px, ${y}px)`;
// }

// setInterval(anime, 1);


let y = 0;

function upDown() {
    const v = document.getElementById("yes"); 
    y += 1; 
    v.style.bottom = y + 'px'; 
    setInterval(upDown, 50);
}

