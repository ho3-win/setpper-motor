# ⚙️ Stepper Motor Control System

<p align="center">
  <img src="https://img.shields.io/badge/Arduino-UNO-00979D?style=for-the-badge&logo=arduino&logoColor=white">
  <img src="https://img.shields.io/badge/Stepper%20Motor-Control-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/Telegram-Control-26A5E4?style=for-the-badge&logo=telegram&logoColor=white">
  <img src="https://img.shields.io/badge/C%2B%2B-Arduino-blue?style=for-the-badge&logo=cplusplus&logoColor=white">
  <img src="https://img.shields.io/badge/Embedded-System-green?style=for-the-badge">
</p>

<p align="center">
  <strong>Remote Stepper Motor Control via Telegram & Arduino</strong>
  <br>
  کنترل از راه دور موتورهای پله‌ای با Telegram و Arduino
</p>

<p align="center">
  <a href="#-english">🇬🇧 English</a>
  &nbsp;&nbsp;•&nbsp;&nbsp;
  <a href="#-فارسی">🇮🇷 فارسی</a>
</p>

---

## 🎬 Project Demo

<p align="center">
  <a href="./demo.gif">
    <img src="./Panel%20-%20telegram/robot_banner.jpg" width="750" alt="Stepper Motor Control System">
  </a>
</p>

<p align="center">
  👆 <strong>Click the image to watch the project demo</strong>
  <br>
  برای مشاهده اجرای پروژه روی تصویر کلیک کنید
</p>

---

# 🇬🇧 English

## 📌 About The Project

This project is a **remote Stepper Motor Control System** built around **Arduino UNO and a Telegram Bot**.

The main idea is to control one or more stepper motors remotely using commands sent through Telegram.

Instead of controlling the motors directly using physical buttons or switches, the user interacts with a **Telegram Bot**. The bot receives commands and passes the required control instructions to the motor-control system.

The system can be used as a foundation for remote-controlled robotic and automation systems.

### 🎯 Main Concept

```text
        📱 User
           │
           │ Telegram Commands
           ▼
    🤖 Telegram Bot
           │
           │ Motor Commands
           ▼
    🧠 Control System
           │
           │ STEP / DIR
           ▼
    🔌 Motor Driver
           │
           ▼
    ⚙️ Stepper Motor
           │
           ▼
       Movement
```

This creates a simple bridge between:

```text
Telegram
   ↓
Software Control
   ↓
Embedded System
   ↓
Motor Driver
   ↓
Stepper Motor
```

---

## 🤖 Telegram Motor Control

The Telegram Bot acts as the **remote control interface** for the motors.

Depending on the implemented commands, the user can send instructions such as:

```text
▶️ Start Motor
⏹️ Stop Motor
⬆️ Move Forward
⬇️ Move Backward
◀️ Rotate Left
▶️ Rotate Right
🎯 Move a Specific Number of Steps
⚡ Change Speed
```

The exact commands and available controls depend on the Telegram panel implementation.

This approach makes it possible to control the motor system remotely without requiring direct physical access to the controller.

---

## ⚙️ System Architecture

```text
                         📱 Telegram
                              │
                              │
                              ▼
                    ┌──────────────────┐
                    │  Telegram Bot    │
                    │  Control Panel   │
                    └────────┬─────────┘
                             │
                       Motor Commands
                             │
                             ▼
                    ┌──────────────────┐
                    │ Control / Server │
                    └────────┬─────────┘
                             │
                        Control Data
                             │
                             ▼
                    ┌──────────────────┐
                    │   Arduino UNO    │
                    └────────┬─────────┘
                             │
                       STEP / DIR / ENA
                             │
                             ▼
                    ┌──────────────────┐
                    │   Motor Driver   │
                    └────────┬─────────┘
                             │
                    ┌────────┴────────┐
                    ▼                 ▼
              ⚙️ Stepper 1      ⚙️ Stepper 2
```

The architecture can be expanded to support multiple motors and more advanced automation logic.

---

## 🔧 Motor Control

For a typical STEP/DIR motor driver:

```text
STEP → Movement
DIR  → Direction
ENA  → Enable / Disable
GND  → Common Ground
```

The Arduino generates the required control pulses.

For example:

```text
More STEP pulses
       ↓
More motor movement
```

and:

```text
DIR = Direction A
       ↓
Motor rotates one way

DIR = Direction B
       ↓
Motor rotates the opposite way
```

---

## 🧠 Stepper Motor

A stepper motor moves in discrete steps.

For a motor with a step angle of **1.8°**:

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

If the motor driver supports microstepping, the resolution can be increased:

```text
Full Step
Half Step
1/4 Step
1/8 Step
1/16 Step
...
```

---

## 🔌 Hardware

| Component           | Role                               |
| ------------------- | ---------------------------------- |
| 🔵 Arduino UNO      | Main controller                    |
| ⚙️ Stepper Motor(s) | Mechanical movement                |
| 🔌 Motor Driver     | Motor control and current handling |
| 🔋 Power Supply     | Motor power                        |
| 📱 Telegram Bot     | Remote control interface           |
| 🧵 Jumper Wires     | Electrical connections             |
| 🧪 Breadboard       | Optional prototyping               |

> ⚠️ The motor driver and power supply must be compatible with the selected motors.

---

## ✨ Main Features

* 📱 Remote control through Telegram
* 🤖 Telegram-based motor control panel
* ⚙️ Stepper motor control
* 🔄 Direction control
* 🎯 Step-based movement
* ⏹️ Motor start / stop control
* ⚡ Potential speed control
* 🔌 Arduino UNO integration
* 🧠 Embedded control architecture
* 🔧 Expandable for multiple motors
* 🎥 Project demonstration

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
│   ├── Telegram Bot / Panel files
│   └── robot_banner.jpg
│
├── 🎥 اجرا.mp4
│
└── 📄 README.md
```

---

# 🇮🇷 فارسی

## 📌 درباره پروژه

این پروژه یک **سیستم کنترل از راه دور موتورهای پله‌ای** است که با استفاده از **Arduino UNO و ربات Telegram** طراحی شده است.

ایده اصلی پروژه این است که کاربر بتواند بدون دسترسی مستقیم به سخت‌افزار، از طریق ربات تلگرام به موتور یا موتورهای پله‌ای فرمان بدهد.

ربات تلگرام نقش **رابط کاربری و کنترل از راه دور** را دارد و دستورات کاربر را به سیستم کنترل موتور منتقل می‌کند.

---

## 🤖 کنترل موتور با ربات Telegram

در این پروژه کاربر از طریق ربات Telegram می‌تواند فرمان‌های مربوط به موتور را ارسال کند.

برای مثال، بسته به امکانات پیاده‌سازی‌شده در پنل:

```text
▶️ روشن کردن موتور
⏹️ توقف موتور
⬆️ حرکت به جلو
⬇️ حرکت به عقب
◀️ چرخش به چپ
▶️ چرخش به راست
🎯 حرکت به تعداد Step مشخص
⚡ کنترل سرعت
```

دستورات دقیق به نحوه پیاده‌سازی Telegram Panel بستگی دارند.

---

## ⚙️ معماری سیستم

```text
                         📱 کاربر
                            │
                            │ Telegram
                            ▼
                   ┌──────────────────┐
                   │   Telegram Bot   │
                   │    پنل کنترل     │
                   └────────┬─────────┘
                            │
                       فرمان موتور
                            │
                            ▼
                   ┌──────────────────┐
                   │ سیستم کنترل      │
                   └────────┬─────────┘
                            │
                            ▼
                   ┌──────────────────┐
                   │   Arduino UNO    │
                   └────────┬─────────┘
                            │
                       STEP / DIR
                            │
                            ▼
                   ┌──────────────────┐
                   │   Motor Driver   │
                   └────────┬─────────┘
                            │
                    ┌───────┴───────┐
                    ▼               ▼
               ⚙️ موتور ۱       ⚙️ موتور ۲
```

بنابراین پروژه در اصل یک ارتباط بین **Telegram، نرم‌افزار کنترل، Arduino و موتورهای پله‌ای** ایجاد می‌کند.

```text
Telegram
   ↓
فرمان کاربر
   ↓
سیستم کنترل
   ↓
Arduino
   ↓
Motor Driver
   ↓
Stepper Motor
   ↓
حرکت
```

---

## 🎯 هدف پروژه

هدف اصلی پروژه ایجاد یک روش ساده و قابل توسعه برای **کنترل موتورهای پله‌ای از راه دور** است.

این معماری می‌تواند پایه‌ای برای پروژه‌های بزرگ‌تر مانند:

* 🤖 ربات‌های کنترل‌شونده از راه دور
* 🏭 سیستم‌های اتوماسیون
* ⚙️ سیستم‌های Positioning
* 🚪 مکانیزم‌های موتوری
* 🦾 بازوهای رباتیک
* 🎥 سیستم‌های حرکتی دوربین
* 🏠 سیستم‌های هوشمند
* 🌐 تجهیزات کنترل از راه دور

باشد.

---

## 🚀 توسعه‌های آینده

در نسخه‌های بعدی می‌توان امکانات بیشتری اضافه کرد:

* 🎛️ کنترل دقیق سرعت
* 🎯 تعیین تعداد Step
* 📐 تعیین زاویه حرکت
* ⚡ Acceleration / Deceleration
* 🎮 کنترل چند موتور
* 🔄 کنترل هم‌زمان چند موتور
* 🛑 Emergency Stop
* 📊 نمایش وضعیت موتور در Telegram
* 📍 نمایش موقعیت فعلی موتور
* 🔐 سیستم احراز هویت کاربران Telegram
* 👥 پنل مدیریت کاربران
* 📡 کنترل بی‌سیم
* 🌐 اتصال به Web Panel
* 🤖 استفاده در پروژه‌های رباتیک پیشرفته

---

## 🔐 امنیت

از آنجایی که موتور از طریق Telegram کنترل می‌شود، در نسخه‌های عملیاتی باید دسترسی کاربران کنترل شود.

برای مثال:

```text
Telegram User
      │
      ▼
Authentication
      │
      ▼
Authorization
      │
      ├── ❌ Unauthorized
      │
      └── ✅ Authorized
               │
               ▼
         Motor Commands
```

در یک سیستم واقعی، فقط کاربران مجاز باید بتوانند فرمان‌های حرکتی ارسال کنند.

---

## ⚠️ نکات ایمنی

> ⚠️ موتور پله‌ای را مستقیماً به پایه‌های Arduino متصل نکنید.

حتماً از Motor Driver مناسب استفاده کنید و موارد زیر را رعایت کنید:

* 🔌 استفاده از منبع تغذیه مناسب
* ⚙️ تنظیم صحیح جریان Driver
* 🔧 بررسی سیم‌کشی
* 🛑 قطع برق قبل از تغییر سیم‌ها
* ⚠️ استفاده از Emergency Stop در سیستم‌های پرقدرت
* 🔐 محدود کردن دسترسی Telegram به کاربران مجاز

---

## 👨‍💻 Author

<p align="center">

<strong>ho3-win</strong>

<br><br>

<a href="https://github.com/ho3-win">
  <img src="https://img.shields.io/badge/GitHub-ho3--win-black?style=for-the-badge&logo=github">
</a>

</p>

⭐ اگر پروژه برای شما مفید بود، Repository را Star کنید.

---

<p align="center">

### ⚙️ Telegram • Arduino • Stepper Motor • Robotics

**📱 Remote Control • ⚙️ Motion Control • 🤖 Embedded Systems**

<br>

**ساخته شده برای کنترل، یادگیری و توسعه سیستم‌های رباتیک 🚀**

</p>

---

<p align="center">
  <a href="#-english">🇬🇧 English</a>
  &nbsp;&nbsp;•&nbsp;&nbsp;
  <a href="#-فارسی">🇮🇷 فارسی</a>
</p>
