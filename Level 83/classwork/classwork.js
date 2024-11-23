function calcTip(){
    let a = document.getElementsByName("buy")
    let b = document.getElementsByName(parseInt("tip" - "%"))
    let c = (b / 100 * a)
    console.log(c)
}

