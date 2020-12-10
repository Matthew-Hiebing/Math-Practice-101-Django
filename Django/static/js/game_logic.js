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
const inputForm = document.getElementById('inputForm');
const checkButton = document.querySelector('#result_check');
const div = document.getElementById('check_button_alert');

newProblemBtn.addEventListener('click', function () {
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

function checkButtonAlertVisible() {
    if (div.style.visibility = 'hidden') {
        div.style.visibility = 'visible'
    }
};

function checkButtonAlertNotVisible() {
    if (div.style.visibility = 'visible') {
        div.style.visibility = 'hidden'
    }
};

let problem, userInput, correctAnswer, questionStatus;

checkButton.addEventListener('click', function () {
    if (document.querySelector('#user_input').value === "") {
        console.log('No input from user')
        checkButtonAlertVisible()

    } else if (document.querySelector('#correct_answer').getAttribute
        ('value') === document.querySelector('#user_input').value) {
        checkButton.classList.remove('btn-primary','btn-lg','btn-danger');
        checkButton.classList.add('btn-success');
        checkButton.textContent = 'Correct!';
        questionStatus = 'Correct'
        checkButtonAlertNotVisible()

    } else if (document.querySelector('#correct_answer').getAttribute
        ('value') !== document.querySelector('#user_input').value) {
        checkButton.classList.remove('btn-primary','btn-lg');
        checkButton.classList.add('btn-danger');
        checkButton.textContent = 'Incorrect';
        questionStatus = 'Incorrect'
        checkButtonAlertNotVisible()
    }

    problem = document.querySelector('p#math_problem').innerText
    userInput = document.querySelector('input#user_input').value
    correctAnswer = document.querySelector('input#correct_answer').value

    if (userInput == "") {
        console.log("No input entered, request not sent.")
        // Display an alert with class danger
    } else {
        let payload = {
            "csrfmiddlewaretoken": my_token,
            "math_problem": problem,
            "user_answer": userInput,
            "true_answer": correctAnswer,
            "question_status": questionStatus,
        }
        console.log(payload);
        axios.post('../api/scoring/submit_score_details', payload)
    }
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

