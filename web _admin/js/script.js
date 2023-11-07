function capturePhoto() {
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
}

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
