// const axios = require('axios').default;
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


const newProblemBtn = document.querySelector('#start');
const mathProblem = document.querySelector('#math_problem').innerText
const inputForm = document.getElementById('inputForm');
const checkButton = document.querySelector('#result_check');

newProblemBtn.addEventListener('click', () => {
    let result = randomFunc[Math.floor(Math.random() * randomFunc.length)]();
    document.querySelector('#correct_answer').setAttribute('value', result);
    if (checkButton.textContent = 'Correct!') {
        checkButton.classList.remove('btn-success');
        checkButton.classList.add('btn', 'btn-primary', 'btn-lg');
        checkButton.textContent = 'Check';
        inputForm.reset()
    }
    if (checkButton.textContent = 'Incorrect') {
        checkButton.classList.remove('btn-danger');
        checkButton.classList.add('btn', 'btn-primary', 'btn-lg');
        checkButton.textContent = 'Check';
        inputForm.reset()
    }
});

const randomFunc = [
    multiplication,
    division,
    addition,
    subtraction,
]

checkButton.addEventListener('click', () => {
    if (document.querySelector('#correct_answer').getAttribute('value') === document.querySelector('#user_input').value) {
        checkButton.classList.remove('btn-primary','btn-lg','btn-danger');
        checkButton.classList.add('btn-success');
        checkButton.textContent = 'Correct!';
    } else {
        checkButton.classList.remove('btn-primary','btn-lg');
        checkButton.classList.add('btn-danger');
        checkButton.textContent = 'Incorrect';
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

