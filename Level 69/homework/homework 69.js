//first
let array = [1, 2, 3, 4, 5];
let length = array.length;
console.log(length)

//second

let secondarray = [1, 2, 3, 4, 5];
let arraystring = secondarray.toString();
console.log(arraystring)

//third

let thirdarray = [1, 2, 3, 4, 5];
let Element = myArray.at(1);
console.log(Element)

//fourth

let fourtharray = [1, 2, 3, 4, 5];
let joinedArray = fourtharray.join('-');
console.log(joinedArray)

//fifth

let fiftharray = [1, 2, 3, 4, 5];
fiftharray.push(6, 7); 
fiftharray.pop();
console.log(fiftharray)

//sixth

let sixtharray = [1, 2, 3, 4, 5]; 
let removedElement = sixtharray.shift();
console.log(removedElement)

//seventh

let seventharray = [2, 3, 4, 5]; 
seventharray.unshift(1); 
console.log(seventharray)


//eighth

let eightharray = [1, 2, 3, 4, 5];
delete eightharray[4]; 

//ninth

let nintharray1 = [1, 2, 3];     
let nintharray2 = [4, 5, 6];      
let botharray = nintharray1.concat(nintharray2);

//tenth

let tentharray = [2, 3, 4, 5]; 
tentharray.unshift(1); 
console.log(tentharray.length)

//eleventh

let eleventharray = [1, 12, 3, 2, 4, 2];
let index = eleventharray.indexOf(2);
console.log(index)

//twelveth

let twelvetharray = [1, 12, 3, 2, 4, 2]; 
let lastindex = twelvetharray.lastIndexOf(2);
console.log(lastindex)