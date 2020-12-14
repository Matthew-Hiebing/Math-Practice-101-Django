var correct_answer_count = document.getElementById("correct_answer_count").value;
var incorrect_answer_count = document.getElementById("incorrect_answer_count").value;
var total_questions_answered = document.getElementById("total_questions_answered").value;

var ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: [
            `Total Correct: ${correct_answer_count}`,
            `Total Incorrect: ${incorrect_answer_count}`,
            `Total Answered: ${total_questions_answered}`],
        datasets: [{
            label: 'Math Results',
            data: [
                correct_answer_count,
                incorrect_answer_count,
                total_questions_answered
            ],
        backgroundColor: [
            'rgba(13, 222, 2, 0.2)',
            'rgba(250, 0, 0, 0.2)',
            'rgba(10, 38, 255, 0.2)',
        ],
        borderColor: [
            'rgba(7, 158, 0, 1)',
            'rgba(225, 0, 0, 1)',
            'rgba(30, 56, 255, 1)',
        ],
            borderWidth: 1.5
        }]
    },
options: {
    scales: {
        yAxes: [{
            ticks: {
                beginAtZero: true
            }
        }]
    }
}
    });
