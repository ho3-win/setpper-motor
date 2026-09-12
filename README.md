# ⚙️ Stepper Motor Control System

<p align="center">
  <img src="https://img.shields.io/badge/Arduino-UNO-00979D?style=for-the-badge&logo=arduino&logoColor=white" alt="Arduino UNO">
  <img src="https://img.shields.io/badge/Stepper-Motor-orange?style=for-the-badge" alt="Stepper Motor">
  <img src="https://img.shields.io/badge/C%2B%2B-Arduino-blue?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Embedded-System-green?style=for-the-badge" alt="Embedded System">
</p>

<p align="center">
  <b>Arduino UNO based Stepper Motor Control Project</b><br>
  پروژه کنترل موتور پله‌ای با استفاده از Arduino UNO
</p>

---

## 🎬 Project Demo | ویدئوی اجرای پروژه

<p align="center">
  <a href="./اجرا.mp4">
    <img src="./Panel%20-%20telegram/robot_banner.jpg" width="750" alt="Stepper Motor Project - Click to watch the demo">
  </a>
</p>

<p align="center">
  👆 <b>Click the image to watch the project demo</b><br>
  برای مشاهده ویدئوی اجرای پروژه روی تصویر کلیک کنید
</p>

---

# 🇬🇧 English

## 📌 About The Project

This project is an **Arduino UNO based Stepper Motor control system** designed to demonstrate how a stepper motor can be controlled accurately using a microcontroller.

Unlike a conventional DC motor, a stepper motor rotates in a series of discrete steps. By controlling the number and timing of these steps, the Arduino can control the motor's movement, direction, and approximate position.

The project provides a simple foundation for learning **embedded systems, digital control signals, motor drivers, and motion control**.

Stepper motors are commonly used in:

* 🤖 Robotics
* 🏭 Industrial automation
* 🖨️ 3D printers
* ⚙️ CNC machines
* 📷 Camera systems
* 🦾 Robotic arms
* 🔧 Positioning systems
* 🚗 Automated mechanisms

---

## ⚙️ How Does It Work?

The Arduino UNO acts as the main controller.

It generates control signals that are sent to a suitable motor driver. The driver then provides the required electrical current to the stepper motor.

The general architecture is:

```text
                 Arduino UNO
                      │
                      │ Control Signals
                      ▼
               ┌─────────────┐
               │ Motor Driver│
               └──────┬──────┘
                      │
                      │ Motor Power
                      ▼
               ┌─────────────┐
               │   Stepper   │
               │    Motor    │
               └─────────────┘
                      │
                      ▼
                  Rotation
```

The Arduino controls the motor by generating a sequence of pulses.

In a typical STEP/DIR system:

```text
STEP → Controls movement
DIR  → Controls direction
ENA  → Enables/disables the driver
GND  → Common ground
```

Each valid STEP pulse causes the motor to move by one step or microstep, depending on the motor driver configuration.

Therefore:

```text
More STEP pulses  →  More rotation
Fewer STEP pulses →  Less rotation

DIR = Direction A →  Rotate one way
DIR = Direction B →  Rotate the opposite way
```

---

## 🧠 Stepper Motor Basics

A stepper motor is an electric motor designed to divide its rotation into a number of small, controlled steps.

For example, if a motor has a step angle of:

```text
1.8° per step
```

then one complete revolution requires:

```text
360° ÷ 1.8° = 200 steps
```

So, theoretically:

```text
200 steps  →  360°
100 steps  →  180°
50 steps   →  90°
25 steps   →  45°
```

The actual resolution can be increased when the motor driver supports **microstepping**.

For example:

```text
Full Step
Half Step
1/4 Step
1/8 Step
1/16 Step
...
```

The available microstepping options depend on the specific motor driver.

---

## 🔌 Hardware Requirements

| Component        | Description                                               |
| ---------------- | --------------------------------------------------------- |
| 🔵 Arduino UNO   | Main microcontroller                                      |
| ⚙️ Stepper Motor | Converts electrical signals into mechanical rotation      |
| 🔌 Motor Driver  | Provides the required motor current and control interface |
| 🔋 Power Supply  | Supplies power to the motor                               |
| 🧵 Jumper Wires  | Used for electrical connections                           |
| 🧪 Breadboard    | Optional for prototyping                                  |

> **Important:** The exact motor driver and power supply must match the specifications of your stepper motor.

---

## 🔧 Basic Wiring

For a common STEP/DIR motor driver, the connection concept is:

```text
Arduino UNO              Motor Driver
───────────              ────────────

Digital Pin  ──────────► STEP
Digital Pin  ──────────► DIR
Digital Pin  ──────────► ENABLE
GND          ──────────► GND

                         │
                         │
                         ▼
                    Stepper Motor
```

The exact Arduino pins depend on the implementation used in the source code.

Always check the motor driver's documentation before connecting the hardware.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/ho3-win/setpper-motor.git
```

### 2. Open the project

Open the Arduino source files located in:

```text
UNO/
```

using the **Arduino IDE**.

### 3. Connect Arduino UNO

Connect the Arduino UNO to your computer using a USB cable.

### 4. Select the board

In Arduino IDE:

```text
Tools
 → Board
 → Arduino UNO
```

### 5. Select the correct port

```text
Tools
 → Port
 → Arduino UNO
```

### 6. Upload the program

Press the **Upload** button in Arduino IDE.

After the upload is completed, connect the motor driver and power supply according to the hardware specifications.

---

## ✨ Features

* ⚙️ Stepper Motor Control
* 🔄 Direction Control
* 🎯 Step-based Movement
* 📐 Controlled Rotation
* 🔌 Arduino UNO Interface
* 🧠 Simple Embedded-System Architecture
* 🛠️ Easy to modify and extend
* 🎥 Project demonstration included
* 📱 Additional Telegram panel files included

---

## 📂 Project Structure

```text
setpper-motor/
│
├── 📁 STP-MOTOR/
│   └── Stepper Motor related files
│
├── 📁 UNO/
│   └── Arduino UNO source code
│
├── 📁 Panel - telegram/
│   └── Telegram panel files
│   └── robot_banner.jpg
│
├── 🎥 اجرا.mp4
│
└── 📄 README.md
```

---

## 🧩 Applications

The concepts demonstrated by this project can be used as a starting point for larger systems such as:

### 🤖 Robotics

Precise control of wheels, robotic arms, linear actuators, and other mechanisms.

### 🏭 Automation

Controlling mechanical positioning systems in automated machines.

### 🖨️ 3D Printing

Stepper motors are widely used for controlling X, Y, Z, and extrusion mechanisms.

### ⚙️ CNC

Stepper motors can be used to control machine axes and provide controlled movement.

### 📷 Camera Systems

Stepper motors can be used for controlled camera movement, focusing mechanisms, and rotating platforms.

---

## 🔮 Future Improvements

The project can be extended with additional features such as:

* 🎛️ Variable speed control
* 🎚️ Potentiometer-based control
* 🎮 Joystick control
* 📱 Bluetooth control
* 📡 Wireless control
* 🖥️ LCD/OLED display
* 🎯 Position tracking
* 🛑 Emergency stop
* 📈 Acceleration and deceleration
* 🔄 Automatic direction control
* 🌐 Web-based control
* 🤖 Integration with a larger robotic system

A possible future architecture could look like:

```text
                 Arduino / Controller
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼
     Joystick         Display         Wireless
        │                │                │
        └────────────────┼────────────────┘
                         │
                         ▼
                   Motor Driver
                         │
                         ▼
                   Stepper Motor
```

---

## ⚠️ Safety Notes

Please follow these guidelines when working with the hardware:

* ⚠️ Never connect a stepper motor directly to Arduino GPIO pins.
* ⚠️ Use an appropriate motor driver.
* ⚠️ Use a suitable power supply for the motor and driver.
* ⚠️ Check the motor driver's current settings.
* ⚠️ Make sure the wiring is correct before applying power.
* ⚠️ Disconnect power before changing the wiring.
* ⚠️ Make sure the Arduino and driver have the required common ground connection.

---

## 📚 What You Can Learn From This Project

This project demonstrates several important concepts in electronics and programming:

```text
Arduino Programming
       ↓
Digital Outputs
       ↓
Control Pulses
       ↓
Motor Driver
       ↓
Stepper Motor
       ↓
Controlled Mechanical Movement
```

It is therefore a useful practical project for learning:

* Embedded Systems
* Arduino Programming
* C/C++
* Digital Electronics
* Motor Control
* Hardware/Software Interaction
* Automation
* Robotics

---

# 🇮🇷 فارسی

## 📌 درباره پروژه

این پروژه یک سیستم **کنترل موتور پله‌ای با استفاده از Arduino UNO** است که برای یادگیری و پیاده‌سازی کنترل حرکت موتورهای Stepper طراحی شده است.

برخلاف موتورهای DC معمولی، موتور پله‌ای به صورت مرحله‌ای حرکت می‌کند. با کنترل تعداد پالس‌ها، زمان‌بندی آن‌ها و جهت سیگنال، می‌توان حرکت و جهت چرخش موتور را کنترل کرد.

این پروژه یک نمونه عملی برای آشنایی با مفاهیم زیر است:

* 🤖 رباتیک
* ⚙️ کنترل موتور
* 🔌 الکترونیک
* 💻 برنامه‌نویسی Arduino
* 🧠 سیستم‌های Embedded
* 🏭 اتوماسیون صنعتی
* 🎯 کنترل حرکت

---

## ⚙️ نحوه عملکرد

در این پروژه **Arduino UNO** نقش کنترل‌کننده اصلی را دارد.

آردوینو سیگنال‌های کنترلی را تولید کرده و آن‌ها را به درایور موتور ارسال می‌کند. درایور نیز جریان موردنیاز موتور را تأمین کرده و باعث حرکت موتور پله‌ای می‌شود.

ساختار کلی:

```text
Arduino UNO
     │
     │ سیگنال کنترلی
     ▼
Motor Driver
     │
     │ توان موتور
     ▼
Stepper Motor
     │
     ▼
حرکت و چرخش
```

در سیستم‌های معمول STEP/DIR:

```text
STEP  → فرمان حرکت موتور
DIR   → تعیین جهت چرخش
ENA   → فعال/غیرفعال کردن درایور
GND   → زمین مشترک
```

هر پالس STEP باعث حرکت موتور به اندازه یک Step یا Microstep می‌شود.

در نتیجه:

```text
پالس بیشتر  → چرخش بیشتر
پالس کمتر  → چرخش کمتر

تغییر DIR  → تغییر جهت چرخش
```

---

## 🧠 موتور پله‌ای چیست؟

موتور پله‌ای موتوری است که چرخش آن به تعداد مشخصی مرحله تقسیم می‌شود.

برای مثال اگر زاویه هر Step برابر با:

```text
1.8°
```

باشد، برای یک دور کامل به:

```text
360 ÷ 1.8 = 200 Step
```

نیاز داریم.

بنابراین به صورت تئوری:

```text
200 Step → 360°
100 Step → 180°
50 Step  → 90°
25 Step  → 45°
```

البته در صورت پشتیبانی درایور از **Microstepping** می‌توان حرکت نرم‌تر و با رزولوشن بالاتر ایجاد کرد.

---

## 🔌 قطعات موردنیاز

| قطعه             | کاربرد                   |
| ---------------- | ------------------------ |
| 🔵 Arduino UNO   | کنترل اصلی پروژه         |
| ⚙️ Stepper Motor | ایجاد حرکت مکانیکی       |
| 🔌 Motor Driver  | راه‌اندازی و کنترل موتور |
| 🔋 Power Supply  | تأمین توان موتور         |
| 🧵 Jumper Wire   | اتصال قطعات              |
| 🧪 Breadboard    | نمونه‌سازی، در صورت نیاز |

---

## 🎯 ویژگی‌های پروژه

* ⚙️ کنترل موتور پله‌ای
* 🔄 کنترل جهت چرخش
* 🎯 کنترل حرکت بر اساس Step
* 📐 امکان کنترل میزان چرخش
* 🔌 استفاده از Arduino UNO
* 🧠 معماری ساده و قابل توسعه
* 🛠️ مناسب برای پروژه‌های آموزشی و رباتیک
* 🎥 دارای ویدئوی اجرای پروژه
* 📱 دارای فایل‌های مربوط به پنل Telegram

---

## 🚀 نحوه اجرا

ابتدا Repository را دریافت کنید:

```bash
git clone https://github.com/ho3-win/setpper-motor.git
```

سپس فایل‌های Arduino موجود در پوشه:

```text
UNO/
```

را با **Arduino IDE** باز کنید.

Arduino UNO را به سیستم متصل کرده و از بخش:

```text
Tools → Board → Arduino UNO
```

برد صحیح را انتخاب کنید.

سپس Port مربوط به Arduino را انتخاب کرده و برنامه را روی برد Upload کنید.

پس از آپلود، موتور و درایور را مطابق مشخصات سخت‌افزار متصل کرده و پروژه را اجرا کنید.

---

## 📱 Panel - Telegram

در پروژه یک پوشه با نام:

```text
Panel - telegram/
```

نیز قرار دارد که فایل‌های مربوط به بخش Telegram پروژه در آن قرار گرفته‌اند.

تصویر معرفی این بخش در README استفاده شده و با کلیک روی آن می‌توانید مستقیماً **ویدئوی اجرای پروژه** را مشاهده کنید.

---

## 🔮 ایده‌های توسعه

این پروژه قابلیت توسعه به یک سیستم کامل‌تر را دارد. برای مثال می‌توان موارد زیر را اضافه کرد:

* 🎛️ کنترل سرعت
* 🎚️ کنترل با Potentiometer
* 🎮 کنترل با Joystick
* 📱 کنترل با Bluetooth
* 📡 کنترل بی‌سیم
* 🖥️ نمایش اطلاعات روی LCD/OLED
* 🎯 تعیین موقعیت دقیق
* 🛑 کلید توقف اضطراری
* 📈 شتاب‌گیری و کاهش سرعت
* 🌐 کنترل از طریق Web
* 🤖 استفاده در پروژه‌های رباتیک

---

## ⚠️ نکات مهم

**موتور پله‌ای را مستقیماً به پایه‌های Arduino متصل نکنید.**

برای راه‌اندازی موتور باید از یک **Motor Driver مناسب** استفاده شود.

همچنین:

* منبع تغذیه باید با موتور و درایور سازگار باشد.
* جریان درایور باید متناسب با موتور تنظیم شود.
* قبل از روشن کردن سیستم، سیم‌کشی را بررسی کنید.
* هنگام تغییر سیم‌کشی، برق را قطع کنید.
* اتصال GND را مطابق مدار و درایور انجام دهید.

---

## 📚 مباحثی که این پروژه آموزش می‌دهد

با بررسی و توسعه این پروژه می‌توانید با مفاهیم زیر آشنا شوید:

```text
Arduino
   ↓
C/C++
   ↓
Digital Signals
   ↓
Motor Driver
   ↓
Stepper Motor
   ↓
Motion Control
   ↓
Robotics & Automation
```

---

## 👨‍💻 Author

**ho3-win**

🔗 GitHub:
https://github.com/ho3-win

⭐ اگر این پروژه برای شما مفید بود، خوشحال می‌شوم Repository را Star کنید.

---

<p align="center">

### ⚙️ Arduino • Stepper Motor • Robotics • Embedded Systems

**Built for learning, experimenting and creating 🚀**

</p>
