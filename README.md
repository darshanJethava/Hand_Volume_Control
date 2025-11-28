Hand Gesture Volume Control System

  This project detects hand landmarks using Mediapipe and changes system volume by measuring the distance between your thumb and index finger.
  A Python-based real-time hand gesture recognition system using OpenCV, Mediapipe, and PyCAW to control system volume using your fingers.
  
Features:

Hand Detection:
  Detects a single hand in real time using Mediapipe.
  Tracks all 21 hand landmarks.
  Optionally displays landmark points and colored markers.
  
Volume Control:
  The distance between Thumb Tip (id 4) and Index Finger Tip (id 8) controls the volume.
  When fingers are close → volume decreases
  When fingers separate → volume increases
  When distance is very small → system mutes

UI Feedback:
  Real-time FPS
  Volume bar
  Percentage display

Technologies Used
  Python 3
  OpenCV
  Mediapipe
  NumPy
  PyCAW (for system volume control)
  Math & time modules
