import cv2
import os
import json
from datetime import datetime
from recognizer import load_model
from camera import get_camera
from recognizer import train_model
from utils import log_access
import csv

# Paths
DATA_DIR = "data"
FACES_DIR = os.path.join(DATA_DIR, "faces")
USERS_JSON = os.path.join(DATA_DIR, "users.json")
LOG_FILE = "logs.csv"

# Ensure necessary folders exist
os.makedirs(FACES_DIR, exist_ok=True)
if not os.path.exists(USERS_JSON):
    with open(USERS_JSON, "w") as f:
        json.dump({}, f)

def register_face():
    """Capture images for a new user and store them in the dataset."""
    user_name = input("Enter your name: ").strip()
    if not user_name:
        print("Name cannot be empty.")
        return

    # Load or update users.json
    with open(USERS_JSON, "r") as f:
        users = json.load(f)

    new_id = str(len(users) + 1)
    users[new_id] = user_name

    with open(USERS_JSON, "w") as f:
        json.dump(users, f, indent=2)

    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    count = 0

    print("[INFO] Capturing face images. Press 'q' to stop early.")
    while count < 10:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            count += 1
            face_img = gray[y:y+h, x:x+w]
            filename = os.path.join(FACES_DIR, f"user_{new_id}_{count}.jpg")
            cv2.imwrite(filename, face_img)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.imshow("Register Face", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        if count >= 10:
            break

    cap.release()
    cv2.destroyAllWindows()
    print(f"[INFO] {count} face images saved for {user_name}.")

def start_recognition():
    """Run face recognition and log identified users."""
    print("[INFO] Starting face recognition...")

    recognizer = load_model()

    with open(USERS_JSON, "r") as f:
        users = json.load(f)

    cap = get_camera()
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            roi = gray[y:y+h, x:x+w]
            label, confidence = recognizer.predict(roi)

            name = users.get(str(label), "Unknown")

            cv2.putText(frame, f"{name} ({int(confidence)})", (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            log_access(name, confidence)  # <- THIS is now correctly placed

        cv2.imshow("SnapAccess - Recognizer", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("[INFO] Recognition ended.")



def start_recognition():
    """Run face recognition and print identified names."""
    print("[INFO] Starting face recognition...")

    recognizer = load_model()

    with open(USERS_JSON, "r") as f:
        users = json.load(f)

    cap = get_camera()
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            roi = gray[y:y+h, x:x+w]
            label, confidence = recognizer.predict(roi)

            name = users.get(str(label), "Unknown")
            cv2.putText(frame, f"{name} ({int(confidence)})", (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.imshow("SnapAccess - Recognizer", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("[INFO] Recognition ended.")



def train_and_notify():
    print("[INFO] Training model from face data...")
    train_model()
    print("[INFO] Training complete.")

def log_access(name, confidence):
    """Log recognized user to logs.csv with timestamp and confidence."""
    log_path = "logs.csv"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(log_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, name, f"{confidence:.2f}"])