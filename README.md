# 🔄 Stepper Motor Control System

<p align="center">
  <img src="https://img.shields.io/badge/Arduino-UNO-00979D?style=for-the-badge&logo=arduino&logoColor=white" alt="Arduino UNO">
  <img src="https://img.shields.io/badge/Stepper-Motor-orange?style=for-the-badge" alt="Stepper Motor">
  <img src="https://img.shields.io/badge/C%2B%2B-Arduino-blue?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Hardware-Embedded-green?style=for-the-badge" alt="Embedded">
</p>

<p align="center">
  <b>A simple and practical Stepper Motor control project using Arduino UNO.</b>
</p>

<p align="center">
  Control • Rotation • Direction • Step Position • Embedded Systems
</p>

---

## 📌 About The Project

This project is an **Arduino-based Stepper Motor control system** designed to demonstrate how a stepper motor can be controlled accurately using a microcontroller.

The main idea of the project is to generate controlled step signals and use them to move a stepper motor in a specific direction and position.

Stepper motors are widely used in:

* 🤖 Robotics
* 🏭 CNC machines
* 🖨️ 3D printers
* 📷 Camera systems
* ⚙️ Industrial automation
* 🔧 Motion-control systems
* 🛰️ Embedded systems

This repository contains the Arduino/UNO code and the related motor-control files.

---

## 🎥 Project Demo

### ▶️ Video

A demonstration video is included in this repository:

**[`اجرا.mp4`](./اجرا.mp4)**

You can download or open the video directly from the repository to see the motor in operation.

---

## 📸 Project Gallery

> Put your real project photos inside the `assets` folder using the names below.

### 🔧 Hardware Setup

<p align="center">
  <img src="./assets/hardware.jpg" width="700" alt="Stepper Motor Hardware Setup">
</p>

### ⚡ Arduino & Motor Connection

<p align="center">
  <img src="./assets/arduino-motor.jpg" width="700" alt="Arduino and Stepper Motor Connection">
</p>

### 🏗️ Complete Project

<p align="center">
  <img src="./assets/project.jpg" width="700" alt="Complete Stepper Motor Project">
</p>

---

## ⚙️ How It Works

A stepper motor does not rotate continuously like a conventional DC motor.

Instead, its movement is divided into individual **steps**.

The Arduino controls the motor by sending electrical pulses to the motor driver.

Conceptually:

```text
Arduino UNO
     │
     │ Control Signals
     ▼
Motor Driver
     │
     │ Electrical Pulses
     ▼
Stepper Motor
     │
     ▼
Mechanical Rotation
```

Each pulse causes the motor to move by a specific angular amount.

Therefore:

```text
More pulses  →  More rotation
Fewer pulses →  Less rotation
```

The direction signal determines whether the motor rotates clockwise or counter-clockwise.

---

## 🧠 Control Logic

The basic control process is:

```text
Start
  │
  ▼
Initialize Arduino
  │
  ▼
Configure Motor Pins
  │
  ▼
Select Direction
  │
  ▼
Generate STEP Pulses
  │
  ▼
Motor Rotates
  │
  ▼
Repeat
```

The exact behavior depends on the code and hardware configuration used in the project.

---

## 🧰 Hardware Requirements

| Component        | Purpose                                  |
| ---------------- | ---------------------------------------- |
| 🟦 Arduino UNO   | Main microcontroller                     |
| ⚙️ Stepper Motor | Converts electrical pulses into rotation |
| 🔌 Motor Driver  | Drives the motor safely                  |
| 🔋 Power Supply  | Provides motor power                     |
| 🧵 Jumper Wires  | Electrical connections                   |
| 🧪 Breadboard    | Optional prototyping board               |

> ⚠️ **Important:** Do not power a stepper motor directly from an Arduino GPIO pin. A suitable motor driver should be used between the Arduino and motor.

---

## 💻 Software Requirements

* [Arduino IDE](https://www.arduino.cc/en/software)
* Arduino UNO board support
* USB cable
* Compatible Stepper Motor library, if required by the source code

---

## 📁 Project Structure

```text
setpper-motor/
│
├── 📂 STP-MOTOR/
│   └── Stepper motor related files
│
├── 📂 UNO/
│   └── Arduino UNO source code
│
├── 📂 Panel - telegram/
│   └── Additional project files
│
├── 📂 assets/
│   ├── hardware.jpg
│   ├── arduino-motor.jpg
│   └── project.jpg
│
├── 🎥 اجرا.mp4
│
└── 📄 README.md
```

---

## 🔌 Basic Wiring Concept

For a typical STEP/DIR motor driver, the Arduino communicates with the driver using control signals similar to:

| Arduino     | Driver | Function           |
| ----------- | ------ | ------------------ |
| Digital Pin | STEP   | Motor step pulse   |
| Digital Pin | DIR    | Rotation direction |
| Digital Pin | ENABLE | Driver enable      |
| GND         | GND    | Common ground      |

> The exact Arduino pins depend on the implementation in the source code.

A typical connection looks like:

```text
              Arduino UNO
          ┌─────────────────┐
          │                 │
          │     STEP ───────┼────────► STEP
          │      DIR ───────┼────────► DIR
          │     ENA ────────┼────────► ENABLE
          │      GND ───────┼────────► GND
          │                 │
          └─────────────────┘
                           │
                           ▼
                    ┌─────────────┐
                    │ Motor Driver│
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │   Stepper   │
                    │    Motor    │
                    └─────────────┘
```

---

## 🚀 Getting Started

### 1️⃣ Clone the repository

```bash
git clone https://github.com/ho3-win/setpper-motor.git
```

### 2️⃣ Open the project

Open the Arduino source code from:

```text
UNO/
```

using the Arduino IDE.

### 3️⃣ Connect Arduino UNO

Connect your Arduino UNO to your computer using USB.

### 4️⃣ Select the board

In Arduino IDE:

```text
Tools
  → Board
      → Arduino UNO
```

### 5️⃣ Select the correct port

```text
Tools
  → Port
      → Arduino UNO
```

### 6️⃣ Upload

Click:

```text
Upload
```

and wait until the upload is completed.

### 7️⃣ Test the motor

After uploading the program, connect the motor driver and power supply correctly and test the motor.

---

## 🎯 Main Features

* ✅ Arduino UNO based control
* ✅ Stepper motor control
* ✅ Controlled rotation
* ✅ Direction control
* ✅ Pulse-based movement
* ✅ Simple embedded-system architecture
* ✅ Easy to modify
* ✅ Suitable for learning and experimentation

---

## 📚 What This Project Demonstrates

This project is useful for learning about:

### 🔹 Embedded Systems

How a microcontroller interacts with external hardware.

### 🔹 Digital Signals

How digital outputs can generate control pulses.

### 🔹 Motor Control

How electrical signals can be converted into mechanical movement.

### 🔹 Automation

How precise motion can be controlled programmatically.

### 🔹 Arduino Programming

Basic hardware control using C/C++ and the Arduino framework.

---

## 🧪 Possible Improvements

This project can be extended with additional features such as:

* 🎛️ Speed control
* 🔄 Automatic direction switching
* 🎚️ Potentiometer-based speed control
* 🖥️ LCD/OLED display
* 🎮 Joystick control
* 📡 Bluetooth control
* 📱 Mobile application
* 🌐 Web-based control
* 📍 Position tracking
* 🛑 Emergency stop
* ⚡ Acceleration and deceleration
* 🎯 Precise positioning
* 🤖 Integration with robotics projects

---

## 🔮 Future Development

Possible future versions could include:

```text
Arduino UNO
     │
     ├── Stepper Motor
     │
     ├── LCD Display
     │
     ├── Joystick
     │
     ├── Bluetooth
     │
     └── Computer / Web Control
```

This would transform the basic project into a more complete **motion-control platform**.

---

## 📷 More Photos

If you add more photos to the `assets` directory, you can display them here:

```markdown
<p align="center">
  <img src="./assets/photo-1.jpg" width="45%">
  <img src="./assets/photo-2.jpg" width="45%">
</p>

<p align="center">
  <img src="./assets/photo-3.jpg" width="45%">
  <img src="./assets/photo-4.jpg" width="45%">
</p>
```

---

## 🎬 Demo

<p align="center">

### Stepper Motor in Action ⚙️

**Watch:** [`اجرا.mp4`](./اجرا.mp4)

</p>

---

## 🛠️ Technologies

| Technology       | Usage                    |
| ---------------- | ------------------------ |
| 🔵 Arduino       | Microcontroller platform |
| 🟦 Arduino UNO   | Hardware board           |
| 🟠 C/C++         | Programming language     |
| ⚙️ Stepper Motor | Motion actuator          |
| 🔌 Motor Driver  | Motor interface          |
| 🔧 Git           | Version control          |
| 🐙 GitHub        | Project hosting          |

---

## 💡 Why Stepper Motors?

Stepper motors are especially useful when controlled movement and repeatability are important.

Unlike a simple DC motor, a stepper motor can be commanded through discrete steps, making it useful for applications where the controller needs predictable movement.

Typical applications include:

```text
Robotics
   ↓
CNC
   ↓
3D Printing
   ↓
Automation
   ↓
Camera Systems
   ↓
Precision Motion
```

---

## ⚠️ Safety Notes

Please make sure that:

* ⚠️ The motor is connected through an appropriate driver.
* ⚠️ The motor power supply matches the motor and driver specifications.
* ⚠️ Arduino GPIO pins are not used to directly power the motor.
* ⚠️ Ground connections are configured correctly.
* ⚠️ The motor driver current is configured appropriately.
* ⚠️ Power is disconnected before changing wiring.

---

## 🤝 Contributing

Contributions are welcome!

If you have an idea for improving this project:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Test your changes.
5. Open a Pull Request.

Example:

```bash
git checkout -b feature/improved-motor-control
git add .
git commit -m "Improve stepper motor control"
git push origin feature/improved-motor-control
```

---

## ⭐ Support

If you found this project useful, consider giving the repository a ⭐ on GitHub.

It helps support the project and encourages further development.

---

## 👨‍💻 Author

**ho3-win**

GitHub:

👉 https://github.com/ho3-win

Project:

👉 https://github.com/ho3-win/setpper-motor

---

## 📜 License

This project is provided for educational and experimental purposes.

You are free to modify and improve the source code for your own projects.

---

<p align="center">

### ⚙️ Built with Arduino • Electronics • C/C++ • Curiosity

**Thanks for checking out the project! 🚀**

</p>
