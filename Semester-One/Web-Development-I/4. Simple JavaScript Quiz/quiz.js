// Prabhat Bhatia
// B.Tech CSE Cyber Security Semester 1
// Lab Assignment 4

const quizQuestions = [
    { question: "What is the capital of India?", answer: "new delhi" },
    { question: "What does HTML stand for?", answer: "hypertext markup language" },
    { question: "What is the largest planet in our solar system?", answer: "jupiter" },
    { question: "Who developed JavaScript?", answer: "brendan eich" },
    { question: "Who is the President Of Russia?", answer: "vladimir putin" }
];

function runQuiz() {
    let score = 0;
    alert("Welcome to Assignment 4 Quiz by Prabhat Bhatia!");
    for (let i = 0; i < quizQuestions.length; i++) {
        const user = prompt(`Q${i + 1}: ${quizQuestions[i].question}`);
        const userAns = user ? user.toLowerCase().trim() : "";
        const correctAns = quizQuestions[i].answer.toLowerCase().trim();

        if (userAns === correctAns) {
            alert("Correct answer");
            score++;
        } else {
            alert(`Incorrect answer\nCorrect answer is: ${quizQuestions[i].answer}`);
        }
    }
    alert(`Quiz Completed!\nYour Score: ${score} / ${quizQuestions.length}`);
}

runQuiz();