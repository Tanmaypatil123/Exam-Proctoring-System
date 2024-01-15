function openSection(sectionId) {
    var sections = document.getElementsByClassName("section");
    for (var i = 0; i < sections.length; i++) {
        sections[i].style.display = "none";
    }
    document.getElementById(sectionId).style.display = "block";
}

function parseData() {
    const email = document.getElementById("email").value;
    const name = document.getElementById("name").value;
    const exam_id = document.getElementById("examId").value;
    data = {
        email : email,
        name : name,
        exam : exam_id
    }
    fetch("http://127.0.0.1:8000/api/student/register/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json;",
            "Authorization" : `Bearer ${localStorage.getItem("token")}`,
            "Accept" : "application/json"
            // "charset=UTF-8"
            // "Access-Control-Allow-Origin": "*",
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        console.log("Registration successful:", data);
        console.log(localStorage.getItem("token"));
    })
    .catch(error => {
        console.error("Registration failed:", error);
    });






}
function saveExamDetails() {
    const examName = document.getElementById("examName").value;
    const examDate = document.getElementById("examDate").value;
    const startTime = document.getElementById("startTime").value;
    const endTime = document.getElementById("endTime").value;

    const today = new Date();
    const selectedDate = new Date(examDate);

    if (examName && examDate && startTime && endTime) {
        if (selectedDate < today) {
            alert("Exam date cannot be in the past.");
            return;
        }

        if (endTime < startTime) {
            alert('End time cannot be less than start time');
            return;
        }
        const examDetails = {
            examName: examName,
            examDate: examDate,
            startTime: startTime,
            endTime: endTime
        };
        console.log(examDetails);
        alert("Exam details saved successfully!");
    } else {
        alert("Please fill in all fields.");
    }
}

