import tkinter as tk
from tkinter import messagebox
from utils import register_face, start_recognition

def main():
    root = tk.Tk()
    root.title("SnapAccess")
    root.geometry("300x200")
    root.resizable(False, False)

    title = tk.Label(root, text="🔓 SnapAccess", font=("Helvetica", 16, "bold"))
    title.pack(pady=20)

    register_btn = tk.Button(root, text="Register Face", command=register_face, width=20)
    register_btn.pack(pady=10)

    recognize_btn = tk.Button(root, text="Start Recognition", command=start_recognition, width=20)
    recognize_btn.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
