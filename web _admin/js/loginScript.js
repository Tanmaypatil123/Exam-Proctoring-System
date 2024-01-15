function captureAndVerifyFace() {
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({ video: { facingMode: 'user' } })
        .then(function (stream) {
            var video = document.createElement('video');
            video.srcObject = stream;
            document.body.appendChild(video);
            LoginOrganisation();
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


function LoginOrganisation(){
    const email = document.getElementById("orgEmail").value;
    const password = document.getElementById("orgPassword").value;

    const data = {
        email : email,
        password : password
    };

    fetch("http://127.0.0.1:8000/api/login/", {
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
        console.log("login successful:", data);
        localStorage.setItem("token",data['token']["access"])
        console.log(localStorage.getItem("token"))
    })
    .catch(error => {
        console.error("login failed:", error);
    });

}

function verifyFace() {
    setTimeout(function() {
        window.location.href = "dashboard.html";
    }, 3000);
}


