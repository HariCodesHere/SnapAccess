# 🧠 SnapAccess

**SnapAccess** is a standalone facial recognition GUI tool built in Python. It performs real-time face detection and authentication using your system's camera. Designed as a reusable software module, SnapAccess will later integrate into the hardware-based **FaceLockR** system — but functions fully independently without any hardware.

---

## 🚀 Features

- 🔍 Real-time face detection using OpenCV
- 📸 Support for any connected camera (defaults to laptop webcam)
- 🧑‍💼 Face registration and profile management
- 🔐 Recognition-based access decision (for future extension)
- 📁 Modular codebase for integration into other systems

---

## 🧰 Tech Stack

- Python 3
- OpenCV (`cv2`)
- Tkinter or PyQt (GUI)
- NumPy, OS, JSON

---

## 🖥️ GUI Preview

Coming soon!

---

## 🗂️ Project Structure

```
snapaccess/
├── main.py              # App entry point (GUI + logic)
├── camera_manager.py    # Handles camera feed (easily switchable)
├── recognizer.py        # Face recognition logic (train, match)
├── register.py          # Register new users with captured photos
├── database/
│   ├── faces/           # Stored user face images
│   └── users.json       # Metadata and labels
├── logs/
│   └── access_log.csv   # Access logs (optional)
└── requirements.txt     # Python dependencies
```

---

## 🔧 Setup

### 1. Clone the Repo

```bash
git clone https://github.com/HariCodesHere/snapaccess.git
cd snapaccess
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Tool

```bash
python main.py
```

---

## 📷 Switching Cameras

By default, SnapAccess uses your system’s primary camera (`cv2.VideoCapture(0)`).  
To switch to another camera, change the index in `camera_manager.py`:

```python
cap = cv2.VideoCapture(1)  # or 2, or a specific device path
```

---

## ❗ No Hardware Required

SnapAccess is designed to work with no physical components. It:
- ❌ Does not use Arduino
- ❌ Does not trigger locks or relays
- ✅ Works entirely in software
- ✅ Outputs logs and recognition results

---

## 👨‍💻 Developed By

- Harikrishnan Santhosh  
Part of the FaceLockR project initiative.

---

## 📜 License

MIT License

---

> _“Snap your face. Secure your access. — SnapAccess”_
