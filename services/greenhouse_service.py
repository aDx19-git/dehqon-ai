def greenhouse_advice(
    inside_temperature: float,
    inside_humidity: float,
    outside_temperature: float,
    outside_rain_probability: int,
) -> str:

    advice = []

    difference = inside_temperature - outside_temperature

    if inside_temperature >= 35:
        advice.append(
            "🔥 TEPLITSA JUDA ISSIQ\n"
            "💨 Shamollatish va soyalanishni tekshiring."
        )

    elif inside_temperature >= 30:
        advice.append(
            "🌡 TEPLITSA ISSIQ\n"
            "💨 Havo almashinuvini nazorat qiling."
        )

    elif inside_temperature <= 8:
        advice.append(
            "❄️ TEPLITSA SOVUQ\n"
            "🌱 Sovuqqa sezgir ekinlarni himoyalang."
        )

    if inside_humidity >= 85:
        advice.append(
            "💧 NAMLIK JUDA YUQORI\n"
            "💨 Shamollatishni kuchaytirish foydali."
        )

    elif inside_humidity <= 35:
        advice.append(
            "🏜 NAMLIK PAST\n"
            "💧 Ekinlarning namlik holatini tekshiring."
        )

    if difference >= 10:
        advice.append(
            f"🌡 HARORAT FARQI: +{difference:.1f}°C\n"
            "Teplitsa tashqariga nisbatan ancha issiq."
        )

    if outside_rain_probability >= 70:
        advice.append(
            "🌧 TASHQARIDA YOMG‘IR EHTIMOLI YUQORI\n"
            "Shamollatish vaqtini ehtiyotkorlik bilan tanlang."
        )

    if not advice:
        advice.append(
            "✅ TEPLITSA SHAROITI YAXSHI\n"
            "🌱 Harorat va namlik hozircha me’yorida."
        )

    return "\n\n".join(advice)


def format_greenhouse(
    location_name: str,
    outside_temperature: float,
    outside_rain_probability: int,
    inside_temperature: float,
    inside_humidity: float,
) -> str:

    advice = greenhouse_advice(
        inside_temperature=inside_temperature,
        inside_humidity=inside_humidity,
        outside_temperature=outside_temperature,
        outside_rain_probability=outside_rain_probability,
    )

    difference = inside_temperature - outside_temperature

    return (
        f"🌱 TEPLITSA — {location_name.upper()}\n\n"

        f"🌦 TASHQARIDA\n"
        f"🌡 Harorat: {outside_temperature:.1f}°C\n"
        f"🌧 Yomg‘ir ehtimoli: "
        f"{outside_rain_probability}%\n\n"

        f"🌱 TEPLITSA ICHKARISIDA\n"
        f"🌡 Harorat: {inside_temperature:.1f}°C\n"
        f"💧 Namlik: {inside_humidity:.0f}%\n"
        f"📊 Farq: {difference:+.1f}°C\n\n"

        f"🧠 DEHQON AI TAVSIYASI\n\n"
        f"{advice}\n\n"

        f"📌 Ma'lumot:\n"
        f"Ichki harorat va namlik siz kiritgan "
        f"o‘lchovlarga asoslangan."
    )