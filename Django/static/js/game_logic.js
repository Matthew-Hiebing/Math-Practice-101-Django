const btn = document.querySelector('#start')

const randomFunc = [
    multiplication,
    // division,
    // addition,
    // subtraction,
]

btn.addEventListener('click', () => {
    let result = randomFunc[Math.floor(Math.random() * randomFunc.length)]();
    document.querySelector('#user_input').addEventListener('input', evt => {
        if (result.toString() === evt.target.value) {
            document.getElementById('c_or_i').innerText = ('Correct!')
        } else {
            document.getElementById('c_or_i').innerText = ('Incorrect')
        }
    });
})

function multiplication() {
    let num1 = Math.floor(Math.random() * 13);
    let num2 = Math.floor(Math.random() * 13);
    let problemResult = num1 * num2;
    console.log(num1, '*', num2, '=', problemResult);
    document.getElementById('mathProblem').innerHTML =
    (`${num1} * ${num2} =`);
    return problemResult
}

function division() {
    let num1 = Math.floor(Math.random() * 13);
    let num2 = Math.floor(Math.random() * 12) + 1;
    let problemResult = (num1 * num2) / num2;
    console.log(num1 * num2, '/', num2, '=', problemResult);
    document.getElementById('mathProblem').innerHTML =
    (`${num1 * num2} / ${num2} =`);
    return problemResult
}

function addition() {
    let num1 = Math.floor(Math.random() * 13);
    let num2 = Math.floor(Math.random() * 13);
    let problemResult = num1 + num2;
    console.log(num1,'+',num2,'=',problemResult);
    document.getElementById('mathProblem').innerHTML =
    (`${num1} + ${num2} =`);
    return problemResult
}

function subtraction() {
    let num1 = Math.floor(Math.random() * 13);
    let num2 = Math.floor(Math.random() * 13);
    let numList = [num1, num2];
    numList.sort(function (a, b) {
        return a - b
    });
    let problemResult = numList[1] - numList[0];
    console.log(numList[1], '-', numList[0], '=', problemResult);
    document.getElementById('mathProblem').innerHTML =
    (`${numList[1]} - ${numList[0]} =`);
    return problemResult
}

