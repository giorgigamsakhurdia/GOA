function greet() {
    let name = prompt("Enter your name: ")
    if (name != "") {
        alert("Greetings, " + name)
    } else {
        alert("Greetings, Guest")
    }
}

greet()


function add_numbers() {
    let a = parseInt(prompt("Enter your number: "))
    if (a.length === 0) {
        a = 0
    }
    let b = 2
    console.log(a + b)
}

add_numbers()


function calculate_area() {
    let s = parseInt(prompt("Enter Length: "))
    if (s = " ") {
        s = 1
    }
    let g = parseInt(prompt("Enter Width: "))
    console.log(s * g)
}

calculate_area()


function convert_temperature() {
    let C = prompt("Enter celsius: ")
    let Feh = (C * 9/5) + 32
    console.log(Feh)
}

convert_temperature()


function add_to_shopping_list() {
    let quan = prompt("How many/much?")
    let item = prompt("What do you want to buy?")
    if (quan.length === 0){
        quan === 1;
    }
    console.log(quan, item)
}

add_to_shopping_list()