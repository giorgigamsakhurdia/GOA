//1

const greet = (name = "მაყურებელი") => `გამარჯობა, ${name}!`;

//2

const sum = (a = 0, b = 5) => a + b;

//3

const maxNumber = (a = 10, b = 20) => (a > b ? a : b);

//4

const multiply = (a = 1, b = 2, c = 3) => a * b * c;

//5

const calculatePrice = (price, tax = 0.05) => price + (price * tax);

//6

const repeatText = (text, count = 3) => text.repeat(count);

//7

const isGreater = (a = 5, b = 10) => a > b;

//8
//9
//10
//idk