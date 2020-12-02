const btn = document.querySelector('#TESTID');

btn.addEventListener('click', function(addition) {
    let num1 = Math.floor(Math.random() * 13);
    let num2 = Math.floor(Math.random() * 13);
    let problemResult = num1 + num2;
    // let problem = (num1,'+',num2,'=')
    console.log(num1,'+',num2,'=',problemResult)
    document.getElementById('num1').textContent = (num1, '+', num2, '=', problemResult)
})

