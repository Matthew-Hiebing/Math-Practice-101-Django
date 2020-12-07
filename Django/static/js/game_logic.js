// const axios = require('axios').default;
const newProblemBtn = document.querySelector('#start');
const checkBox = document.querySelector('#splash_screen_preference_check_box');


if (checkBox) {
    checkBox.addEventListener('change', function () {
        console.log(checkBox.checked)
        axios.post('../api/user_preferences/set_preference', {
            "splash_screen_name": "Math",
            "display_on_refresh": !this.checked
        });
    });
}

const randomFunc = [
    multiplication,
    division,
    addition,
    subtraction,
]


let mathProblem = document.querySelector('#math_problem').innerText

newProblemBtn.addEventListener('click', () => {
    let result = randomFunc[Math.floor(Math.random() * randomFunc.length)]();
    document.querySelector('#correct_answer').setAttribute('value', result);
    if (document.querySelector('#result_check').textContent = 'Correct!') {
        document.querySelector('#result_check').classList.remove('btn-success');
        document.querySelector('#result_check').classList.add('btn');
        document.querySelector('#result_check').classList.add('btn-primary');
        document.querySelector('#result_check').classList.add('btn-lg');
        document.querySelector('#result_check').textContent = 'Check';
        document.getElementById('answerForm').reset()
    }
    if (document.querySelector('#result_check').textContent = 'Incorrect') {
        document.querySelector('#result_check').classList.remove('btn-danger');
        document.querySelector('#result_check').classList.add('btn');
        document.querySelector('#result_check').classList.add('btn-primary');
        document.querySelector('#result_check').classList.add('btn-lg');
        document.querySelector('#result_check').textContent = 'Check';
        document.getElementById('answerForm').reset()
    }
});

document.querySelector('#result_check').addEventListener('click', () => {
    const Button = document.querySelector('#result_check');
    if (document.querySelector('#correct_answer').getAttribute('value') === document.querySelector('#user_input').value) {
        Button.classList.remove('btn-primary');
        Button.classList.remove('btn-lg');
        Button.classList.add('btn-success');
        Button.textContent = 'Correct!';
    } else {
        Button.classList.remove('btn-primary');
        Button.classList.remove('btn-lg');
        Button.classList.add('btn-danger');
        Button.textContent = 'Incorrect';
    }
    // This is where axios request happens
});


function multiplication() {
    let num1 = Math.floor(Math.random() * 13);
    let num2 = Math.floor(Math.random() * 13);
    let problemResult = num1 * num2;
    console.log(num1, '*', num2, '=', problemResult);
    document.getElementById('math_problem').innerHTML =
    (`${num1} x ${num2}`);
    return problemResult
}


function division() {
    let num1 = Math.floor(Math.random() * 13);
    let num2 = Math.floor(Math.random() * 12) + 1;
    let problemResult = (num1 * num2) / num2;
    console.log(num1 * num2, '/', num2, '=', problemResult);
    document.getElementById('math_problem').innerHTML =
    (`${num1 * num2} ÷ ${num2}`);
    return problemResult
}


function addition() {
    let num1 = Math.floor(Math.random() * 13);
    let num2 = Math.floor(Math.random() * 13);
    let problemResult = num1 + num2;
    console.log(num1,'+',num2,'=',problemResult);
    document.getElementById('math_problem').innerHTML =
    (`${num1} + ${num2}`);
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
    document.getElementById('math_problem').innerHTML =
    (`${numList[1]} - ${numList[0]}`);
    return problemResult
}

