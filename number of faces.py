#number of faces detected 
import cv2

# Load pre-trained face classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize the camera
cap = cv2.VideoCapture(0)  # Use 0 for default camera, change to the appropriate camera index if needed

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform face detection
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    # Display appropriate message based on the number of persons detected
    num_persons = len(faces)
    if num_persons == 0:
        cv2.putText(frame, 'Please come in the camera frame', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    else:
        cv2.putText(frame, f'Persons Detected: {num_persons}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display the resulting frame
    cv2.imshow('Face Detection', frame)

    # Break the loop if 'q' key is pressed or if the camera window is closed
    if cv2.waitKey(1) & 0xFF == ord('q') or not ret:
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
