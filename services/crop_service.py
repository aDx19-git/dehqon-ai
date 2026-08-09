CROPS = {
    "🌾 Bug‘doy": {
        "name": "Bug‘doy",
        "icon": "🌾",
        "description": "Donli ekin. Salqinroq va me’yoridagi namlikni yaxshi ko‘radi.",
        "min_temp": 10,
        "max_temp": 25,
        "water": "O‘rtacha",
        "humidity": "50–70%",
    },

    "🌽 Makkajo‘xori": {
        "name": "Makkajo‘xori",
        "icon": "🌽",
        "description": "Issiqsevar ekin. Yetarli namlik va quyoshni talab qiladi.",
        "min_temp": 18,
        "max_temp": 30,
        "water": "Ko‘p",
        "humidity": "60–80%",
    },

    "🍅 Pomidor": {
        "name": "Pomidor",
        "icon": "🍅",
        "description": "Issiqsevar ekin. Harorat va namlikni barqaror saqlash muhim.",
        "min_temp": 18,
        "max_temp": 30,
        "water": "O‘rtacha",
        "humidity": "60–75%",
    },

    "🥒 Bodring": {
        "name": "Bodring",
        "icon": "🥒",
        "description": "Namlikni yaxshi ko‘radi, lekin ortiqcha suv ham zararli.",
        "min_temp": 18,
        "max_temp": 30,
        "water": "Ko‘p",
        "humidity": "65–85%",
    },

    "🥔 Kartoshka": {
        "name": "Kartoshka",
        "icon": "🥔",
        "description": "Mo‘tadil haroratni yaxshi ko‘radi. Haddan tashqari issiqdan zarar ko‘rishi mumkin.",
        "min_temp": 12,
        "max_temp": 25,
        "water": "O‘rtacha",
        "humidity": "60–80%",
    },

    "🍎 Mevali daraxtlar": {
        "name": "Mevali daraxtlar",
        "icon": "🍎",
        "description": "Mevali daraxtlarda harorat, namlik va sovuq xavfini kuzatish muhim.",
        "min_temp": 10,
        "max_temp": 30,
        "water": "O‘rtacha",
        "humidity": "50–75%",
    },
}


def get_crop(crop_key: str) -> dict | None:
    return CROPS.get(crop_key)


def crop_advice(
    crop_key: str,
    temperature: float,
    rain_probability: int,
) -> str:

    crop = get_crop(crop_key)

    if crop is None:
        return "❌ Ekin topilmadi."

    advice = []

    min_temp = crop["min_temp"]
    max_temp = crop["max_temp"]

    # HARORAT
    if temperature < min_temp:
        advice.append(
            f"❄️ Harorat {temperature:.0f}°C.\n"
            f"{crop['name']} uchun havo salqin."
        )

    elif temperature > max_temp:
        advice.append(
            f"🔥 Harorat {temperature:.0f}°C.\n"
            f"{crop['name']} uchun havo issiq."
        )

    else:
        advice.append(
            f"✅ Harorat {temperature:.0f}°C.\n"
            f"{crop['name']} uchun harorat hozircha qulay."
        )

    # YOMG‘IR
    if rain_probability >= 70:
        advice.append(
            f"🌧 Yomg‘ir ehtimoli {rain_probability}%.\n"
            "💧 Sug‘orishni shoshilmasdan rejalashtirish mumkin."
        )

    elif rain_probability <= 20:
        advice.append(
            f"☀️ Yomg‘ir ehtimoli faqat {rain_probability}%.\n"
            "💧 Tuproq namligini tekshiring."
        )

    else:
        advice.append(
            f"🌦 Yomg‘ir ehtimoli {rain_probability}%.\n"
            "🌱 Ekin holatini kuzatib boring."
        )

    # ISSIQ
    if temperature >= 35:
        advice.append(
            "🔥 Kuchli issiq kuzatilmoqda.\n"
            "💧 Sug‘orishni ertalab yoki kechqurun rejalashtirish ma’qul."
        )

    return "\n\n".join(advice)


def format_crop(
    crop_key: str,
    temperature: float,
    rain_probability: int,
) -> str:

    crop = get_crop(crop_key)

    if crop is None:
        return "❌ Ekin topilmadi."

    advice = crop_advice(
        crop_key=crop_key,
        temperature=temperature,
        rain_probability=rain_probability,
    )

    return (
        f"{crop['icon']} {crop['name'].upper()}\n\n"

        f"📖 {crop['description']}\n\n"

        f"🌡 Tavsiya etiladigan harorat: "
        f"{crop['min_temp']}–{crop['max_temp']}°C\n"

        f"💧 Suv talabi: {crop['water']}\n"

        f"💦 Namlik: {crop['humidity']}\n\n"

        f"🌦 HOZIRGI OB-HAVO\n"
        f"🌡 Harorat: {temperature:.0f}°C\n"
        f"🌧 Yomg‘ir ehtimoli: "
        f"{rain_probability}%\n\n"

        f"🧠 DEHQON AI TAVSIYASI\n\n"
        f"{advice}"
    )