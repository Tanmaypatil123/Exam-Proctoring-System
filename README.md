# Ctrl-Alt-Defeat

# setup info

create virtual environment😁.
```bash
python -m venv venv
```

then install all the dependencies 😅.

```bash
pip install -r requirements.txt
```
# Steps to run Django.

```bash
cd app/
python manage.py runserver
```
Now you can interact with server 😀.

# Tech Stack
**Client** : HTML, CSS, JS, PYQT5
**Server** : Django, Python, Pytorch, 

Features:
- Remote monitoring via webcam and screen sharing to ensure exam integrity.
- Facial recognition for biometric identity verification, preventing impersonation.
- Intergrated AI models that analyze behavior in real-time to detect potential cheating
- Enhanced security by restricting unauthorized resource access by adding a facial biometric verification at the admin side as well.
- We have successfully built an intuitive interface and robust backend infrastructure. computer vision model include customized YOLO network, to detect Phones and Person within the camera frame.

```Simulation:```

# Register Page
![image](https://github.com/anurag12-webster/Ctrl-Alt-Defeat/assets/75563673/9e168567-6b37-494d-b457-3e060ce5b713)

The Admin panel is web based, and it is connected with a remotely hosted Django Server.

# Login Page
![image](https://github.com/anurag12-webster/Ctrl-Alt-Defeat/assets/75563673/8505ca24-9668-4502-88ec-345587f88872)

# Facial verification prompt
When the institution has been registered they can log into their, account here comes the facial verification.
![Screenshot (461)](https://github.com/anurag12-webster/Ctrl-Alt-Defeat/assets/75563673/543d0598-c154-4fb8-b73a-a5d6d48bb763)
![Screenshot (462)](https://github.com/anurag12-webster/Ctrl-Alt-Defeat/assets/75563673/e066b6d3-d0db-4134-87ae-5c402741145e)

This ensures that, the person who is at the admin side is the verified one, and no other person can make changes to the details of the exam and etcetera.

# Admin Dashboard
After login we'll be prompted to the Admin Dashboard.
![Dashboard Admin](https://github.com/anurag12-webster/Ctrl-Alt-Defeat/assets/75563673/d5862226-fe39-4d88-9b6e-53429171641c)

Within the Dashboard we can check the exams created, upload the students data to the server to send emails to them for at the time of exam.

# Email notification 
Data section takes in the csv or excel file and extracts the emails in bulk.
Email will be sent to the students on their registered emailID's.
as below:
![image](https://github.com/anurag12-webster/Ctrl-Alt-Defeat/assets/75563673/d0eccb3b-3eee-476e-8948-f4e023a5a0bb)

after receiving the credentials students can start their usual exam, they'll login with a application we built and there student will have to verify their face, and credentials.
# cheating Scene recognition
this desktop application also ensure to check for mobile phones and people in the camera frame.
![cheating prevention](https://github.com/anurag12-webster/Ctrl-Alt-Defeat/assets/75563673/52b6d91b-fda1-449a-a523-3c315b2ec071)

We've used the 

YOLOV8 Model to speed up the process of identofying the mobile phone and the background.

More details about yolo you can find here:
https://docs.ultralytics.com/


we created a binary classification model to categorize the phone and the background.
We used confusion metric as our performance metric where object detection is considered as binary classification task whether is model is able to detect and mark object clearly.

# Confusion Metrix
![image](https://github.com/anurag12-webster/Ctrl-Alt-Defeat/assets/75563673/1dd7b721-9d98-447e-a45f-c7077bc3afc1)



| Measure | Value |
| ------- | ----- |
| Sensitivity | 0.8300 |
| specificity | 0.5000 |
| Precision | 0.4536 |
| Negative Predicted Value | 0.8547 |
| False Positive Rate | 0.5000 |
| False Discovery Rate | 0.5464 |
| False Negative Rate | 0.1700 |



 
# Dataset Details we've used for model training
| Training Samples | Testing Samples | Classes |
| ---------------- | --------------- | ------- |
|  1293| 350 | Mobile Phone, Background|

# Task 
The primary objective of this dataset is to enable the training and testing of object detection models specifically designed for recognizing mobile phones within images. The dataset encompasses scenarios where mobile phones may appear against various backgrounds.

# Annotations
Each sample in the dataset is annotated with bounding boxes indicating the precise location of mobile phones within the images. This facilitates the training of models to accurately detect and delineate mobile phones from their surroundings.
below are the sample images of dataset.
![WhatsApp Image 2024-01-30 at 14 46 30_90f468eb](https://github.com/anurag12-webster/Ctrl-Alt-Defeat/assets/75563673/e413b1f9-d937-4107-b994-c710176c8bc1)


