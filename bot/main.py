import asyncio
import os
from pathlib import Path

from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
)

from services.weather import (
    get_weather,
    format_weather,
)

from services.greenhouse_service import (
    format_greenhouse,
)

from services.crop_service import (
    CROPS,
    format_crop,
)

from services.ai_advisor import (
    get_ai_advice,
)


# =========================================================
# CONFIG
# =========================================================

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_FILE = BASE_DIR / ".env"

# Local kompyuterda .env bo'lsa, uni yuklaydi.
# Railway'da esa Environment Variables ishlaydi.

# BOT_TOKEN:
# 1. Railway Environment Variable'dan oladi
# 2. Agar local bo'lsa .env'dan oladi
load_dotenv(ENV_FILE)

def get_bot_token() -> str:
    token = os.getenv("BOT_TOKEN")

    if not token:
        raise RuntimeError(
            "BOT_TOKEN topilmadi! "
            "Railway Variables yoki local .env faylni tekshiring."
        )

    return token.strip()


BOT_TOKEN: str = get_bot_token()
# =========================================================
# BOT
# =========================================================
dp = Dispatcher()
# =========================================================
# STATES
# =========================================================

class GreenhouseState(StatesGroup):
    waiting_location = State()
    waiting_temperature = State()
    waiting_humidity = State()


class AIState(StatesGroup):
    waiting_question = State()


# =========================================================
# MAIN MENU
# =========================================================

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🌦 Ob-havo"),
            KeyboardButton(text="🌱 Ekinlar"),
        ],
        [
            KeyboardButton(text="🌱 Teplitsa"),
            KeyboardButton(text="🧠 AI maslahati"),
        ],
        [
            KeyboardButton(text="🚨 Ogohlantirishlar"),
            KeyboardButton(text="👤 Profil"),
        ],
        [
            KeyboardButton(text="ℹ️ Dehqon AI haqida"),
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder="Bo‘limni tanlang...",
)


# =========================================================
# REGION KEYBOARD
# =========================================================

regions_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📍 Toshkent"),
            KeyboardButton(text="📍 Andijon"),
        ],
        [
            KeyboardButton(text="📍 Farg‘ona"),
            KeyboardButton(text="📍 Namangan"),
        ],
        [
            KeyboardButton(text="📍 Samarqand"),
            KeyboardButton(text="📍 Buxoro"),
        ],
        [
            KeyboardButton(text="📍 Xorazm"),
            KeyboardButton(text="📍 Navoiy"),
        ],
        [
            KeyboardButton(text="📍 Qashqadaryo"),
            KeyboardButton(text="📍 Surxondaryo"),
        ],
        [
            KeyboardButton(text="📍 Jizzax"),
            KeyboardButton(text="📍 Sirdaryo"),
        ],
        [
            KeyboardButton(text="📍 Qoraqalpog‘iston"),
        ],
        [
            KeyboardButton(text="⬅️ Bosh menyu"),
        ],
    ],
    resize_keyboard=True,
)


# =========================================================
# CROP KEYBOARD
# =========================================================

crop_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🌾 Bug‘doy"),
            KeyboardButton(text="🌽 Makkajo‘xori"),
        ],
        [
            KeyboardButton(text="🍅 Pomidor"),
            KeyboardButton(text="🥒 Bodring"),
        ],
        [
            KeyboardButton(text="🥔 Kartoshka"),
            KeyboardButton(text="🍎 Mevali daraxtlar"),
        ],
        [
            KeyboardButton(text="⬅️ Bosh menyu"),
        ],
    ],
    resize_keyboard=True,
)


# =========================================================
# REGIONS
# =========================================================

REGIONS = {
    "📍 Toshkent": (
        "Toshkent",
        41.2995,
        69.2401,
    ),

    "📍 Andijon": (
        "Andijon",
        40.7821,
        72.3442,
    ),

    "📍 Farg‘ona": (
        "Farg‘ona",
        40.3864,
        71.7864,
    ),

    "📍 Namangan": (
        "Namangan",
        41.0011,
        71.6683,
    ),

    "📍 Samarqand": (
        "Samarqand",
        39.6542,
        66.9597,
    ),

    "📍 Buxoro": (
        "Buxoro",
        39.7747,
        64.4286,
    ),

    "📍 Xorazm": (
        "Xorazm",
        41.5500,
        60.6333,
    ),

    "📍 Navoiy": (
        "Navoiy",
        40.0844,
        65.3792,
    ),

    "📍 Qashqadaryo": (
        "Qashqadaryo",
        38.8606,
        65.7891,
    ),

    "📍 Surxondaryo": (
        "Surxondaryo",
        37.9400,
        67.5700,
    ),

    "📍 Jizzax": (
        "Jizzax",
        40.1158,
        67.8422,
    ),

    "📍 Sirdaryo": (
        "Sirdaryo",
        40.8363,
        68.6617,
    ),

    "📍 Qoraqalpog‘iston": (
        "Qoraqalpog‘iston",
        42.4600,
        59.6100,
    ),
}


# =========================================================
# START
# =========================================================

@dp.message(CommandStart())
async def start_handler(message: Message, state: FSMContext):

    await state.clear()

    await message.answer(
        "🌾 DEHQON AI\n\n"
        "🇺🇿 O‘zbekiston dehqonlari uchun "
        "aqlli yordamchi.\n\n"

        "🌦 Real ob-havo\n"
        "🌱 Ekinlar\n"
        "🌱 Teplitsa\n"
        "🧠 AI maslahatlar\n"
        "🚨 Ogohlantirishlar\n\n"

        "👇 Kerakli bo‘limni tanlang:",
        reply_markup=main_keyboard,
    )


# =========================================================
# WEATHER MENU
# =========================================================

@dp.message(F.text == "🌦 Ob-havo")
async def weather_menu(
    message: Message,
    state: FSMContext,
):

    await state.clear()

    await message.answer(
        "🌦 OB-HAVO\n\n"
        "📍 Hududingizni tanlang:",
        reply_markup=regions_keyboard,
    )


# =========================================================
# GREENHOUSE MENU
# =========================================================

@dp.message(F.text == "🌱 Teplitsa")
async def greenhouse_menu(
    message: Message,
    state: FSMContext,
):

    await state.clear()

    await state.set_state(
        GreenhouseState.waiting_location
    )

    await message.answer(
        "🌱 TEPLITSA\n\n"
        "Teplitsa qaysi hududda joylashgan?\n\n"
        "📍 Viloyatingizni tanlang:",
        reply_markup=regions_keyboard,
    )


# =========================================================
# REGION HANDLER
# =========================================================

@dp.message(F.text.in_(REGIONS.keys()))
async def region_handler(
    message: Message,
    state: FSMContext,
):

    current_state = await state.get_state()

    # -----------------------------------------------------
    # GREENHOUSE MODE
    # -----------------------------------------------------

    if current_state == GreenhouseState.waiting_location.state:

        name, latitude, longitude = REGIONS[message.text]

        await state.update_data(
            location_name=name,
            latitude=latitude,
            longitude=longitude,
        )

        await state.set_state(
            GreenhouseState.waiting_temperature
        )

        await message.answer(
            f"📍 Hudud: {name}\n\n"

            "🌡 Teplitsa ichidagi "
            "hozirgi haroratni kiriting.\n\n"

            "Masalan:\n"
            "28\n"
            "yoki\n"
            "28.5\n\n"

            "°C da kiriting:"
        )

        return

    # -----------------------------------------------------
    # NORMAL WEATHER MODE
    # -----------------------------------------------------

    name, latitude, longitude = REGIONS[message.text]

    await message.answer(
        f"⏳ {name} uchun real ob-havo "
        "olinmoqda..."
    )

    try:

        data = await get_weather(
            latitude=latitude,
            longitude=longitude,
        )

        result = format_weather(
            data=data,
            location_name=name,
        )

        await message.answer(
            result,
            reply_markup=regions_keyboard,
        )

    except Exception as error:

        print("WEATHER ERROR:", error)

        await message.answer(
            "❌ Ob-havo ma’lumotlarini olishda "
            "xatolik yuz berdi.\n\n"
            "Birozdan keyin qayta urinib ko‘ring.",
            reply_markup=regions_keyboard,
        )


# =========================================================
# GREENHOUSE TEMPERATURE
# =========================================================

@dp.message(GreenhouseState.waiting_temperature)
async def greenhouse_temperature_handler(
    message: Message,
    state: FSMContext,
):

    text = message.text or ""

    try:

        temperature = float(
            text.replace(",", ".")
        )

    except ValueError:

        await message.answer(
            "❌ Haroratni faqat raqam bilan kiriting.\n\n"
            "Masalan: 28 yoki 28.5"
        )

        return

    if temperature < -30 or temperature > 70:

        await message.answer(
            "⚠️ Harorat noto‘g‘ri ko‘rinmoqda.\n\n"
            "Iltimos, teplitsa ichidagi real "
            "haroratni kiriting."
        )

        return

    await state.update_data(
        inside_temperature=temperature
    )

    await state.set_state(
        GreenhouseState.waiting_humidity
    )

    await message.answer(
        f"🌡 Ichki harorat: {temperature:.1f}°C\n\n"

        "💧 Endi teplitsa ichidagi "
        "namlikni kiriting.\n\n"

        "Masalan:\n"
        "70\n"
        "yoki\n"
        "78.5\n\n"

        "Foiz (%) ko‘rinishida:"
    )


# =========================================================
# GREENHOUSE HUMIDITY
# =========================================================

@dp.message(GreenhouseState.waiting_humidity)
async def greenhouse_humidity_handler(
    message: Message,
    state: FSMContext,
):

    text = message.text or ""

    try:

        humidity = float(
            text.replace(",", ".")
        )

    except ValueError:

        await message.answer(
            "❌ Namlikni faqat raqam bilan kiriting.\n\n"
            "Masalan: 70"
        )

        return

    if humidity < 0 or humidity > 100:

        await message.answer(
            "⚠️ Namlik 0% dan 100% gacha "
            "bo‘lishi kerak."
        )

        return

    data = await state.get_data()

    location_name = data["location_name"]
    latitude = data["latitude"]
    longitude = data["longitude"]
    inside_temperature = data["inside_temperature"]

    await message.answer(
        "⏳ Tashqi real ob-havo olinmoqda...\n"
        "🧠 Teplitsa sharoiti tahlil qilinmoqda..."
    )

    try:

        weather = await get_weather(
            latitude=latitude,
            longitude=longitude,
        )

        outside_temperature = weather[
            "current"
        ]["temperature_2m"]

        rain_probability = weather[
            "daily"
        ]["precipitation_probability_max"][0]

        result = format_greenhouse(
            location_name=location_name,
            outside_temperature=outside_temperature,
            outside_rain_probability=rain_probability,
            inside_temperature=inside_temperature,
            inside_humidity=humidity,
        )

        await message.answer(
            result,
            reply_markup=main_keyboard,
        )

    except Exception as error:

        print("GREENHOUSE ERROR:", error)

        await message.answer(
            "❌ Teplitsa ma’lumotlarini "
            "olishda xatolik yuz berdi.\n\n"
            "Birozdan keyin qayta urinib ko‘ring.",
            reply_markup=main_keyboard,
        )

    finally:

        await state.clear()


# =========================================================
# CROPS MENU
# =========================================================

@dp.message(F.text == "🌱 Ekinlar")
async def crops_handler(
    message: Message,
    state: FSMContext,
):

    await state.clear()

    await message.answer(
        "🌱 EKINLAR\n\n"
        "Qaysi ekin haqida ma’lumot kerak?\n\n"
        "👇 Ekinni tanlang:",
        reply_markup=crop_keyboard,
    )


# =========================================================
# CROP SELECTED
# =========================================================

@dp.message(F.text.in_(CROPS.keys()))
async def crop_selected_handler(
    message: Message,
    state: FSMContext,
):

    await state.clear()

    crop_key = message.text

    if not crop_key:
        await message.answer(
            "❌ Ekin nomi aniqlanmadi. Iltimos, ekinni menyudan tanlang.",
            reply_markup=crop_keyboard,
        )
        return

    crop_key = crop_key.strip()

    await message.answer(
        "⏳ Bugungi real ob-havo olinmoqda...\n"
        "🧠 Ekin uchun tavsiya tayyorlanmoqda..."
    )

    # Hozircha Namangan.
    # Keyingi bosqichda foydalanuvchining
    # tanlagan hududini profilga saqlaymiz.

    latitude = 41.0011
    longitude = 71.6683

    try:

        weather = await get_weather(
            latitude=latitude,
            longitude=longitude,
        )

        temperature = weather[
            "current"
        ]["temperature_2m"]

        rain_probability = weather[
            "daily"
        ]["precipitation_probability_max"][0]

        result = format_crop(
            crop_key=crop_key,
            temperature=temperature,
            rain_probability=rain_probability,
        )

        await message.answer(
            result,
            reply_markup=crop_keyboard,
        )

    except Exception as error:

        print("CROP ERROR:", error)

        await message.answer(
            "❌ Ekin ma’lumotlarini olishda "
            "xatolik yuz berdi.",
            reply_markup=crop_keyboard,
        )


# =========================================================
# AI MENU
# =========================================================

@dp.message(F.text == "🧠 AI maslahati")
async def ai_handler(
    message: Message,
    state: FSMContext,
):

    await state.clear()

    await state.set_state(
        AIState.waiting_question
    )

    await message.answer(
        "🧠 DEHQON AI MASLAHATCHISI\n\n"

        "Dehqonchilik bo‘yicha "
        "savolingizni yozing. 🌱\n\n"

        "Masalan:\n"
        "💬 Pomidorni qachon sug‘orish kerak?\n"
        "💬 Ekinimga qancha suv kerak?\n"
        "💬 Yomg‘ir oldidan nima qilish kerak?\n"
        "💬 Teplitsani qachon shamollatish kerak?\n\n"

        "✍️ Savolingizni yozing:"
    )


# =========================================================
# AI QUESTION
# =========================================================

@dp.message(AIState.waiting_question)
async def ai_question_handler(
    message: Message,
    state: FSMContext,
):
    question = (message.text or "").strip()

    if not question:
        await message.answer(
            "✍️ Savolingizni yozing."
        )
        return

    # Bitta xabar yaratamiz
    processing_message = await message.answer(
        "🧠 Savolingiz tahlil qilinmoqda..."
    )

    try:
        answer = get_ai_advice(question)

        # O‘sha xabarni javobga almashtiramiz
        await processing_message.edit_text(
            answer
        )

    except Exception as error:
        print("AI ERROR:", error)

        await processing_message.edit_text(
            "❌ Maslahat tayyorlashda "
            "xatolik yuz berdi."
        )

    finally:
        await state.clear()

# =========================================================
# ALERTS
# =========================================================

@dp.message(F.text == "🚨 Ogohlantirishlar")
async def alerts_handler(
    message: Message,
    state: FSMContext,
):

    await state.clear()

    await message.answer(
        "🚨 OGOHLANTIRISHLAR\n\n"

        "🌧 Kuchli yomg‘ir\n"
        "💨 Kuchli shamol\n"
        "❄️ Sovuq\n"
        "🔥 Kuchli issiq\n"
        "⛈ Momaqaldiroq\n\n"

        "📡 Avtomatik ogohlantirish tizimi "
        "keyingi bosqichda ulanadi.",

        reply_markup=main_keyboard,
    )


# =========================================================
# PROFILE
# =========================================================

@dp.message(F.text == "👤 Profil")
async def profile_handler(
    message: Message,
    state: FSMContext,
):

    await state.clear()

    user = message.from_user

    if user is None:
        return

    await message.answer(
        "👤 MENING PROFILIM\n\n"

        f"👨‍🌾 Ism: {user.first_name}\n"
        f"🆔 Telegram ID: {user.id}\n\n"

        "📍 Hudud: Belgilanmagan\n"
        "🌱 Ekin: Belgilanmagan\n"
        "🌱 Teplitsa: Belgilanmagan",

        reply_markup=main_keyboard,
    )


# =========================================================
# ABOUT
# =========================================================

@dp.message(F.text == "ℹ️ Dehqon AI haqida")
async def about_handler(
    message: Message,
    state: FSMContext,
):

    await state.clear()

    await message.answer(
        "🌾 DEHQON AI\n\n"

        "🇺🇿 O‘zbekiston dehqonlari uchun "
        "aqlli yordamchi.\n\n"

        "🌦 Real ob-havo\n"
        "🌱 Ekinlar\n"
        "🌱 Teplitsa\n"
        "🧠 AI maslahatlar\n"
        "🚨 Ogohlantirishlar\n\n"

        "🚀 Loyiha rivojlantirilmoqda.",

        reply_markup=main_keyboard,
    )


# =========================================================
# BACK TO MENU
# =========================================================

@dp.message(F.text == "⬅️ Bosh menyu")
async def back_handler(
    message: Message,
    state: FSMContext,
):

    await state.clear()

    await message.answer(
        "🌾 Bosh menyu",
        reply_markup=main_keyboard,
    )


# =========================================================
# UNKNOWN MESSAGE
# =========================================================

@dp.message()
async def unknown_handler(
    message: Message,
    state: FSMContext,
):

    await state.clear()

    await message.answer(
        "🤔 Bu buyruqni tushunmadim.\n\n"
        "👇 Menyudan bo‘lim tanlang.",
        reply_markup=main_keyboard,
    )


# =========================================================
# RUN BOT
# =========================================================

async def main():

    print("===================================")
    print("🌾 DEHQON AI ISHGA TUSHDI!")
    print("🌦 REAL WEATHER READY!")
    print("🌱 GREENHOUSE SYSTEM READY!")
    print("🌾 CROPS SYSTEM READY!")
    print("🧠 AI ADVISOR READY!")
    print("===================================")

    async with Bot(token=BOT_TOKEN) as polling_bot:
        await dp.start_polling(polling_bot)


if __name__ == "__main__":
    asyncio.run(main())