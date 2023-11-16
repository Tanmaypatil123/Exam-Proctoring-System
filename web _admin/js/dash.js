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

