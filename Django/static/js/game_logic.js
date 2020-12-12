//-------------------------------Variables-----------------------------------//
const randomFunc = [multiplication, popUpision, addition, subtraction,]
const checkBox = document.querySelector('#splash_screen_preference_check_box');
const newProblemBtn = document.querySelector('#new_problem_button');
const input_form = document.getElementById('input_form');
const checkButton = document.querySelector('#result_check');
const popUp = document.getElementById('check_button_alert');
let problem, userInput, correctAnswer, questionStatus;


//-------------------Splash Screen Check & Axios Request---------------------//
if (checkBox) {
    checkBox.addEventListener('change', function () {
        console.log(checkBox.checked)
        axios.post('../api/user_preferences/set_preference', {
            "splash_screen_name": "Math",
            "display_on_refresh": !this.checked
        });
    });
}


//---------------------------Check Button Actions----------------------------//
checkButton.addEventListener('click', function () {
    problem = document.querySelector('#math_problem').innerText
    userInput = document.querySelector('#user_input').value
    correctAnswer = document.querySelector('#correct_answer').value

    if (document.querySelector('#user_input').value === "") {
        noAnswerPrompt();

    } else if (document.querySelector('#correct_answer').getAttribute
    ('value') === document.querySelector('#user_input').value) {
        correctAnswerPrompt();
        sendMathResults();

    } else if (document.querySelector('#correct_answer').getAttribute
    ('value') !== document.querySelector('#user_input').value) {
        incorrectAnswerPrompt();
        sendMathResults();
    }
});


//---------------------------------Functions---------------------------------//
function sendMathResults() {
    axios.defaults.xsrfCookieName = 'csrftoken';
    axios.defaults.xsrfHeaderName = 'X-CSRFToken';
    axios.post('../api/scoring/submit_score_details', {
        "math_problem": problem,
        "user_answer": userInput,
        "true_answer": correctAnswer,
        "question_status": questionStatus,
    });
    console.log(`Problem: ${problem}, User Input: ${userInput},
        Correct Answer: ${correctAnswer}, Question Status: ${questionStatus}`);
}


function noAnswerPrompt() {
    console.log('No input from user, alert shown')
    popUp.style.visibility = 'visible'
}


function incorrectAnswerPrompt() {
    checkButton.classList.remove('btn-primary', 'btn-lg');
    checkButton.classList.add('btn-danger');
    checkButton.textContent = 'Incorrect';
    questionStatus = 'Incorrect'
    popUp.style.visibility = 'hidden'
    document.getElementById('new_problem_button').disabled = false;
    document.getElementById('result_check').disabled = true;
}


function correctAnswerPrompt() {
    checkButton.classList.remove('btn-primary', 'btn-lg', 'btn-danger');
    checkButton.classList.add('btn-success');
    checkButton.textContent = 'Correct!';
    questionStatus = 'Correct'
    popUp.style.visibility = 'hidden'
    document.getElementById('new_problem_button').disabled = false;
    document.getElementById('result_check').disabled = true;
}


function multiplication() {
    let num1 = Math.floor(Math.random() * 13);
    let num2 = Math.floor(Math.random() * 13);
    let problemResult = num1 * num2;
    console.log(num1, '*', num2, '=', problemResult);
    document.getElementById('math_problem').innerHTML =
        (`${num1} x ${num2}`);
    return problemResult
}


function popUpision() {
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
    console.log(num1, '+', num2, '=', problemResult);
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


//--------------------------Random Math Function-----------------------------//
newProblemBtn.addEventListener('click', function () {
    document.getElementById('new_problem_button').disabled = true;
    document.getElementById('result_check').disabled = false;
    let result = randomFunc[Math.floor(Math.random() * randomFunc.length)]();
    document.querySelector('#correct_answer').setAttribute('value', result);
    if (checkButton.textContent = 'Correct!') {
        checkButton.classList.remove('btn-success');
        checkButton.classList.add('btn', 'btn-primary', 'btn-lg');
        checkButton.textContent = 'Check';
        input_form.reset();
    }
    if (checkButton.textContent = 'Incorrect') {
        checkButton.classList.remove('btn-danger');
        checkButton.classList.add('btn', 'btn-primary', 'btn-lg');
        checkButton.textContent = 'Check';
        input_form.reset();
    }
});





