const btn = document.querySelector('#TESTID');

btn.onclick = function(addition) {
    let num1 = Math.floor(Math.random() * 13);
    let num2 = Math.floor(Math.random() * 13);
    let problemResult = num1 + num2;
    console.log(problemResult);
}
