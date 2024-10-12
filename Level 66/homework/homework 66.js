//first

function odd_or_even() {
    let a = parseInt(prompt("Enter your number: "))
    if (a % 2 === 0) {
        console.log("This number is even")
    } else {
        console.log("This number is odd")
    }
}


odd_or_even()

//second

function list_sum() {
    let b = [2, 4, 5];
    if (b.length === 0) {
        console.log("list is empty")
    } else {
        let sum = 0
        for (let i = 0; i < b.length; i++) {
            sum += b[i];  
        }
        console.log(sum)
    }
}

list_sum()

//third

function multiply(numbers) {
    let result = [];
    for (let i = 0; i < numbers.length; i++) {
        let multiplied = numbers[i] * 3;
        if (multiplied > 20) {
            result.push(multiplied);  // თუ რიცხვი 20-ზე მეტია, ამატებს მას შედეგში
        }
    }
    console.log(result) 
}

const numbers = [2, 10, 11]
multiply(numbers)
