let quizData = [];
let currentQuestionIndex = 0;
let questionsAdded = false;

function addQAndA() {
    addQuestion("Q & A");
}

function addCodingQ() {
    addQuestion("Coding Q");
}

function addQuestion(questionType) {
    const quizCards = document.getElementById('quiz-cards');
    const questionCard = document.createElement('div');
    questionCard.classList.add('quiz-card');

    const questionContainer = document.createElement('div');
    questionContainer.classList.add('question-input');

    const questionLabel = document.createElement('label');
    questionLabel.textContent = `Question No ${currentQuestionIndex + 1} (${questionType}):`;
    questionContainer.appendChild(questionLabel);

    const questionInput = document.createElement('input');
    questionInput.type = 'text';
    questionInput.placeholder = 'Enter your question...';
    questionInput.required = true;
    questionContainer.appendChild(questionInput);

    if (questionType === "Q & A") {
        const optionsContainer = document.createElement('div');
        optionsContainer.classList.add('options-container');

        for (let j = 0; j < 4; j++) {
            const optionInput = document.createElement('input');
            optionInput.type = 'text';
            optionInput.placeholder = `Option ${String.fromCharCode(97 + j)}`;
            optionInput.classList.add('option-input');
            optionsContainer.appendChild(optionInput);
        }

        const correctAnswerInput = document.createElement('select');
        correctAnswerInput.classList.add('option-input');
        for (let j = 0; j < 4; j++) {
            const option = document.createElement('option');
            option.value = String.fromCharCode(97 + j);
            option.text = `Option ${String.fromCharCode(97 + j)}`;
            correctAnswerInput.add(option);
        }
        optionsContainer.appendChild(correctAnswerInput);

        const pointsInput = document.createElement('input');
        pointsInput.type = 'number';
        pointsInput.placeholder = 'Enter points for the question...';
        pointsInput.required = true;
        optionsContainer.appendChild(pointsInput);

        questionContainer.appendChild(optionsContainer);
    } else if (questionType === "Coding Q") {
        const codingLanguageInput = document.createElement('select');
        codingLanguageInput.id = 'coding-language-input';
        codingLanguageInput.type = 'select';
        codingLanguageInput.placeholder = 'Select coding language...';
        codingLanguageInput.required = true;

        const languages = ['Python', 'C++', 'JavaScript'];
        for (const language of languages) {
            const option = document.createElement('option');
            option.value = language.toLowerCase();
            option.text = language;
            codingLanguageInput.add(option);
        }

        questionContainer.appendChild(codingLanguageInput);
    }

    questionCard.appendChild(questionContainer);
    quizCards.appendChild(questionCard);

    showQuestion(currentQuestionIndex);
    currentQuestionIndex;
    questionsAdded = true; // Set to true to prevent additional card generation
}

function showQuestion(index) {
    const quizCards = document.getElementById('quiz-cards');
    const cards = quizCards.getElementsByClassName('quiz-card');

    if (index >= 0 && index < cards.length) {
        for (let i = 0; i < cards.length; i++) {
            cards[i].style.transform = i === index ? 'translateX(0)' : 'translateX(0px)';
        }
    }

    currentQuestionIndex = index;
}

function publishExam() {
    const quizCards = document.getElementById('quiz-cards');
    const jsonOutput = document.getElementById('json-output');

    const cards = quizCards.getElementsByClassName('quiz-card');
    quizData = [];

    for (let i = 0; i < cards.length; i++) {
        const card = cards[i];
        const questionInput = card.querySelector('input[type="text"]');
        const optionsInputs = card.querySelectorAll('input[type="text"]');
        const correctAnswerInput = card.querySelector('select');
        const pointsInput = card.querySelector('input[type="number"]');
        const codingLanguageInput = card.querySelector('#coding-language-input');

        const questionData = {
            id: i,
            question: questionInput.value,
            options: {},
            answer: correctAnswerInput ? correctAnswerInput.value : undefined
        };

        optionsInputs.forEach((input, index) => {
            // Iterate over all four options
            if ( index>0 && index <= 4) {
                questionData.options[String.fromCharCode(97 + index)] = input.value;
            }
        });

        // Check for correctAnswerInput outside the loop
        if (correctAnswerInput) {
            questionData.answer = correctAnswerInput.value;
        }

        if (codingLanguageInput) {
            questionData.codingLanguage = codingLanguageInput.value;
        }

        questionData.points = pointsInput ? pointsInput.value : undefined;

        quizData.push(questionData);
    }

    jsonOutput.textContent = JSON.stringify(quizData, null, 2);
}