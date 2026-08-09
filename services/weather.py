import httpx


WEATHER_URL = "https://api.open-meteo.com/v1/forecast"


WEATHER_CODES = {
    0: "☀️ Ochiq havo",
    1: "🌤 Asosan ochiq",
    2: "⛅ Qisman bulutli",
    3: "☁️ Bulutli",
    45: "🌫 Tuman",
    48: "🌫 Qirovli tuman",
    51: "🌦 Yengil yomg‘ir",
    53: "🌦 O‘rtacha yomg‘ir",
    55: "🌧 Kuchli yomg‘ir",
    61: "🌧 Yengil yomg‘ir",
    63: "🌧 O‘rtacha yomg‘ir",
    65: "🌧 Kuchli yomg‘ir",
    71: "🌨 Yengil qor",
    73: "🌨 O‘rtacha qor",
    75: "❄️ Kuchli qor",
    80: "🌦 Yomg‘ir",
    81: "🌧 Kuchli yomg‘ir",
    82: "⛈ Juda kuchli yomg‘ir",
    95: "⛈ Momaqaldiroq",
    96: "⛈ Do‘l bilan momaqaldiroq",
    99: "⛈ Kuchli do‘l va momaqaldiroq",
}


def weather_description(code: int) -> str:
    return WEATHER_CODES.get(code, "🌤 Noma'lum ob-havo")


async def get_weather(latitude: float, longitude: float) -> dict:

    params = {
        "latitude": latitude,
        "longitude": longitude,

        "current": (
            "temperature_2m,"
            "relative_humidity_2m,"
            "apparent_temperature,"
            "precipitation,"
            "weather_code,"
            "wind_speed_10m,"
            "wind_direction_10m"
        ),

        "daily": (
            "weather_code,"
            "temperature_2m_max,"
            "temperature_2m_min,"
            "apparent_temperature_max,"
            "apparent_temperature_min,"
            "precipitation_probability_max,"
            "precipitation_sum,"
            "sunrise,"
            "sunset,"
            "uv_index_max"
        ),

        "forecast_days": 7,
        "timezone": "Asia/Tashkent",
        "wind_speed_unit": "kmh",
    }

    async with httpx.AsyncClient(timeout=15) as client:
        response = await client.get(
            WEATHER_URL,
            params=params,
        )

        response.raise_for_status()

        return response.json()


def temperature_scale(
    current: float,
    minimum: float,
    maximum: float,
) -> str:

    if maximum <= minimum:
        return f"🌡 {current:.0f}°C"

    position = (current - minimum) / (maximum - minimum)
    position = max(0.0, min(position, 1.0))

    total = 24
    marker = round(position * total)

    scale = ["─"] * (total + 1)
    scale[marker] = "●"

    return (
        f"{minimum:.0f}°C "
        f"{''.join(scale)} "
        f"{maximum:.0f}°C\n"
        f"{' ' * (marker + 7)}{current:.0f}°C"
    )


def farming_advice(
    temperature: float,
    humidity: float,
    rain_probability: int,
    wind_speed: float,
    uv_index: float,
) -> str:

    advice = []

    if temperature >= 35:
        advice.append(
            "🔥 Harorat juda yuqori.\n"
            "💧 Sug‘orishni ertalab yoki kechqurun qilish ma’qul."
        )

    elif temperature >= 30 and rain_probability < 30:
        advice.append(
            "☀️ Havo issiq va yomg‘ir ehtimoli past.\n"
            "💧 Ekinlarning namligini kuzating."
        )

    elif temperature <= 3:
        advice.append(
            "❄️ Harorat juda past.\n"
            "🌱 Sovuqqa sezgir ekinlarni himoyalashni tekshiring."
        )

    if rain_probability >= 70:
        advice.append(
            "🌧 Yomg‘ir ehtimoli yuqori.\n"
            "💧 Sug‘orishni kechiktirish mumkin."
        )

    if wind_speed >= 30:
        advice.append(
            "💨 Shamol kuchli.\n"
            "🌱 Nozik ekinlar va tayanchlarni tekshiring."
        )

    if humidity >= 85:
        advice.append(
            "💧 Namlik juda yuqori.\n"
            "🌱 Zamburug‘li kasallik belgilarini kuzating."
        )

    if uv_index >= 8:
        advice.append(
            "☀️ UV indeksi yuqori.\n"
            "🌱 Kuchli quyosh vaqtida ekinlarni kuzating."
        )

    if not advice:
        advice.append(
            "✅ Ob-havo hozircha qulay.\n"
            "🌱 Ekinlarni odatdagi reja bo‘yicha kuzatib boring."
        )

    return "\n\n".join(advice)


def format_time(value: str) -> str:
    return value.split("T")[-1][:5]


def format_date(value: str) -> str:

    parts = value.split("-")

    if len(parts) == 3:
        return f"{parts[2]}.{parts[1]}"

    return value


def format_weather(
    data: dict,
    location_name: str,
) -> str:

    current = data["current"]
    daily = data["daily"]

    temperature = current["temperature_2m"]
    feels_like = current["apparent_temperature"]
    humidity = current["relative_humidity_2m"]
    precipitation = current["precipitation"]
    weather_code = current["weather_code"]
    wind_speed = current["wind_speed_10m"]
    wind_direction = current["wind_direction_10m"]

    minimum = daily["temperature_2m_min"][0]
    maximum = daily["temperature_2m_max"][0]

    rain_probability = daily["precipitation_probability_max"][0]
    uv_index = daily["uv_index_max"][0]

    sunrise = format_time(daily["sunrise"][0])
    sunset = format_time(daily["sunset"][0])

    description = weather_description(weather_code)

    advice = farming_advice(
        temperature=temperature,
        humidity=humidity,
        rain_probability=rain_probability,
        wind_speed=wind_speed,
        uv_index=uv_index,
    )

    forecast = []

    for i in range(7):

        date = format_date(daily["time"][i])

        min_temp = daily["temperature_2m_min"][i]
        max_temp = daily["temperature_2m_max"][i]

        rain = daily["precipitation_probability_max"][i]

        icon = weather_description(
            daily["weather_code"][i]
        ).split(" ")[0]

        forecast.append(
            f"{date}   {icon}   "
            f"{min_temp:.0f}° / {max_temp:.0f}°   "
            f"🌧 {rain}%"
        )

    forecast_text = "\n".join(forecast)

    return (
        f"🌦 {location_name.upper()}\n\n"
        f"{description}\n\n"

        f"🌡 Hozir: {temperature:.0f}°C\n"
        f"🌡 His qilinadi: {feels_like:.0f}°C\n\n"

        f"{temperature_scale(temperature, minimum, maximum)}\n\n"

        f"⬇️ Minimum: {minimum:.0f}°C\n"
        f"⬆️ Maksimum: {maximum:.0f}°C\n\n"

        f"💧 Namlik: {humidity}%\n"
        f"🌧 Yomg‘ir ehtimoli: {rain_probability}%\n"
        f"💦 Yog‘in: {precipitation:.1f} mm\n"
        f"💨 Shamol: {wind_speed:.0f} km/soat\n"
        f"🧭 Shamol yo‘nalishi: {wind_direction}°\n"
        f"☀️ UV indeksi: {uv_index:.1f}\n\n"

        f"🌅 Quyosh chiqishi: {sunrise}\n"
        f"🌇 Quyosh botishi: {sunset}\n\n"

        f"🌾 DEHQON AI TAVSIYASI\n\n"
        f"{advice}\n\n"

        f"📅 7 KUNLIK PROGNOZ\n\n"
        f"{forecast_text}"
    )