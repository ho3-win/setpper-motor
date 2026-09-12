"""
لایه ارتباط سریال با آردوینو.
دستورات را می‌فرستد و خط‌های پاسخ را جمع‌آوری می‌کند
(TARGET = ..., "Motor X done", "All motors done", ERROR, WARNING, ...)
"""

import asyncio
import time
import serial  # pyserial

import config


class ArduinoController:
    def __init__(self, port: str = config.SERIAL_PORT, baud: int = config.BAUD_RATE):
        self.port = port
        self.baud = baud
        self._ser: serial.Serial | None = None
        self._lock = asyncio.Lock()

    # ---------- اتصال ----------
    def _connect_sync(self):
        self._ser = serial.Serial(self.port, self.baud, timeout=0.2)
        # به آردوینو زمان بده تا بعد از باز شدن پورت ریست/بوت شود
        time.sleep(2)
        # پاک کردن بافر پیام خوش‌آمدگویی اولیه
        self._ser.reset_input_buffer()

    async def connect(self):
        loop = asyncio.get_running_loop()
        await loop.run_in_executor(None, self._connect_sync)

    def is_connected(self) -> bool:
        return self._ser is not None and self._ser.is_open

    async def close(self):
        if self._ser and self._ser.is_open:
            loop = asyncio.get_running_loop()
            await loop.run_in_executor(None, self._ser.close)

    # ---------- ارسال دستور و خواندن پاسخ ----------
    def _send_sync(self, command: str, read_seconds: float = 1.0) -> list[str]:
        if not self._ser or not self._ser.is_open:
            raise RuntimeError("پورت سریال باز نیست")

        self._ser.reset_input_buffer()
        self._ser.write((command + "\n").encode("utf-8"))
        self._ser.flush()

        lines = []
        deadline = time.time() + read_seconds
        while time.time() < deadline:
            raw = self._ser.readline()
            if raw:
                text = raw.decode("utf-8", errors="ignore").strip()
                if text:
                    lines.append(text)
                    # اگر پیام پایانی رسید زودتر خارج شو
                    if text.endswith("done") or text.startswith("ERROR"):
                        # کمی صبر برای خط‌های احتمالی باقی‌مانده
                        time.sleep(0.1)
                        while self._ser.in_waiting:
                            extra = self._ser.readline().decode("utf-8", errors="ignore").strip()
                            if extra:
                                lines.append(extra)
                        break
        return lines

    async def send_command(self, command: str, read_seconds: float = 1.0) -> list[str]:
        async with self._lock:
            loop = asyncio.get_running_loop()
            return await loop.run_in_executor(
                None, self._send_sync, command, read_seconds
            )
