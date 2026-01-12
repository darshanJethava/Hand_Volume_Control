# ✋ Hand Gesture Volume Control System

The Hand Gesture Volume Control System is a real-time computer vision application
that allows users to control system volume using hand gestures. It uses hand
landmark detection to measure the distance between fingers and map it to system
volume levels.

This project demonstrates the practical use of computer vision and human–computer
interaction concepts.

---

## 🛠 Technologies Used
- Python 3
- OpenCV
- MediaPipe
- NumPy
- PyCAW (System Volume Control)
- Math & Time modules

---

## ✨ Features

### Hand Detection
- Real-time detection of a single hand using MediaPipe
- Tracks all 21 hand landmarks
- Optional visualization of landmarks and colored markers

### Volume Control
- Volume is controlled by the distance between:
  - Thumb Tip (Landmark ID 4)
  - Index Finger Tip (Landmark ID 8)
- Finger distance behavior:
  - Fingers close → Volume decreases
  - Fingers apart → Volume increases
  - Very small distance → System mutes

### User Interface Feedback
- Real-time FPS display
- Volume level bar
- Volume percentage indicator

---

## 🎯 Purpose
This project was developed to explore gesture-based interaction and real-time
computer vision applications. It highlights the use of Python libraries for
hardware-level system control through intuitive hand gestures.

---

## 👨‍💻 Author
**Darshan Jethava**  
🎓 Computer Engineering Student  
💻 Application & Full-Stack Developer  

GitHub: https://github.com/darshanjethava
