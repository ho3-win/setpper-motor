import logging
import os

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.constants import ParseMode
from telegram.error import BadRequest
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)






import config
from serial_controller import ArduinoController

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

NUM_MOTORS = 4

ANGLES = [45, 90, 135, 180]



MOTOR_LABEL = {"1": "1️⃣", "2": "2️⃣", "3": "3️⃣", "4": "4️⃣"}
ICON_ALL = "🎛"
ICON_STATUS = "📍"
ICON_RESET = "↺"
ICON_TERMINAL = "⌨️"
ICON_BACK = "🔙"
ICON_LEFT = "▶️"
ICON_RIGHT = "◀️"
ICON_DEV = "👨‍💻" # آیکون دکمه توسعه‌دهنده
ICON_LED_ON = "🟢"
ICON_LED_OFF = "🔴"

BANNER_PATH = os.path.join(os.path.dirname(__file__), config.BANNER_IMAGE_PATH)
MAIN_CAPTION = (
    "🤖 <b>کنترل‌گر ربات چهارموتوره</b>\n\n"
    "هر موتور رو جدا یا همه رو با هم بچرخون، وضعیت رو ببین، ریست کن یا از "
    "ترمینال برای فرستادن هر دستور دلخواه استفاده کن."
)



arduino = ArduinoController()


def is_allowed(user_id: int) -> bool:
    return not config.ALLOWED_USER_IDS or user_id in config.ALLOWED_USER_IDS



def main_menu_keyboard(context: ContextTypes.DEFAULT_TYPE = None) -> InlineKeyboardMarkup:
 
    is_led_on = context.chat_data.get("led_state", False) if context else False
    led_button_text = f"{ICON_LED_ON} چراغ روشن است" if is_led_on else f"{ICON_LED_OFF} چراغ خاموش است"
    
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(f"{MOTOR_LABEL['1']} موتور ۱", callback_data="MENU:M:1"),
            InlineKeyboardButton(f"{MOTOR_LABEL['2']} موتور ۲", callback_data="MENU:M:2"),
        ],
        [
            InlineKeyboardButton(f"{MOTOR_LABEL['3']} موتور ۳", callback_data="MENU:M:3"),
            InlineKeyboardButton(f"{MOTOR_LABEL['4']} موتور ۴", callback_data="MENU:M:4"),
        ],
        [InlineKeyboardButton(f"{ICON_ALL} کنترل همه موتورها", callback_data="MENU:ALL")],
        [
            InlineKeyboardButton(f"{ICON_STATUS} وضعیت", callback_data="CMD:STATUS"),
            InlineKeyboardButton(f"{ICON_RESET} ریست به صفر", callback_data="CMD:RESET"),
        ],
        [
            InlineKeyboardButton(led_button_text, callback_data="LED:TOGGLE"),
        ],
        [
            InlineKeyboardButton(f"{ICON_TERMINAL} ترمینال", callback_data="TERM:OPEN"),
            InlineKeyboardButton(f"{ICON_DEV}  توسعه‌دهندگان", callback_data="MENU:DEV")
        ],
    ])


def motor_menu_keyboard(motor_idx: str) -> InlineKeyboardMarkup:
    left = [InlineKeyboardButton(f"{ICON_LEFT} {a}°", callback_data=f"MV:{motor_idx}:L:{a}") for a in ANGLES]
    right = [InlineKeyboardButton(f"{a}° {ICON_RIGHT}", callback_data=f"MV:{motor_idx}:R:{a}") for a in ANGLES]
    rows = [left, right]
    if motor_idx != "ALL":
        rows.append([InlineKeyboardButton(f"{ICON_STATUS} وضعیت این موتور", callback_data="CMD:STATUS")])
    rows.append([InlineKeyboardButton(f"{ICON_BACK} بازگشت به منو", callback_data="MENU:MAIN")])
    return InlineKeyboardMarkup(rows)


def terminal_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([[InlineKeyboardButton(f"{ICON_BACK} خروج از ترمینال", callback_data="TERM:CLOSE")]])


def dev_menu_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([[InlineKeyboardButton(f"{ICON_BACK} بازگشت به منو", callback_data="MENU:MAIN")]])


def motor_title(motor_idx: str) -> str:
    if motor_idx == "ALL":
        return f"{ICON_ALL} کنترل همه موتورها"
    return f"{MOTOR_LABEL.get(motor_idx, '')} موتور {motor_idx}"


async def render(context: ContextTypes.DEFAULT_TYPE, chat_id: int, text: str, keyboard: InlineKeyboardMarkup):
    anchor_id = context.chat_data.get("anchor_id")

    if anchor_id is not None:
        try:
            await context.bot.edit_message_caption(
                chat_id=chat_id, message_id=anchor_id,
                caption=text, parse_mode=ParseMode.HTML, reply_markup=keyboard,
            )
            return
        except BadRequest as e:
            if "not modified" in str(e).lower():
                return
            logger.warning("Anchor edit failed (%s), sending a fresh one", e)

    await _send_fresh_anchor(context, chat_id, text, keyboard)


async def _send_fresh_anchor(context: ContextTypes.DEFAULT_TYPE, chat_id: int, text: str, keyboard: InlineKeyboardMarkup):
    if os.path.exists(BANNER_PATH):
        with open(BANNER_PATH, "rb") as photo:
            msg = await context.bot.send_photo(
                chat_id=chat_id, photo=photo, caption=text,
                parse_mode=ParseMode.HTML, reply_markup=keyboard,
            )
    else:
        msg = await context.bot.send_message(
            chat_id=chat_id, text=text, parse_mode=ParseMode.HTML, reply_markup=keyboard
        )
    context.chat_data["anchor_id"] = msg.message_id



async def run_arduino_command(command: str) -> str:
    if not arduino.is_connected():
        try:
            await arduino.connect()
        except Exception as e:
            return f"❌ پورت سریال باز نشد ({config.SERIAL_PORT}):\n{e}"

    try:
        lines = await arduino.send_command(command)
    except Exception as e:
        return f"❌ خطا هنگام ارسال دستور:\n{e}"

    return "\n".join(lines) if lines else "⚠️ پاسخی از آردوینو دریافت نشد."



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_allowed(update.effective_user.id):
        await update.message.reply_text("⛔️ شما اجازه استفاده از این ربات را ندارید.")
        return
    context.chat_data["awaiting_terminal"] = False
    context.chat_data["led_state"] = False  # حالت اولیه: خاموش
    context.chat_data.pop("anchor_id", None)
    await render(context, update.effective_chat.id, MAIN_CAPTION, main_menu_keyboard(context))


async def connect_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_allowed(update.effective_user.id):
        return
    try:
        await arduino.connect()
        await update.message.reply_text(f"✅ اتصال سریال به {config.SERIAL_PORT} برقرار شد.")
    except Exception as e:
        await update.message.reply_text(f"❌ خطا در اتصال سریال:\n{e}")


async def on_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if not is_allowed(query.from_user.id):
        await query.answer("⛔️ اجازه ندارید", show_alert=True)
        return

    chat_id = query.message.chat_id
    context.chat_data["anchor_id"] = query.message.message_id

    action, *rest = query.data.split(":")

 
    if action == "LED":
        if rest[0] == "TOGGLE":
      
            current_state = context.chat_data.get("led_state", False)
            new_state = not current_state
            
    
            command = "LED_ON" if new_state else "LED_OFF"
            await query.answer(f"در حال اجرا: {command}")
            result = await run_arduino_command(command)
            
     
            context.chat_data["led_state"] = new_state
            
   
            status_text = "چراغ روشن است ✅" if new_state else "چراغ خاموش است"
            text = f"💡 <code>{command}</code>\n\n{status_text}\n\n{result}"
            await render(context, chat_id, text, main_menu_keyboard(context))
        return

    if action == "MENU":
        context.chat_data["awaiting_terminal"] = False
        target = rest[0]
        if target == "MAIN":
            await render(context, chat_id, MAIN_CAPTION, main_menu_keyboard(context))
        elif target == "M":
            motor_idx = rest[1]
            text = f"{motor_title(motor_idx)}\n\nزاویه و جهت چرخش رو انتخاب کن:"
            await render(context, chat_id, text, motor_menu_keyboard(motor_idx))
        elif target == "ALL":
            text = f"{motor_title('ALL')}\n\nزاویه و جهت چرخش رو انتخاب کن:"
            await render(context, chat_id, text, motor_menu_keyboard("ALL"))
        elif target == "DEV":
            dev_text = (
                f"{ICON_DEV} <b>درباره پروژه و توسعه‌دهندگان</b>\n\n"
                f"📌 <b>نام پروژه:</b> سامانه مدیریت خانه هوشمند\n\n"
                f"👨‍🏫 <b>استاد راهنما:</b>\n"
                f"• جناب آقای دکتر کیانی\n\n"
                f"👨‍💻 <b>توسعه‌دهندگان:</b>\n"
                f"• حسین شیخی\n"
                f"• امیرحسین ایمانی‌فرد\n\n"
                f"📝 <i>این ربات جهت کنترل اجزای سخت‌افزاری و شبیه‌سازی سیستم‌های هوشمند، به عنوان پروژه دانشگاهی طراحی و پیاده‌سازی شده است.</i>"
            )
            await render(context, chat_id, dev_text, dev_menu_keyboard())
        return 

    if action == "MV":
        motor_idx, direction, angle = rest
        command = f"ALL_{direction}_{angle}" if motor_idx == "ALL" else f"M{motor_idx}_{direction}_{angle}"
        await query.answer(f"در حال اجرا: {command}")
        result = await run_arduino_command(command)
        text = f"{motor_title(motor_idx)}\n\n⚙️ <code>{command}</code>\n\n{result}"
        await render(context, chat_id, text, motor_menu_keyboard(motor_idx))
        return

    if action == "CMD":
        command = rest[0]
        icon = ICON_STATUS if command == "STATUS" else ICON_RESET
        await query.answer(f"در حال اجرا: {command}")
        result = await run_arduino_command(command)
        text = f"{icon} <code>{command}</code>\n\n{result}"
        await render(context, chat_id, text, main_menu_keyboard(context))
        return

    if action == "TERM":
        if rest[0] == "OPEN":
            context.chat_data["awaiting_terminal"] = True
            text = (
                f"{ICON_TERMINAL} <b>حالت ترمینال</b>\n\n"
                "هر دستوری بفرستی مستقیم به آردوینو می‌ره (مثلاً <code>M1_R_90</code> یا "
                "<code>ALL_HOME</code>). پیام‌های خودت خودکار پاک می‌شن."
            )
            await render(context, chat_id, text, terminal_keyboard())
        elif rest[0] == "CLOSE":
            context.chat_data["awaiting_terminal"] = False
            await render(context, chat_id, MAIN_CAPTION, main_menu_keyboard(context))
        return


async def on_terminal_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return
    if not is_allowed(update.effective_user.id):
        return
    if not context.chat_data.get("awaiting_terminal"):
        return

    command = update.message.text.strip()
    try:
        await update.message.delete()
    except Exception:
        pass

    result = await run_arduino_command(command)
    text = (
        f"{ICON_TERMINAL} <b>حالت ترمینال</b>\n\n"
        f"⚙️ <code>{command}</code>\n\n{result}\n\n"
        "دستور بعدی رو بفرست، یا خارج شو."
    )
    await render(context, update.effective_chat.id, text, terminal_keyboard())


def main():
    app = Application.builder().token(config.BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("connect", connect_cmd))
    app.add_handler(CallbackQueryHandler(on_button))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, on_terminal_text))

    app.run_polling()


if __name__ == "__main__":
    main()