function showRegistrationAlert() {
    var alertBox = document.createElement('div');
    alertBox.setAttribute('id', 'registrationAlert');
    alertBox.textContent = 'You\'re registered!';
    document.body.appendChild(alertBox);

    setTimeout(function() {
        document.getElementById('registrationAlert').style.opacity = '0';
        setTimeout(function() {
            document.body.removeChild(alertBox);
            redirectToLoginPage();
        }, 500);
    }, 3000);
}

function redirectToLoginPage() {
    setTimeout(function () {
        window.location.href = "login.html"; 
    }, 5000);
}

function isPasswordValid(password) {
    const passwordRegex = /^(?=.*[0-9].*[0-9].*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{6,}$/;
    return passwordRegex.test(password);
}

function registerOrganization() {
            
    const orgName = document.getElementById("orgName").value;
    const orgEmail = document.getElementById("orgEmail").value;
    const orgPassword = document.getElementById("orgPassword").value;

    
    const data = {
        name: orgName,
        email: orgEmail,
        password: orgPassword,
        password2: orgPassword,  
        tc: "True"
    };

    // Make POST request
    fetch("http://127.0.0.1:8000/api/register/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json;",
            // "charset=UTF-8"
            // "Access-Control-Allow-Origin": "*",
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        console.log("Registration successful:", data);
        showRegistrationAlert();
    })
    .catch(error => {
        console.error("Registration failed:", error);
    });
}

function capturePhoto() {
    const password = document.getElementById('orgPassword').value;
    if (isPasswordValid(password)) {
        registerOrganization();
        if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
            navigator.mediaDevices.getUserMedia({ video: { facingMode: 'environment' } })
            .then(function (stream) {
                var video = document.createElement('video');
                video.srcObject = stream;
                document.body.appendChild(video);
                showRegistrationAlert();
            })
            .catch(function (error) {
                console.error("Error accessing the camera: ", error);
            });
        } else {
            console.error("getUserMedia not supported");
        }
    } else {
        alert('Password must be at least 6 characters long, contain at least 3 digits, and one symbol.');
    }
}
document.getElementById('registerButton').addEventListener('click', function () {
    capturePhoto();
});


function closeBanner() {
    var banner = document.getElementById('banner');
    banner.style.display = 'none';
}

function togglePassword() {
    var passwordInput = document.getElementById('orgPassword');
    var toggleIcon = document.getElementById('togglePassword');
    if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
        toggleIcon.textContent = 'Hide';
    } else {
        passwordInput.type = 'password';
        toggleIcon.textContent = 'Show';
    }
}


// add database connectivity here 
// function Database(){
    
    // add your code here for storing, the images in database

// }