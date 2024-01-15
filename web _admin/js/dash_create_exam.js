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
        codingLanguageInput.type = 'input';
        codingLanguageInput.placeholder = 'Select coding language...';
        codingLanguageInput.required = true;

        const languages = ['Python', 'C++', 'JavaScript', 'Rust'];
        for (const language of languages) {
            const option = document.createElement('option');
            option.value = language.toLowerCase();
            option.text = language;
            codingLanguageInput.add(option);
        }

        // Add input for coding question
        const inputTextLabel = document.createElement('label');
        inputTextLabel.textContent = 'Input Text:';
        const inputText = document.createElement('input');
        inputText.type = 'text';
        inputText.placeholder = 'Enter input text...';
        inputText.required = true;

        // Add output for coding question
        const outputTextLabel = document.createElement('label');
        outputTextLabel.textContent = 'Output Text:';
        const outputText = document.createElement('input');
        outputText.type = 'text';
        outputText.placeholder = 'Enter expected output text...';
        outputText.required = true;

        questionContainer.appendChild(codingLanguageInput);
        questionContainer.appendChild(inputTextLabel);
        questionContainer.appendChild(inputText);
        questionContainer.appendChild(outputTextLabel);
        questionContainer.appendChild(outputText);
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
    const exam_name = document.getElementById("examName").value;
    const duration = 60
    const max_no_limit = 15
    const description = exam_name
    const no_of_question = document.getElementById("no-of-questions").value;


    const exam_creation_data = {
        name : exam_name,
        description : description,
        no_of_questions : no_of_question,
        max_warning_limit : max_no_limit,
        duration : duration,
    }
    console.log(exam_creation_data)


    fetch("http://127.0.0.1:8000/api/exam/create-exam/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json;",
            "Authorization" : `Bearer ${localStorage.getItem("token")}`,
            "Accept" : "application/json"
        },
        body: JSON.stringify(exam_creation_data),
    })
    .then(response => response.json())
    .then(data => {
        console.log("exam creation successful:", data);
        localStorage.setItem("exam_id" , data["exam"])
        alert(`Your exam id is ${data["exam"]}`)
    })
    .catch(error => {
        console.error("Exam creation failed:", error);
    });

    for (let i = 0; i < cards.length; i++) {
        const card = cards[i];
        const questionInput = card.querySelector('input[type="text"]');
        const optionsInputs = card.querySelectorAll('input[type="text"]');
        const correctAnswerInput = card.querySelector('select');
        const pointsInput = card.querySelector('input[type="number"]');
        const codingLanguageInput = card.querySelector('#coding-language-input');
        
        console.log(questionInput.value);
        console.log(localStorage.getItem("exam_id"))

        const question_data_new = {
            exam_id : localStorage.getItem("exam_id"),
            question : questionInput.value
        }
        const questionData = {
            id: i,
            question: questionInput.value,
            options: {},
            answer: correctAnswerInput ? correctAnswerInput.value : undefined
        };

        // fetch("http://127.0.0.1:8000/api/exam/question/", {
        // method: "POST",
        // headers: {
        //     "Content-Type": "application/json;",
        //     "Authorization" : `Bearer ${localStorage.getItem("token")}`,
        //     "Accept" : "application/json"
        // },
        //     body: JSON.stringify(question_data_new),
        // })
        // .then(response => response.json())
        // .then(data => {
        //     console.log("quetion creation successful:", data);
        //     localStorage.setItem("question_id" , data["question_id"])

        //     // alert(`Your exam id is ${data["exam"]}`)
        // })
        // .catch(error => {
        //     console.error("question creation failed:", error);
        // });

        optionsInputs.forEach((input, index) => {
            // Iterate over all four options
            if ( index>0 && index <= 4) {
                console.log(localStorage.getItem("question_id"))

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
    // console.log(quizData);
    quizData.forEach(questionData => {
        console.log(`Question ${questionData.id + 1}: ${questionData.question}`);
        
        // Iterate through options if available
        if (questionData.codingLanguage) {
            console.log(`Coding Language: ${questionData.codingLanguage}`);
            Object.keys(questionData.options).forEach(optionKey => {
                const optionValue = questionData.options[optionKey];
                console.log(`Option ${optionKey}: ${optionValue}`);
            });
            // request 
        }
        else {
            Object.keys(questionData.options).forEach(optionKey => {
                const optionValue = questionData.options[optionKey];
                console.log(`Option ${optionKey}: ${optionValue}`);
            });
        }
    
        // Print other properties
        console.log(`Answer: ${questionData.answer}`);
        console.log(`Points: ${questionData.points}`);
        
        
    
        console.log("--------");
    });
    jsonOutput.textContent = JSON.stringify(quizData, null, 2);
}