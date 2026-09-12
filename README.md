# ⚙️ Stepper Motor Control System

<p align="center">
  <img src="https://img.shields.io/badge/Arduino-UNO-00979D?style=for-the-badge&logo=arduino&logoColor=white">
  <img src="https://img.shields.io/badge/Stepper%20Motor-Control-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/C%2B%2B-Arduino-blue?style=for-the-badge&logo=cplusplus&logoColor=white">
  <img src="https://img.shields.io/badge/Embedded-System-green?style=for-the-badge">
</p>

<p align="center">
  <strong>Arduino UNO based Stepper Motor Control System</strong>
  <br>
  سیستم کنترل موتور پله‌ای مبتنی بر Arduino UNO
</p>

<p align="center">
  <a href="#-english">
    <img src="https://img.shields.io/badge/🇬🇧%20English-Click%20Here-blue?style=for-the-badge">
  </a>
  &nbsp;
  <a href="#-فارسی">
    <img src="https://img.shields.io/badge/🇮🇷%20فارسی-کلیک%20کنید-red?style=for-the-badge">
  </a>
</p>

---

## 🎬 Project Demo

<p align="center">
  <a href="./demo.gif">
    <img src="./Panel%20-%20telegram/robot_banner.jpg" width="750" alt="Stepper Motor Control System Demo">
  </a>
</p>

<p align="center">
  <strong>👆 Click the image to watch the project demo</strong>
  <br>
  برای مشاهده اجرای پروژه روی تصویر کلیک کنید
</p>

---

# 🇬🇧 English

<a name="-english"></a>

## 📌 About

**Stepper Motor Control System** is an Arduino UNO based project designed to demonstrate accurate and controlled movement of a stepper motor.

The Arduino generates control signals that are sent to a motor driver. The driver provides the required electrical power to the motor and controls its movement.

The project demonstrates fundamental concepts of:

* ⚙️ Stepper motor control
* 🔄 Direction control
* 🎯 Step-based positioning
* 🔌 Motor drivers
* 💻 Arduino / C++
* 🧠 Embedded systems
* 🤖 Robotics
* 🏭 Automation

It can also serve as a starting point for more advanced motion-control and robotics projects.

---

## ✨ Features

| Feature                  | Description                                  |
| ------------------------ | -------------------------------------------- |
| ⚙️ Stepper Control       | Control stepper motor movement               |
| 🔄 Direction Control     | Change the motor rotation direction          |
| 🎯 Step-Based Movement   | Move the motor by a specific number of steps |
| 📐 Controlled Rotation   | Calculate approximate angular movement       |
| 🔌 Arduino Interface     | Arduino UNO as the main controller           |
| 🧠 Embedded Architecture | Simple hardware/software interaction         |
| 🛠️ Extensible           | Easy to modify and expand                    |
| 🎥 Demo                  | Project demonstration included               |
| 📱 Telegram Files        | Additional Telegram panel files included     |

---

## ⚙️ How It Works

The basic architecture of the system is:

```text
                  ┌──────────────────┐
                  │    Arduino UNO   │
                  │   Main Controller│
                  └────────┬─────────┘
                           │
                    Control Signals
                           │
                           ▼
                  ┌──────────────────┐
                  │   Motor Driver   │
                  └────────┬─────────┘
                           │
                      Motor Power
                           │
                           ▼
                  ┌──────────────────┐
                  │  Stepper Motor   │
                  └────────┬─────────┘
                           │
                           ▼
                       Rotation
```

For a typical **STEP / DIR** driver:

```text
STEP  → Movement command
DIR   → Rotation direction
ENA   → Driver enable / disable
GND   → Common ground
```

The Arduino generates pulses on the STEP input.

```text
More STEP pulses  → More movement
Fewer STEP pulses → Less movement

DIR = HIGH → Direction A
DIR = LOW  → Direction B
```

The exact behavior depends on the motor driver and the implementation used in the source code.

---

## 🧠 Stepper Motor Basics

A stepper motor divides its rotation into a number of discrete steps.

For example, a motor with a **1.8° step angle** requires:

```text
360° ÷ 1.8° = 200 steps
```

Therefore:

```text
200 steps → 360°
100 steps → 180°
50 steps  → 90°
25 steps  → 45°
```

### 🔬 Microstepping

Some motor drivers support microstepping to provide smoother movement and higher positional resolution.

Common configurations include:

```text
Full Step
Half Step
1/4 Step
1/8 Step
1/16 Step
...
```

The available microstepping modes depend on the motor driver.

---

## 🔌 Hardware Requirements

| Component            | Purpose                             |
| -------------------- | ----------------------------------- |
| 🔵 **Arduino UNO**   | Main microcontroller                |
| ⚙️ **Stepper Motor** | Mechanical movement                 |
| 🔌 **Motor Driver**  | Controls motor current and movement |
| 🔋 **Power Supply**  | Provides motor power                |
| 🧵 **Jumper Wires**  | Electrical connections              |
| 🧪 **Breadboard**    | Optional prototyping                |

> ⚠️ The motor driver and power supply must be selected according to the specifications of the stepper motor.

---

## 🔧 Basic Wiring

A typical STEP/DIR configuration looks like this:

```text
        Arduino UNO                  Motor Driver
        ───────────                  ────────────

        Digital Pin  ─────────────► STEP
        Digital Pin  ─────────────► DIR
        Digital Pin  ─────────────► ENA
        GND         ─────────────► GND

                                      │
                                      │
                                      ▼
                                Stepper Motor

                                      ▲
                                      │
                               External Power
```

> ℹ️ The exact Arduino pins depend on the source code and hardware implementation.

Always check the motor driver's documentation before connecting the circuit.

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/ho3-win/setpper-motor.git
```

```bash
cd setpper-motor
```

### 2️⃣ Open the Arduino Project

Open the source files located in:

```text
UNO/
```

using **Arduino IDE**.

### 3️⃣ Connect Arduino UNO

Connect your Arduino UNO to your computer using a USB cable.

### 4️⃣ Select the Board

From Arduino IDE:

```text
Tools
 └── Board
      └── Arduino UNO
```

### 5️⃣ Select the Port

```text
Tools
 └── Port
      └── Arduino UNO
```

### 6️⃣ Upload

Click **Upload** in Arduino IDE.

After uploading the program, connect the motor driver, motor and external power supply according to their specifications.

---

## 📂 Project Structure

```text
setpper-motor/
│
├── 📁 STP-MOTOR/
│   └── Stepper motor related files
│
├── 📁 UNO/
│   └── Arduino UNO source code
│
├── 📁 Panel - telegram/
│   ├── Telegram panel files
│   └── robot_banner.jpg
│
├── 🎥 اجرا.mp4
│
└── 📄 README.md
```

---

## 📱 Telegram Panel

The repository also contains a separate directory for the Telegram-related panel:

```text
Panel - telegram/
```

This directory contains the additional files used for the Telegram part of the project.

The project banner is also located inside this directory:

```text
Panel - telegram/robot_banner.jpg
```

---

## 🤖 Possible Applications

The concepts used in this project can be applied to many real-world systems.

### 🤖 Robotics

Stepper motors can be used for:

* Robotic arms
* Wheels
* Linear actuators
* Rotating platforms
* Positioning mechanisms

### 🏭 Industrial Automation

Stepper motors are widely used for controlled mechanical positioning in automated systems.

### 🖨️ 3D Printers

Stepper motors are commonly used to control:

```text
X Axis
Y Axis
Z Axis
Extruder
```

### ⚙️ CNC Machines

Stepper motors can control machine axes and provide repeatable movement.

### 📷 Camera Systems

They can also be used for:

* Camera positioning
* Pan/tilt mechanisms
* Focus mechanisms
* Rotating platforms

---

## 🔮 Future Improvements

This project can be extended with many additional features:

* 🎛️ Variable speed control
* 🎚️ Potentiometer control
* 🎮 Joystick control
* 📱 Bluetooth control
* 📡 Wireless control
* 🖥️ LCD / OLED display
* 🎯 Position tracking
* 🛑 Emergency stop
* 📈 Acceleration and deceleration
* 🔄 Automatic direction control
* 🌐 Web-based control
* 🤖 Robotic system integration

A possible future architecture:

```text
                    Controller
                        │
          ┌─────────────┼─────────────┐
          │             │             │
          ▼             ▼             ▼
      🎮 Joystick   🖥️ Display    📡 Wireless
          │             │             │
          └─────────────┼─────────────┘
                        │
                        ▼
                 ┌──────────────┐
                 │ Motor Driver │
                 └──────┬───────┘
                        │
                        ▼
                 ⚙️ Stepper Motor
```

---

## ⚠️ Safety

Please follow these safety guidelines when working with the hardware:

* ⚠️ **Never connect a stepper motor directly to Arduino GPIO pins.**
* ⚠️ Always use a suitable motor driver.
* ⚠️ Use an appropriate external power supply.
* ⚠️ Configure the driver's current according to the motor specifications.
* ⚠️ Check all wiring before applying power.
* ⚠️ Disconnect power before modifying the wiring.
* ⚠️ Make sure the required common ground connections are present.
* ⚠️ Follow the manufacturer's documentation for the motor driver.

---

## 📚 What You Can Learn

This project provides practical experience with:

```text
Arduino Programming
        │
        ▼
      C / C++
        │
        ▼
   Digital Signals
        │
        ▼
   Control Pulses
        │
        ▼
    Motor Driver
        │
        ▼
   Stepper Motor
        │
        ▼
  Motion Control
        │
        ▼
 Robotics & Automation
```

### Main Topics

* Embedded Systems
* Arduino Programming
* C/C++
* Digital Electronics
* Motor Control
* Hardware / Software Interaction
* Robotics
* Automation
* Motion Control

---

## 👨‍💻 Author

<p align="center">

<strong>ho3-win</strong>

<br><br>

<a href="https://github.com/ho3-win">
  <img src="https://img.shields.io/badge/GitHub-ho3--win-black?style=for-the-badge&logo=github">
</a>

</p>

⭐ If you find this project useful, consider giving the repository a **Star**.

---

# 🇮🇷 فارسی

<a name="-فارسی"></a>

## 📌 درباره پروژه

**Stepper Motor Control System** یک پروژه مبتنی بر **Arduino UNO** برای کنترل و حرکت دقیق موتور پله‌ای است.

در این پروژه آردوینو به عنوان کنترل‌کننده اصلی عمل کرده و سیگنال‌های کنترلی را برای **Motor Driver** ارسال می‌کند. درایور نیز جریان موردنیاز موتور را تأمین کرده و حرکت آن را کنترل می‌کند.

این پروژه یک نمونه عملی برای یادگیری مفاهیم زیر است:

* ⚙️ کنترل موتور پله‌ای
* 🔄 کنترل جهت چرخش
* 🎯 کنترل حرکت بر اساس Step
* 📐 کنترل میزان چرخش
* 🔌 کار با Motor Driver
* 💻 برنامه‌نویسی Arduino و C++
* 🧠 سیستم‌های Embedded
* 🤖 رباتیک
* 🏭 اتوماسیون

---

## ✨ امکانات

| قابلیت                 | توضیح                         |
| ---------------------- | ----------------------------- |
| ⚙️ کنترل Stepper Motor | کنترل حرکت موتور              |
| 🔄 کنترل جهت           | تغییر جهت چرخش                |
| 🎯 حرکت بر اساس Step   | تعیین تعداد مراحل حرکت        |
| 📐 کنترل چرخش          | کنترل تقریبی زاویه حرکت       |
| 🔌 Arduino UNO         | کنترل‌کننده اصلی              |
| 🧠 معماری Embedded     | ارتباط نرم‌افزار و سخت‌افزار  |
| 🛠️ قابل توسعه         | امکان اضافه کردن امکانات جدید |
| 🎥 ویدئوی Demo         | نمایش اجرای پروژه             |
| 📱 Telegram Panel      | دارای فایل‌های بخش تلگرام     |

---

## ⚙️ نحوه عملکرد

ساختار کلی پروژه به صورت زیر است:

```text
                 ┌──────────────────┐
                 │    Arduino UNO   │
                 │   کنترل‌کننده    │
                 └────────┬─────────┘
                          │
                     سیگنال کنترل
                          │
                          ▼
                 ┌──────────────────┐
                 │   Motor Driver   │
                 │    درایور موتور  │
                 └────────┬─────────┘
                          │
                       توان موتور
                          │
                          ▼
                 ┌──────────────────┐
                 │  Stepper Motor   │
                 │   موتور پله‌ای   │
                 └────────┬─────────┘
                          │
                          ▼
                       چرخش موتور
```

در یک سیستم معمول **STEP / DIR**:

```text
STEP → فرمان حرکت
DIR  → تعیین جهت
ENA  → فعال / غیرفعال کردن درایور
GND  → زمین مشترک
```

آردوینو با تولید پالس‌های STEP باعث حرکت موتور می‌شود.

```text
پالس بیشتر  → حرکت بیشتر
پالس کمتر   → حرکت کمتر

DIR = HIGH → جهت اول
DIR = LOW  → جهت دوم
```

رفتار دقیق این پایه‌ها به نوع درایور و کد استفاده‌شده بستگی دارد.

---

## 🧠 موتور پله‌ای چیست؟

موتور پله‌ای موتوری است که چرخش آن به تعداد مشخصی مرحله تقسیم می‌شود.

برای مثال اگر زاویه هر Step برابر با:

```text
1.8°
```

باشد:

```text
360° ÷ 1.8° = 200 Step
```

بنابراین:

```text
200 Step → 360°
100 Step → 180°
50 Step  → 90°
25 Step  → 45°
```

### 🔬 Microstepping

برخی Motor Driverها از Microstepping پشتیبانی می‌کنند که باعث حرکت نرم‌تر و افزایش رزولوشن حرکتی می‌شود.

برای مثال:

```text
Full Step
Half Step
1/4 Step
1/8 Step
1/16 Step
...
```

میزان Microstepping قابل استفاده به مدل Motor Driver بستگی دارد.

---

## 🔌 قطعات موردنیاز

| قطعه                 | کاربرد                   |
| -------------------- | ------------------------ |
| 🔵 **Arduino UNO**   | کنترل اصلی پروژه         |
| ⚙️ **Stepper Motor** | ایجاد حرکت مکانیکی       |
| 🔌 **Motor Driver**  | کنترل جریان و حرکت موتور |
| 🔋 **Power Supply**  | تأمین توان موتور         |
| 🧵 **Jumper Wire**   | اتصال قطعات              |
| 🧪 **Breadboard**    | نمونه‌سازی در صورت نیاز  |

> ⚠️ درایور و منبع تغذیه باید متناسب با مشخصات موتور پله‌ای انتخاب شوند.

---

## 🔧 سیم‌کشی پایه

در یک سیستم معمول STEP/DIR:

```text
        Arduino UNO                  Motor Driver
        ───────────                  ────────────

        Digital Pin  ─────────────► STEP
        Digital Pin  ─────────────► DIR
        Digital Pin  ─────────────► ENA
        GND         ─────────────► GND

                                      │
                                      ▼
                                Stepper Motor

                                      ▲
                                      │
                               منبع تغذیه خارجی
```

> ℹ️ پایه‌های دقیق Arduino به کد و سخت‌افزار استفاده‌شده در پروژه بستگی دارند.

قبل از اتصال، حتماً مستندات Motor Driver را بررسی کنید.

---

## 🚀 راه‌اندازی پروژه

### 1️⃣ دریافت Repository

```bash
git clone https://github.com/ho3-win/setpper-motor.git
```

سپس:

```bash
cd setpper-motor
```

### 2️⃣ باز کردن پروژه

فایل‌های مربوط به Arduino در مسیر زیر قرار دارند:

```text
UNO/
```

این فایل‌ها را با **Arduino IDE** باز کنید.

### 3️⃣ اتصال Arduino UNO

برد Arduino UNO را با کابل USB به کامپیوتر متصل کنید.

### 4️⃣ انتخاب Board

در Arduino IDE:

```text
Tools
 └── Board
      └── Arduino UNO
```

### 5️⃣ انتخاب Port

```text
Tools
 └── Port
      └── Arduino UNO
```

### 6️⃣ Upload

برنامه را روی Arduino آپلود کنید.

پس از اتمام Upload، موتور، درایور و منبع تغذیه را مطابق مشخصات سخت‌افزار متصل کنید.

---

## 📂 ساختار پروژه

```text
setpper-motor/
│
├── 📁 STP-MOTOR/
│   └── فایل‌های مربوط به Stepper Motor
│
├── 📁 UNO/
│   └── کدهای Arduino UNO
│
├── 📁 Panel - telegram/
│   ├── فایل‌های پنل Telegram
│   └── robot_banner.jpg
│
├── 🎥 اجرا.mp4
│
└── 📄 README.md
```

---

## 📱 پنل Telegram

در Repository یک پوشه با نام:

```text
Panel - telegram/
```

وجود دارد که فایل‌های مربوط به بخش Telegram پروژه در آن قرار گرفته‌اند.

تصویر معرفی این بخش نیز در همین پوشه قرار دارد:

```text
Panel - telegram/robot_banner.jpg
```

---

## 🤖 کاربردهای پروژه

مفاهیم این پروژه را می‌توان در پروژه‌های مختلف استفاده کرد.

### 🤖 رباتیک

* بازوی رباتیک
* چرخ‌ها
* Linear Actuator
* پلتفرم‌های چرخان
* سیستم‌های Positioning

### 🏭 اتوماسیون صنعتی

موتورهای پله‌ای برای کنترل دقیق موقعیت در بسیاری از سیستم‌های مکانیکی استفاده می‌شوند.

### 🖨️ پرینتر سه‌بعدی

در پرینترهای سه‌بعدی معمولاً موتورهای Stepper برای کنترل موارد زیر استفاده می‌شوند:

```text
X Axis
Y Axis
Z Axis
Extruder
```

### ⚙️ CNC

Stepper Motorها می‌توانند برای کنترل محورهای دستگاه‌های CNC استفاده شوند.

### 📷 سیستم‌های دوربین

برای مواردی مانند:

* حرکت دوربین
* Pan / Tilt
* سیستم Focus
* پلتفرم چرخان

نیز قابل استفاده هستند.

---

## 🔮 ایده‌های توسعه

پروژه را می‌توان با امکانات زیر توسعه داد:

* 🎛️ کنترل سرعت
* 🎚️ کنترل با Potentiometer
* 🎮 کنترل با Joystick
* 📱 کنترل با Bluetooth
* 📡 کنترل بی‌سیم
* 🖥️ نمایش اطلاعات روی LCD / OLED
* 🎯 Position Tracking
* 🛑 Emergency Stop
* 📈 Acceleration / Deceleration
* 🔄 تغییر جهت خودکار
* 🌐 کنترل تحت وب
* 🤖 اتصال به سیستم‌های رباتیک

معماری احتمالی نسخه پیشرفته:

```text
                    Controller
                        │
          ┌─────────────┼─────────────┐
          │             │             │
          ▼             ▼             ▼
      🎮 Joystick   🖥️ Display    📡 Wireless
          │             │             │
          └─────────────┼─────────────┘
                        │
                        ▼
                 ┌──────────────┐
                 │ Motor Driver │
                 └──────┬───────┘
                        │
                        ▼
                 ⚙️ Stepper Motor
```

---

## ⚠️ نکات ایمنی

هنگام کار با سخت‌افزار موارد زیر را رعایت کنید:

* ⚠️ **موتور پله‌ای را مستقیماً به پایه‌های Arduino متصل نکنید.**
* ⚠️ حتماً از Motor Driver مناسب استفاده کنید.
* ⚠️ از منبع تغذیه مناسب استفاده کنید.
* ⚠️ جریان Motor Driver را مطابق مشخصات موتور تنظیم کنید.
* ⚠️ قبل از روشن کردن سیستم سیم‌کشی را بررسی کنید.
* ⚠️ قبل از تغییر سیم‌ها برق را قطع کنید.
* ⚠️ اتصال GND مشترک موردنیاز را رعایت کنید.
* ⚠️ دستورالعمل سازنده Motor Driver را مطالعه کنید.

---

## 📚 چیزهایی که از این پروژه یاد می‌گیرید

این پروژه یک نمونه عملی برای یادگیری موارد زیر است:

```text
Arduino Programming
        │
        ▼
      C / C++
        │
        ▼
   Digital Signals
        │
        ▼
   Control Pulses
        │
        ▼
    Motor Driver
        │
        ▼
   Stepper Motor
        │
        ▼
  Motion Control
        │
        ▼
 Robotics & Automation
```

### مباحث اصلی

* سیستم‌های Embedded
* برنامه‌نویسی Arduino
* C / C++
* الکترونیک دیجیتال
* کنترل موتور
* ارتباط سخت‌افزار و نرم‌افزار
* رباتیک
* اتوماسیون
* کنترل حرکت

---

## 👨‍💻 سازنده

<p align="center">

<strong>ho3-win</strong>

<br><br>

<a href="https://github.com/ho3-win">
  <img src="https://img.shields.io/badge/GitHub-ho3--win-black?style=for-the-badge&logo=github">
</a>

</p>

⭐ اگر این پروژه برای شما مفید بود، خوشحال می‌شوم Repository را **Star ⭐** کنید.

---

<p align="center">

## ⚙️ Arduino • Stepper Motor • Robotics • Embedded Systems

### 🚀 Built for learning, experimenting and creating

**ساخته شده برای یادگیری، آزمایش و خلق ایده‌های جدید**

</p>

---

<p align="center">
  <a href="#-english">🇬🇧 English</a>
  &nbsp;&nbsp;•&nbsp;&nbsp;
  <a href="#-فارسی">🇮🇷 فارسی</a>
</p>
