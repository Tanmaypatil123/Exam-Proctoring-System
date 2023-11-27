function openSection(sectionId) {
    var sections = document.getElementsByClassName("section");
    for (var i = 0; i < sections.length; i++) {
        sections[i].style.display = "none";
    }
    document.getElementById(sectionId).style.display = "block";
}

function parseData() {
    var fileInput = document.getElementById('fileInput');
    var preview = document.getElementById('preview');

    var file = fileInput.files[0];

    if (file) {
        const reader = new FileReader();

        reader.onload = function (e) {
            var content = e.target.result;
            // display the content of the file uploaded as preview.

            preview.innerHTML = "<h3>Preview:</h3>" + content.slice(0, 500);
        };

        reader.readAsText(file);
    }
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

