# ✋ Hand Gesture Controlled LEDs with Arduino

This project uses **OpenCV + cvzone (MediaPipe)** in Python to detect hand gestures (finger count) from a webcam and sends the count to an **Arduino** via serial communication.  
The Arduino then lights up **LEDs** based on the number of fingers detected.

---

## 🚀 Features
- Detects fingers using **hand tracking** in real-time
- Sends **finger count (0–5)** to Arduino via Serial
- Arduino lights up **LEDs on pins 2–6** according to count
- Can be extended to control motors, relays, or other devices

---

## 🛠️ Requirements

### Hardware
- Arduino UNO (or compatible board)
- 5 LEDs + 220Ω resistors
- Breadboard & jumper wires
- USB cable for Arduino

### Software
- Python 3.8+
- Arduino IDE
- Python libraries:
  - `opencv-python`
  - `cvzone`
  - `pyserial`
