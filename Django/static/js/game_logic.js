//----------------------------Splash Screen Check----------------------------//
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


//---------------------------------Constants---------------------------------//
const newProblemBtn = document.querySelector('#new_problem_button');
const inputForm = document.getElementById('inputForm');
const checkButton = document.querySelector('#result_check');
const div = document.getElementById('check_button_alert');

//---------------------------Check Button Actions----------------------------//
let problem, userInput, correctAnswer, questionStatus;
checkButton.addEventListener('click', function () {
    if (document.querySelector('#user_input').value === "") {
        console.log('No input from user, alert shown')
        div.style.visibility = 'visible'

    } else if (document.querySelector('#correct_answer').getAttribute
    ('value') === document.querySelector('#user_input').value) {
        checkButton.classList.remove('btn-primary','btn-lg','btn-danger');
        checkButton.classList.add('btn-success');
        checkButton.textContent = 'Correct!';
        questionStatus = 'Correct'
        div.style.visibility = 'hidden'
        document.getElementById('new_problem_button').disabled = false;

    } else if (document.querySelector('#correct_answer').getAttribute
    ('value') !== document.querySelector('#user_input').value) {
        checkButton.classList.remove('btn-primary','btn-lg');
        checkButton.classList.add('btn-danger');
        checkButton.textContent = 'Incorrect';
        questionStatus = 'Incorrect'
        div.style.visibility = 'hidden'
        document.getElementById('new_problem_button').disabled = false;
    }

    problem = document.querySelector('p#math_problem').innerText
    userInput = document.querySelector('input#user_input').value
    correctAnswer = document.querySelector('input#correct_answer').value

    if (userInput == "") {
        console.log("No input entered, POST not sent.")
    } else {
        axios.defaults.xsrfCookieName = 'csrftoken';
        axios.defaults.xsrfHeaderName = 'X-CSRFToken';
        axios.post('../api/scoring/submit_score_details', {
            "math_problem": problem,
            "user_answer": userInput,
            "true_answer": correctAnswer,
            "question_status": questionStatus,
        });
        console.log(`Problem:${problem}, User Input: ${userInput},
        Correct Answer: ${correctAnswer}, Question Status: ${questionStatus}`);
    }
});


//--------------------------Random Math Function-----------------------------//
newProblemBtn.addEventListener('click', function () {
    document.getElementById('new_problem_button').disabled = true;
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

