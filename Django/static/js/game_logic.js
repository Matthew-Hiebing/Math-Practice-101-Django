//-------------------------------Variables-----------------------------------//
const randomFunc = [multiplication, division, addition, subtraction,]
const checkBox = document.querySelector('#splash_screen_preference_check_box');
const newProblemBtn = document.querySelector('#new_problem_button');
const input_form = document.getElementById('input_form');
const checkButton = document.querySelector('#result_check');
const noAnswerAlert = document.getElementById('no_answer_check_button_alert');
const nonIntegerAlert = document.getElementById('non_integer_check_button_alert');
let problem, userInput, correctAnswer, questionStatus;


//------------------------------Event Listeners------------------------------//
if (checkBox) {
    checkBox.addEventListener('change', function () {
        console.log(checkBox.checked)
        axios.post('../api/user_preferences/set_preference', {
            "splash_screen_name": "Math",
            "display_on_refresh": !this.checked
        });
    });
}


checkButton.addEventListener('click', function () {
    problem = document.querySelector('#math_problem').innerText
    userInput = document.querySelector('#user_input').value
    correctAnswer = document.querySelector('#correct_answer').value
    console.log(`User input is: ${userInput}`)
    console.log(`The correct answer is: ${correctAnswer}`)

    if (isNaN(userInput)) {
        nonIntegerPrompt()

    } else if (userInput === "") {
        noAnswerPrompt();

    } else if (userInput === correctAnswer) {
        correctAnswerPrompt();
        sendMathResults();

    } else if (userInput !== correctAnswer) {
        incorrectAnswerPrompt();
        sendMathResults();
    }
});


//---------------------------New Problem Actions-----------------------------//
newProblemBtn.addEventListener('click', function () {
    newProblemPrompt()
});


//---------------------------------Functions---------------------------------//
function newProblemPrompt() {
    newProblemBtn.disabled = true;
    checkButton.disabled = false;
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
}


function sendMathResults() {
    axios.defaults.xsrfCookieName = 'csrftoken';
    axios.defaults.xsrfHeaderName = 'X-CSRFToken';
    axios.post('../api/scoring/submit_score_details', {
        "math_problem": problem,
        "user_answer": userInput,
        "true_answer": correctAnswer,
        "question_status": questionStatus,
    });
    console.log(`Axios sent: ${problem}, User Input: ${userInput},
        Correct Answer: ${correctAnswer}, Question Status: ${questionStatus}`);
}


function noAnswerPrompt() {
    console.log('No input from user, alert shown')
    noAnswerAlert.style.visibility = 'visible'
    noAnswerAlert.style.display = 'block'
}


function nonIntegerPrompt() {
    console.log('Non-integer entered')
    nonIntegerAlert.style.visibility = 'visible'
    noAnswerAlert.style.visibility = 'hidden'
    nonIntegerAlert.style.display = 'block'
}


function incorrectAnswerPrompt() {
    checkButton.classList.remove('btn-primary', 'btn-lg');
    checkButton.classList.add('btn-danger');
    checkButton.textContent = 'Incorrect';
    questionStatus = 'Incorrect'
    noAnswerAlert.style.visibility = 'hidden'
    nonIntegerAlert.style.visibility = 'hidden'
    noAnswerAlert.style.display = 'none'
    nonIntegerAlert.style.display = 'none'
    document.getElementById('new_problem_button').disabled = false;
    document.getElementById('result_check').disabled = true;
}


function correctAnswerPrompt() {
    checkButton.classList.remove('btn-primary', 'btn-lg', 'btn-danger');
    checkButton.classList.add('btn-success');
    checkButton.textContent = 'Correct!';
    questionStatus = 'Correct'
    noAnswerAlert.style.visibility = 'hidden'
    nonIntegerAlert.style.visibility = 'hidden'
    noAnswerAlert.style.display = 'none'
    nonIntegerAlert.style.display = 'none'
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







