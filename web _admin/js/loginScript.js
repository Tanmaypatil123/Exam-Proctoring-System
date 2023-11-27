function captureAndVerifyFace() {
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({ video: { facingMode: 'user' } })
        .then(function (stream) {
            var video = document.createElement('video');
            video.srcObject = stream;
            document.body.appendChild(video);
            verifyFace();
        })
        .catch(function (error) {
            console.error("Error accessing the camera: ", error);
        });
    } else {
        console.error("getUserMedia not supported");
    }
}

// function Database(){
    
    // code here for DB 

// }

function verifyFace() {
    setTimeout(function() {
        window.location.href = "dashboard.html";
    }, 3000);
}