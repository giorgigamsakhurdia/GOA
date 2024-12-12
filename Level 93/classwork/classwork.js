const Count =  document.getElementById("text")
const incButton = document.getElementById("inc")

incButton.addEventListener("click", () => {
    let currentCount = parseInt(countInput.value, 10); 
    Count.value = currentCount + 1;
})
