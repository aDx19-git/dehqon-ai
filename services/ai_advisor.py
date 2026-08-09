def get_ai_advice(question: str) -> str:
    text = question.lower().strip()

    # POMIDOR
    if "pomidor" in text:
        if "sug'or" in text or "sugor" in text:
            return (
                "🍅 POMIDORNI SUG‘ORISH\n\n"
                "💧 Pomidorni sug‘orishda tuproq namligini "
                "asosiy mezon sifatida oling.\n\n"
                "🌅 Eng ma’qul vaqt: ertalab yoki kechqurun.\n"
                "☀️ Juda issiq paytda sug‘orishni kamaytirish ma’qul.\n"
                "🌧 Yomg‘ir kutilayotgan bo‘lsa, ortiqcha sug‘orishdan saqlaning.\n\n"
                "🌱 Maslahat: barglarni emas, asosan tuproqni "
                "namlashga harakat qiling."
            )

        return (
            "🍅 POMIDOR\n\n"
            "🌡 Pomidor issiqsevar ekin.\n"
            "💧 Tuproq namligini muntazam kuzatish muhim.\n"
            "☀️ Kuchli issiqda o‘simlikni kuzatib boring.\n"
            "🌧 Yomg‘irdan keyin ortiqcha namlikni tekshiring.\n\n"
            "💡 Aniqroq maslahat uchun savolingizni yozing."
        )

    # BUG‘DOY
    if "bug'doy" in text or "bug‘doy" in text:
        return (
            "🌾 BUG‘DOY\n\n"
            "🌡 Bug‘doy uchun harorat va tuproq namligini "
            "muntazam kuzatish muhim.\n\n"
            "🌧 Kuchli yom‘g‘irdan keyin daladagi ortiqcha "
            "suvni nazorat qiling.\n"
            "🔥 Kuchli issiqda ekinning holatini kuzating.\n\n"
            "💡 Agar sug‘orish yoki kasallik haqida savol bo‘lsa, "
            "savolingizni aniqroq yozing."
        )

    # MAKKAYO‘XORI
    if "makkajo" in text or "makkajo'xori" in text:
        return (
            "🌽 MAKKAJO‘XORI\n\n"
            "🌡 Issiqsevar ekin.\n"
            "💧 Yetarli namlik muhim.\n"
            "☀️ Issiq kunlarda tuproq namligini kuzating.\n"
            "🌧 Yom‘g‘irdan keyin qo‘shimcha sug‘orishni "
            "shoshilmasdan rejalashtiring."
        )

    # BODRING
    if "bodring" in text:
        return (
            "🥒 BODRING\n\n"
            "💧 Bodring namlikni yaxshi ko‘radi.\n"
            "🌡 Juda yuqori haroratda o‘simlikni kuzatish kerak.\n"
            "🌧 Ortiqcha namlik esa kasallik xavfini oshirishi mumkin.\n\n"
            "🌱 Teplitsada yetarli shamollatish ham muhim."
        )

    # KARTOSHKA
    if "kartoshka" in text:
        return (
            "🥔 KARTOSHKA\n\n"
            "🌡 Mo‘tadil harorat qulay.\n"
            "💧 Tuproq namligini kuzating.\n"
            "🔥 Juda issiq havoda o‘simlik holatini tekshiring.\n"
            "🌧 Ortiqcha suv to‘planishiga yo‘l qo‘ymaslik kerak."
        )

    # YOMG‘IR
    if "yomg'ir" in text or "yomg‘ir" in text:
        return (
            "🌧 YOMG‘IR BO‘YICHA\n\n"
            "Agar yomg‘ir kutilayotgan bo‘lsa:\n\n"
            "💧 Sug‘orishni qayta rejalashtiring.\n"
            "🌱 Tuproq namligini tekshiring.\n"
            "🌱 Teplitsada shamollatishni nazorat qiling.\n"
            "🌧 Kuchli yom‘irdan keyin dalada suv to‘planmaganini tekshiring."
        )

    # SUG‘ORISH
    if "sug'or" in text or "sugor" in text:
        return (
            "💧 SUG‘ORISH BO‘YICHA\n\n"
            "Sug‘orish miqdori ekin turi, tuproq va ob-havoga "
            "bog‘liq.\n\n"
            "🌅 Odatda ertalab yoki kechqurun sug‘orish qulay.\n"
            "🌧 Yom‘g‘ir kutilayotgan bo‘lsa, tuproq namligini "
            "oldindan tekshiring.\n"
            "🔥 Kuchli issiqda o‘simlikning suvga ehtiyojini kuzating."
        )

    # TEPLITSA
    if "teplitsa" in text or "issiqxona" in text:
        return (
            "🌱 TEPLITSA BO‘YICHA\n\n"
            "🌡 Haroratni muntazam kuzating.\n"
            "💧 Ichki namlikni nazorat qiling.\n"
            "💨 Juda issiq bo‘lsa shamollatishni tekshiring.\n"
            "🌧 Tashqarida namlik yuqori bo‘lsa, "
            "havo almashinuviga e’tibor bering."
        )

    # UMUMIY
    return (
        "🧠 DEHQON AI\n\n"
        "Savolingizni tushundim, lekin aniqroq maslahat "
        "berishim uchun savolni biroz batafsilroq yozing.\n\n"
        "Masalan:\n"
        "🍅 Pomidorni qachon sug‘orish kerak?\n"
        "🌾 Bug‘doyga yom‘g‘ir zarar qiladimi?\n"
        "🌱 Teplitsani qachon shamollatish kerak?\n"
        "💧 Qachon sug‘orish kerak?\n"
        "🔥 Issiqda ekinni qanday himoyalash kerak?"
    )