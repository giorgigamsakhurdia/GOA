
//Part 1 createElement - ქმნის ელემენტს html-ში

let div1 = document.createElement("div");


let newP = document.createElement("p");
newP.textContent = "nice";


let button1 = document.createElement("button");
Button1.textContent = "happy";


let list = document.createElement("ul");


let listItem = document.createElement("li");
listItem.textContent = "mhm";

//Part 2 appendChild - ამატებს ელემენტს მშობელ ელემენტში როგორ შვილი(მგონი)


let container = document.getElementById("container");
let paragraph = document.createElement("p");
paragraph.textContent = "Goot.";
container.appendChild(paragraph);


let ul = document.createElement("ul");
let li = document.createElement("li");
li.textContent = "I";
ul.appendChild(li);


let div = document.createElement("div");
let button = document.createElement("button");
button.textContent = "CliCK!!!";
div.appendChild(button);


let header = document.createElement("h1");
header.textContent = "good title";
document.body.appendChild(header);


let orderedList = document.createElement("ol");
let inorderList = document.createElement("li");
inorderList.textContent = "Order";
orderedList.appendChild(inorderList);


//insertBefore კარგად ვერ გავიგე

//Part 3 removeChild  - აშორებს შვილს ელემენტს მშობლიდან


let pRemove = document.getElementById("paragraph");
pRemove.parentNode.removeChild(paragraphToRemove);


let ulToRemoveFrom = document.getElementById("myList");
ulToRemoveFrom.removeChild(ulToRemoveFrom.firstChild);

//მეტი ვერ მოვიფიქრე