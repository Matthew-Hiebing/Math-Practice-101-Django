const btn = document.querySelector('#START')

const randomFunc = [
    multiplication,
    division,
    addition,
    subtraction,
]

btn.addEventListener(
    'click',
    function () {
        randomFunc[Math.floor(Math.random() * randomFunc.length)]();
    }
)

function multiplication() {
    let num1 = Math.floor(Math.random() * 13);
    let num2 = Math.floor(Math.random() * 13);
    let problemResult = num1 * num2;
    console.log(num1, '*', num2, '=', problemResult);
    document.getElementById('mathProblem').innerHTML =
    (`${num1} * ${num2} =`);
}

function division() {
    let num1 = Math.floor(Math.random() * 13);
    let num2 = Math.floor(Math.random() * 12) + 1;
    let problemResult = (num1 * num2) / num2;
    console.log(num1 * num2, '/', num2, '=', problemResult);
    document.getElementById('mathProblem').innerHTML =
    (`${num1 * num2} / ${num2} =`);
}

function addition() {
    let num1 = Math.floor(Math.random() * 13);
    let num2 = Math.floor(Math.random() * 13);
    let problemResult = num1 + num2;
    console.log(num1,'+',num2,'=',problemResult);
    document.getElementById('mathProblem').innerHTML =
    (`${num1} + ${num2} =`);
}

function subtraction() {
    let num1= Math.floor(Math.random() * 13);
    let num2 = Math.floor(Math.random() * 13);
    let numList = [num1,num2];
    numList.sort(function(a,b){return b-a});
    let problemResult = numList[0] - numList[1];
    console.log(numList[0], '-', numList[1], '=', problemResult);
    document.getElementById('mathProblem').innerHTML =
    (`${numList[0]} - ${numList[1]} =`);
}

