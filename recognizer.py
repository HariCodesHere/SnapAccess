import cv2
import os
import numpy as np
import json

FACES_DIR = "data/faces"
USERS_JSON = "data/users.json"
MODEL_PATH = "data/trained_model.yml"

def train_model():
    """Train the LBPH recognizer with saved face images."""
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    faces = []
    labels = []

    with open(USERS_JSON, "r") as f:
        users = json.load(f)
    
    for filename in os.listdir(FACES_DIR):
        if filename.endswith(".jpg"):
            label = int(filename.split("_")[1])
            img_path = os.path.join(FACES_DIR, filename)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            faces.append(img)
            labels.append(label)

    recognizer.train(faces, np.array(labels))
    recognizer.save(MODEL_PATH)
    print("[INFO] Model trained and saved.")

def load_model():
    """Load and return the trained model."""
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read(MODEL_PATH)
    return recognizer
