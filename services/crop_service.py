# =========================================================
# DEHQON AI — CROP SERVICE
# =========================================================

from __future__ import annotations


# =========================================================
# CROP DATABASE
# =========================================================

CROPS: dict[str, dict] = {

    "bug'doy": {
        "name": "Bug‘doy",
        "icon": "🌾",
        "description": (
            "Donli ekin. Salqinroq sharoitda yaxshi rivojlanadi "
            "va ortiqcha issiqlik, qurg‘oqchilik hamda suv to‘planishiga "
            "sezgir bo‘lishi mumkin."
        ),
        "min_temp": 10,
        "max_temp": 25,
        "water": "O‘rtacha",
        "humidity": "50–70%",
        "aliases": [
            "bug'doy", "bug‘doy", "bugdoy",
            "bug'doyni", "bug‘doyni", "bugdoyni",
            "пшеница", "пшеницу", "пшеницага",
        ],
        "tips": [
            "🌱 Nihollik davrida dalani begona o‘tlardan toza saqlash muhim.",
            "💧 Sug‘orishdan oldin tuproq namligini tekshirish foydali.",
            "🌧 Kuchli yom‘g‘irdan keyin past joylarda suv to‘planishini tekshiring.",
            "☀️ Uzoq davom etgan issiqda tuproq namligi tez kamayishi mumkin.",
            "🌾 Gullash va don to‘lish davrida suv tanqisligi hosilga ta’sir qilishi mumkin.",
            "🌱 Juda zich ekilgan maydonda havo aylanishi yomonlashishi mumkin.",
            "🦠 Barglarda noodatiy dog‘lar paydo bo‘lsa, ularni muntazam kuzating.",
            "🌿 Begona o‘tlar suv va oziqa uchun bug‘doy bilan raqobat qiladi.",
            "💨 Kuchli shamoldan keyin yotib qolgan poyalarni tekshirish foydali.",
            "🌡 Keskin harorat o‘zgarishlarida ekinning rivojlanishini kuzating.",
            "💧 Ortiqcha sug‘orish ildiz zonasida havo kamayishiga olib kelishi mumkin.",
            "🌧 Yom‘irdan keyin darhol qo‘shimcha sug‘orish shart emas.",
            "🧪 O‘g‘itlashni tuproq tahliliga asoslash ancha ishonchli.",
            "🌾 Hosil pishishiga yaqin davrda ortiqcha namlikni nazorat qiling.",
            "📋 Bugungi qarorni faqat bitta ko‘rsatkichga emas, ob-havo va ekin holatiga qarab qabul qiling.",
        ],
    },

    "makkajo'xori": {
        "name": "Makkajo‘xori",
        "icon": "🌽",
        "description": (
            "Issiqsevar ekin. Ayniqsa faol o‘sish davrida yetarli "
            "namlik va quyosh talab qiladi."
        ),
        "min_temp": 18,
        "max_temp": 30,
        "water": "Ko‘p",
        "humidity": "60–80%",
        "aliases": [
            "makkajo'xori", "makkajo‘xori", "makkajoxori",
            "makkajo", "makkani", "makkajo'xori",
            "кукуруза", "кукурузу",
        ],
        "tips": [
            "🌱 Urug‘ unishi uchun tuproqda yetarli namlik bo‘lishi muhim.",
            "💧 Barglar bukilishi va tuproqning quruqligi suv tanqisligidan darak berishi mumkin.",
            "🌽 Gullash davri namlik tanqisligiga ayniqsa sezgir.",
            "☀️ Issiq kunlarda tuproq namligini tez-tez tekshiring.",
            "🌧 Kuchli yom‘irdan keyin ildiz zonasida suv turib qolmasin.",
            "🌿 Begona o‘tlarni erta nazorat qilish o‘sishni yaxshilaydi.",
            "🧪 Azotli o‘g‘itni me’yoridan oshirmaslik kerak.",
            "💨 Kuchli shamoldan keyin poyalarning yotib qolganini tekshiring.",
            "🌡 Juda yuqori haroratda changlanish jarayoni qiyinlashishi mumkin.",
            "💧 Sug‘orishni faqat kalendar bo‘yicha emas, tuproq holatiga qarab belgilang.",
            "🌱 Ildiz zonasini muntazam kuzatish foydali.",
            "🌧 Yom‘ir ehtimoli yuqori bo‘lsa, sug‘orishni qayta hisoblang.",
            "🦠 Barglarda dog‘ yoki chirish belgilari bo‘lsa, namlik sharoitini tekshiring.",
            "🌽 Don to‘lish davrida keskin suv tanqisligiga yo‘l qo‘ymaslik muhim.",
            "📋 Harorat, yom‘ir va tuproq namligini birgalikda baholang.",
        ],
    },

    "pomidor": {
        "name": "Pomidor",
        "icon": "🍅",
        "description": (
            "Issiqsevar sabzavot. Barqaror namlik, yaxshi havo almashinuvi "
            "va keskin stresslardan himoya qilish muhim."
        ),
        "min_temp": 18,
        "max_temp": 30,
        "water": "O‘rtacha",
        "humidity": "60–75%",
        "aliases": [
            "pomidor", "pamidor", "pomodir", "pomidorni",
            "pamidorni", "pom", "помидор", "памидор",
            "помидорни", "томаты", "томат",
        ],
        "tips": [
            "🍅 Pomidorni sug‘orishda bargdan ko‘ra ildiz zonasini namlash ma’qul.",
            "💧 Sug‘orish oralig‘ida tuproqning ustki qatlamini tekshiring.",
            "🌅 Ertalab sug‘orish ko‘pincha qulay sharoit yaratadi.",
            "🌙 Kechasi barglarni uzoq vaqt nam holda qoldirmang.",
            "🌧 Yom‘irdan oldin tuproq allaqachon nam bo‘lsa, qo‘shimcha suv bermang.",
            "💨 Teplitsada havo aylanishi barg namligini kamaytirishga yordam beradi.",
            "🌡 Juda issiq havoda o‘simlikning suvga ehtiyoji oshadi.",
            "☀️ Issiq va quruq shamol tuproq namligini tez kamaytirishi mumkin.",
            "🌱 Yon novdalarni boshqarish o‘simlikning zichligini kamaytirishi mumkin.",
            "🦠 Barglarda jigarrang yoki qora dog‘lar paydo bo‘lsa, kuzatuvni kuchaytiring.",
            "💧 Juda ko‘p suv berish ildiz zonasida muammo keltirib chiqarishi mumkin.",
            "🌿 Mulcha tuproq namligini barqarorroq saqlashga yordam berishi mumkin.",
            "🌸 Gullash paytida keskin suv stressidan saqlanish foydali.",
            "🍅 Meva pishish davrida sug‘orish rejimini keskin o‘zgartirmang.",
            "📋 Ob-havo + tuproq namligi + o‘simlik holatini birgalikda baholang.",
        ],
    },

    "bodring": {
        "name": "Bodring",
        "icon": "🥒",
        "description": (
            "Namlikni yaxshi ko‘radigan ekin. Issiqlik, suv va havo "
            "almashinuvi muvozanati muhim."
        ),
        "min_temp": 18,
        "max_temp": 30,
        "water": "Ko‘p",
        "humidity": "65–85%",
        "aliases": [
            "bodring", "bodringni", "bodr", "бодринг",
            "огурец", "огурцы", "огурецни",
        ],
        "tips": [
            "🥒 Bodring tuproq namligi keskin o‘zgarishiga sezgir.",
            "💧 Tuproqni juda quritib yubormaslikka harakat qiling.",
            "🌅 Ertalab sug‘orish qulay variantlardan biridir.",
            "🌧 Yom‘irdan keyin qo‘shimcha sug‘orishga shoshilmang.",
            "💨 Teplitsada havo almashinuvi juda muhim.",
            "🌡 Kuchli issiqda barglar vaqtincha so‘lishi mumkin, lekin tuproq holatini tekshirish kerak.",
            "🦠 Uzoq vaqt yuqori namlik kasallik xavfini oshirishi mumkin.",
            "🌿 Begona o‘tlarni vaqtida olib tashlash foydali.",
            "🌱 Ildiz atrofidagi tuproqni haddan tashqari zichlashtirmang.",
            "☀️ Kuchli quyoshda tuproq namligini muntazam nazorat qiling.",
            "💧 Barglarga doimiy suv sepishdan ko‘ra ildiz zonasini sug‘orish ma’qul.",
            "🥒 Meva shakli o‘zgarishi stress yoki oziqlanish muammolarini ko‘rsatishi mumkin.",
            "🌸 Gullash paytida suv tanqisligini kamaytirish muhim.",
            "🌧 Tashqarida namlik yuqori bo‘lsa, teplitsani shamollating.",
            "📋 Harorat va namlikni birgalikda kuzatish bodringda ayniqsa foydali.",
        ],
    },

    "kartoshka": {
        "name": "Kartoshka",
        "icon": "🥔",
        "description": (
            "Mo‘tadil sharoitni yaxshi ko‘radigan ildizmevali ekin. "
            "Haddan tashqari issiq va suv to‘planishi muammoga olib kelishi mumkin."
        ),
        "min_temp": 12,
        "max_temp": 25,
        "water": "O‘rtacha",
        "humidity": "60–80%",
        "aliases": [
            "kartoshka", "kartoshkani", "kartosh",
            "картошка", "картофель", "картошку",
        ],
        "tips": [
            "🥔 Tuproq namligini bir tekis saqlash muhim.",
            "💧 Ildiz hosil bo‘lish davrida suv tanqisligidan saqlaning.",
            "🌧 Suv to‘planadigan joylarni alohida nazorat qiling.",
            "🌱 Tuproqni yumshoq va havo o‘tadigan holatda saqlash foydali.",
            "🌿 Begona o‘tlar hosil bilan raqobat qiladi.",
            "☀️ Kuchli issiqda tuproq namligini tez-tez tekshiring.",
            "🦠 Barglarda dog‘lar paydo bo‘lsa, rivojlanishini kuzating.",
            "🌧 Uzoq nam davrda kasallik xavfi oshishi mumkin.",
            "🥔 Tugunaklar yashil rangga kirishiga yo‘l qo‘ymaslik kerak.",
            "🌱 O‘simlikni tuproq bilan uyumlash ildiz zonasini himoyalashga yordam beradi.",
            "💧 Sug‘orish miqdorini tuproq turiga moslashtiring.",
            "🌡 Juda yuqori harorat hosil shakllanishiga salbiy ta’sir qilishi mumkin.",
            "🌧 Kuchli yom‘irdan keyin daladagi drenajni tekshiring.",
            "🧪 O‘g‘itlashda ayniqsa azot miqdorini nazorat qiling.",
            "📋 Hosilga yaqin davrda namlikni ortiqcha oshirmaslik foydali.",
        ],
    },

    "sabzi": {
        "name": "Sabzi",
        "icon": "🥕",
        "description": (
            "Ildizmevali ekin. Yumshoq, toshsiz tuproq va bir maromdagi "
            "namlik ildizning tekis rivojlanishiga yordam beradi."
        ),
        "min_temp": 10,
        "max_temp": 27,
        "water": "O‘rtacha",
        "humidity": "50–70%",
        "aliases": [
            "sabzi", "sabzini", "sabza", "морковь", "морковку",
        ],
        "tips": [
            "🥕 Sabzi uchun tuproqning yumshoqligi ildiz shakliga katta ta’sir qiladi.",
            "💧 Namlikning keskin o‘zgarishi ildizlarning yorilishiga sabab bo‘lishi mumkin.",
            "🌱 Urug‘ unishi davrida tuproq yuzasini quritib yubormang.",
            "🌿 Yosh nihollarni begona o‘tlardan himoya qiling.",
            "🌧 Kuchli yom‘irdan keyin tuproq zichlashganini tekshiring.",
            "☀️ Issiq kunlarda yuzaki tuproq tez qurishi mumkin.",
            "💧 Juda ko‘p suv berishdan ko‘ra bir tekis namlik ma’qul.",
            "🌱 Qator oralari ehtiyotkorlik bilan yumshatilishi mumkin.",
            "🦠 Barglarda rang o‘zgarishi paydo bo‘lsa kuzatuvni kuchaytiring.",
            "🥕 Ildiz rivojlanayotgan davrda tuproqning chuqurroq qatlamini ham tekshiring.",
            "🧪 Yangi go‘ngni bevosita sabzi ekiladigan joyga berishdan saqlanish ma’qul.",
            "🌧 Yom‘irli kunlarda sug‘orishni kamaytirish kerak bo‘lishi mumkin.",
            "☀️ Uzoq qurg‘oqchilikdan keyin birdaniga juda ko‘p suv bermang.",
            "🌱 Tuproqdagi tosh va zich qatlamlar ildiz shaklini buzishi mumkin.",
            "📋 Hosilga yaqin davrda namlikni barqaror saqlashga e’tibor bering.",
        ],
    },

    "piyoz": {
        "name": "Piyoz",
        "icon": "🧅",
        "description": (
            "Piyozning ildiz va piyozbosh rivojlanishida namlik, quyosh "
            "va tuproqning havo o‘tkazuvchanligi muhim."
        ),
        "min_temp": 10,
        "max_temp": 28,
        "water": "O‘rtacha",
        "humidity": "50–70%",
        "aliases": [
            "piyoz", "piyozni", "лук", "луковица",
        ],
        "tips": [
            "🧅 Piyoz uchun quyoshli joy tanlash foydali.",
            "💧 O‘sish davrida tuproq namligini muntazam tekshiring.",
            "🌧 Suv turib qolishi piyozboshga zarar yetkazishi mumkin.",
            "🌿 Begona o‘tlarni erta nazorat qilish muhim.",
            "☀️ Kuchli issiqda yuzaki tuproq tez qurishi mumkin.",
            "🌱 Tuproqning haddan tashqari zichlashishiga yo‘l qo‘ymang.",
            "🦠 Barg uchlarining qurishi turli stresslar bilan bog‘liq bo‘lishi mumkin.",
            "💧 Hosil pishishiga yaqin ortiqcha sug‘orishni kamaytirish kerak bo‘lishi mumkin.",
            "🌧 Yom‘irli davrda piyozbosh atrofida suv to‘planmasin.",
            "🧪 Azotni haddan tashqari ko‘paytirish pishishni kechiktirishi mumkin.",
            "🌱 Qator oralari begona o‘tlardan toza bo‘lsa oziqa raqobati kamayadi.",
            "☀️ Yetarli yorug‘lik piyozbosh shakllanishiga yordam beradi.",
            "💨 Havo almashinuvi barglarning uzoq nam qolishini kamaytiradi.",
            "🧅 Piyozbosh kattalashish davrida suv tanqisligini kuzating.",
            "📋 Hosil yig‘imiga yaqin ob-havo prognozini oldindan hisobga oling.",
        ],
    },

    "sarimsoq": {
        "name": "Sarimsoq",
        "icon": "🧄",
        "description": (
            "Salqinroq sharoitni yoqtiradigan piyozdosh ekin. "
            "Tuproqning yaxshi drenaji va me’yoridagi namlik muhim."
        ),
        "min_temp": 8,
        "max_temp": 26,
        "water": "O‘rtacha",
        "humidity": "50–70%",
        "aliases": [
            "sarimsoq", "sarimsoqni", "чеснок", "чеснока",
        ],
        "tips": [
            "🧄 Sarimsoq uchun yaxshi drenajlangan tuproq muhim.",
            "💧 O‘sish davrida tuproqni haddan tashqari quritib yubormang.",
            "🌧 Suv turib qolishi piyozbosh chirish xavfini oshirishi mumkin.",
            "🌿 Begona o‘tlarni vaqtida nazorat qiling.",
            "🌡 Salqinroq sharoitda ildiz rivojlanishi qulay kechishi mumkin.",
            "☀️ Juda issiq davrda namlikni nazorat qilish muhim.",
            "🦠 Barglarda dog‘ yoki sarg‘ayish kuzatilsa tekshiruvni kuchaytiring.",
            "💧 Hosil pishishiga yaqin sug‘orishni me’yorlashtirish kerak.",
            "🌱 Tuproqning zichlashib qolishiga yo‘l qo‘ymang.",
            "🧪 O‘g‘itlashni tuproq holatiga qarab rejalashtiring.",
            "🌧 Uzoq yom‘irli davrda drenajni tekshiring.",
            "💨 Havo almashinuvi yuqori namlik sharoitida foydali.",
            "🧄 Piyozbosh kattalashayotgan davrda suv stressini kamaytiring.",
            "☀️ Hosilni yig‘ishdan oldin uzoq nam davr bo‘lsa reja tuzing.",
            "📋 Namlik, harorat va barg holatini birgalikda kuzating.",
        ],
    },

    "qalampir": {
        "name": "Qalampir",
        "icon": "🫑",
        "description": (
            "Issiqsevar sabzavot. Barqaror issiqlik, yorug‘lik va "
            "me’yoridagi namlik yaxshi rivojlanish uchun muhim."
        ),
        "min_temp": 18,
        "max_temp": 30,
        "water": "O‘rtacha",
        "humidity": "60–75%",
        "aliases": [
            "qalampir", "qalampirni", "qalamp", "перец", "перецни",
        ],
        "tips": [
            "🫑 Qalampir sovuq haroratga sezgir.",
            "🌡 Harorat qulay diapazondan chiqsa o‘sishni kuzating.",
            "💧 Tuproq namligini keskin o‘zgartirmang.",
            "☀️ Yetarli yorug‘lik meva shakllanishiga yordam beradi.",
            "🌧 Yom‘irdan keyin suv turib qolmaganini tekshiring.",
            "🌱 Ildiz zonasida havo yetishmasligiga yo‘l qo‘ymang.",
            "🌸 Gullash paytida suv stressini kamaytirish muhim.",
            "🔥 Juda issiq havoda o‘simlikni tez-tez kuzating.",
            "🦠 Barglarda dog‘ yoki burishish bo‘lsa sababini tekshiring.",
            "🌿 Begona o‘tlar bilan raqobatni kamaytiring.",
            "💧 Sug‘orishni tuproq namligiga moslang.",
            "🌧 Yom‘ir ehtimoli yuqori bo‘lsa sug‘orishni qayta rejalashtiring.",
            "🧪 O‘g‘itni me’yoridan oshirmang.",
            "🫑 Meva hosil bo‘lish davrida barqaror sharoitni saqlash foydali.",
            "📋 Harorat va namlikdagi keskin o‘zgarishlarni alohida kuzating.",
        ],
    },

    "baqlajon": {
        "name": "Baqlajon",
        "icon": "🍆",
        "description": (
            "Issiqsevar ekin. Issiqlik, quyosh va tuproq namligining "
            "barqarorligi hosil shakllanishida muhim."
        ),
        "min_temp": 20,
        "max_temp": 32,
        "water": "O‘rtacha",
        "humidity": "60–75%",
        "aliases": [
            "baqlajon", "baqlajonni", "баклажан", "баклажаны",
        ],
        "tips": [
            "🍆 Baqlajon iliq tuproq va havoni yaxshi ko‘radi.",
            "☀️ Yorug‘lik yetarli bo‘lishiga e’tibor bering.",
            "💧 Tuproq namligini barqaror saqlash foydali.",
            "🌧 Kuchli yom‘irdan keyin ildiz zonasini tekshiring.",
            "🔥 Issiq havoda suv ehtiyojini kuzating.",
            "🌱 Ildiz atrofidagi tuproqni zichlashtirmang.",
            "🌸 Gullash davrida keskin suv stressidan saqlaning.",
            "🦠 Barglardagi dog‘larni erta kuzatish muhim.",
            "🌿 Begona o‘tlarni nazorat qiling.",
            "💧 Barglarni doimiy namlab turishdan saqlaning.",
            "🌡 Kechasi keskin sovuq bo‘lsa rivojlanishni kuzating.",
            "🧪 O‘g‘itlashni ekinning rivojlanish bosqichiga moslang.",
            "🌧 Nam ob-havoda teplitsani shamollatish foydali.",
            "🍆 Meva hosil bo‘lish davrida namlikni keskin o‘zgartirmang.",
            "📋 Harorat + namlik + yom‘ir ehtimolini birga baholang.",
        ],
    },

    "karam": {
        "name": "Karam",
        "icon": "🥬",
        "description": (
            "Salqinroq sharoitga moslashgan sabzavot. Yetarli namlik "
            "va oziqa bilan birga yaxshi havo almashinuvi ham muhim."
        ),
        "min_temp": 12,
        "max_temp": 25,
        "water": "Ko‘p",
        "humidity": "60–80%",
        "aliases": [
            "karam", "karamni", "капуста", "капусту",
        ],
        "tips": [
            "🥬 Karam tuproq namligiga talabchan.",
            "💧 Quruq davrda tuproq namligini muntazam tekshiring.",
            "🌧 Suv turib qolishi ildizlarga zarar yetkazishi mumkin.",
            "🌱 Begona o‘tlarni vaqtida nazorat qiling.",
            "🌡 Juda yuqori haroratda o‘simlik stressga tushishi mumkin.",
            "☀️ Issiq kunlarda suv ehtiyojini kuzating.",
            "🦠 Barglarni muntazam ko‘zdan kechiring.",
            "🐛 Barglarda hasharot yoki teshiklar paydo bo‘lsa tekshiring.",
            "💧 Sug‘orishni keskin ko‘paytirish yoki kamaytirishdan saqlaning.",
            "🌿 Tuproqni yengil yumshatish ildiz zonasiga foyda berishi mumkin.",
            "🌧 Uzoq yom‘irli davrda drenajni nazorat qiling.",
            "🧪 Oziqlantirishni rivojlanish bosqichiga moslang.",
            "🥬 Bosh hosil bo‘lish davrida suv stressini kamaytirish muhim.",
            "☀️ Kuchli issiqda tuproq namligini tez-tez tekshiring.",
            "📋 Barg holati, tuproq namligi va ob-havoni birgalikda kuzating.",
        ],
    },

    "salat": {
        "name": "Salat",
        "icon": "🥗",
        "description": (
            "Tez o‘sadigan bargli ekin. Mo‘tadil harorat va bir maromdagi "
            "namlik sifatli barg hosil bo‘lishiga yordam beradi."
        ),
        "min_temp": 10,
        "max_temp": 24,
        "water": "O‘rtacha",
        "humidity": "55–75%",
        "aliases": [
            "salat", "salatni", "lettuce", "салат",
        ],
        "tips": [
            "🥗 Salat mo‘tadil haroratda yaxshi rivojlanadi.",
            "💧 Tuproq namligini barqaror saqlash muhim.",
            "☀️ Kuchli issiq barglarning tez qarishiga sabab bo‘lishi mumkin.",
            "🌧 Yom‘irli davrda ortiqcha namlikni nazorat qiling.",
            "🌱 Yosh nihollarni qurib qolishdan himoya qiling.",
            "🌿 Begona o‘tlar bilan raqobatni kamaytiring.",
            "💨 Havo almashinuvi barglarning uzoq nam qolishini kamaytiradi.",
            "🦠 Barglarda dog‘lar paydo bo‘lsa kuzating.",
            "💧 Barglarni emas, imkon qadar ildiz zonasini sug‘oring.",
            "🌡 Juda issiq havoda ekin holatini tez-tez tekshiring.",
            "🌱 Qatorlar orasida yetarli masofa havo aylanishiga yordam beradi.",
            "🧪 Ortiqcha azotdan ehtiyot bo‘ling.",
            "🌧 Yom‘irdan keyin barglar uzoq nam qolsa havo almashinuvini yaxshilang.",
            "🥗 Hosilni haddan tashqari kechiktirmaslik sifatga yordam beradi.",
            "📋 Salatda harorat va namlikni birgalikda kuzatish juda muhim.",
        ],
    },

    "tarvuz": {
        "name": "Tarvuz",
        "icon": "🍉",
        "description": (
            "Issiqsevar poliz ekini. Quyosh, issiqlik va ildiz zonasida "
            "yetarli namlik muhim."
        ),
        "min_temp": 20,
        "max_temp": 35,
        "water": "Ko‘p",
        "humidity": "50–70%",
        "aliases": [
            "tarvuz", "tarvuzni", "arbuz", "арбуз", "арбузы",
        ],
        "tips": [
            "🍉 Tarvuz issiq va quyoshli sharoitni yaxshi ko‘radi.",
            "☀️ Yetarli quyosh meva pishishiga yordam beradi.",
            "💧 Meva kattalashish davrida namlik muhim.",
            "🌧 Kuchli yom‘irdan keyin suv turib qolmasin.",
            "🔥 Juda issiq havoda tuproq namligini tekshiring.",
            "🌱 Ildiz zonasida yaxshi drenaj bo‘lishi kerak.",
            "🌿 Begona o‘tlarni nazorat qilish suv raqobatini kamaytiradi.",
            "🌸 Gullash davrida suv stressini kamaytiring.",
            "🍉 Meva kattalashganda namlikni keskin o‘zgartirmang.",
            "💧 Hosil pishishiga yaqin sug‘orish rejimini ehtiyotkorlik bilan boshqaring.",
            "🦠 Barglarda dog‘lar paydo bo‘lsa kuzating.",
            "🌧 Nam va issiq sharoitda kasallik xavfini nazorat qiling.",
            "🌱 Mevalarning tuproq bilan doimiy nam aloqasini kamaytirish foydali.",
            "☀️ Issiq shamol tuproqni tez quritishi mumkin.",
            "📋 Tarvuzda ob-havo va sug‘orish rejasini birga ko‘rib chiqish kerak.",
        ],
    },

    "qovun": {
        "name": "Qovun",
        "icon": "🍈",
        "description": (
            "Issiqsevar poliz ekini. Quyosh, issiqlik va rivojlanish "
            "bosqichiga mos namlik talab qiladi."
        ),
        "min_temp": 20,
        "max_temp": 35,
        "water": "O‘rtacha",
        "humidity": "50–70%",
        "aliases": [
            "qovun", "qovunni", "дыня", "дыню",
        ],
        "tips": [
            "🍈 Qovun issiq va quyoshli ob-havoni yaxshi ko‘radi.",
            "☀️ Yorug‘lik yetarli bo‘lishi pishishga yordam beradi.",
            "💧 Faol o‘sish davrida namlikni nazorat qiling.",
            "🌧 Kuchli yom‘irdan keyin suv to‘planishini tekshiring.",
            "🔥 Issiq shamol tuproq namligini tez kamaytirishi mumkin.",
            "🌱 Yaxshi drenaj ildizlar uchun muhim.",
            "🌿 Begona o‘tlarni vaqtida nazorat qiling.",
            "🌸 Gullash davrida suv stressini kamaytirish foydali.",
            "🍈 Meva kattalashish davrida namlikni barqaror saqlang.",
            "💧 Pishishga yaqin sug‘orishni keskin o‘zgartirmang.",
            "🦠 Barglarda dog‘lar paydo bo‘lsa kuzating.",
            "🌧 Nam va issiq sharoitda havo almashinuviga e’tibor bering.",
            "🌱 Mevalarning tuproq bilan ortiqcha nam aloqasini kamaytiring.",
            "☀️ Kuchli issiqda ildiz zonasidagi namlikni tekshiring.",
            "📋 Qovunda sug‘orish qarorini rivojlanish bosqichi bilan bog‘lang.",
        ],
    },

    "qulupnay": {
        "name": "Qulupnay",
        "icon": "🍓",
        "description": (
            "Ildiz zonasi namligini yaxshi ko‘radigan, lekin suv turib "
            "qolishiga sezgir mevali ekin."
        ),
        "min_temp": 12,
        "max_temp": 26,
        "water": "O‘rtacha",
        "humidity": "60–75%",
        "aliases": [
            "qulupnay", "qulupnayni", "клубника", "клубнику",
        ],
        "tips": [
            "🍓 Qulupnay ildiz zonasida bir maromdagi namlikni yaxshi ko‘radi.",
            "💧 Tuproqni quritib yubormaslikka harakat qiling.",
            "🌧 Kuchli yom‘irdan keyin suv turib qolmaganini tekshiring.",
            "🌱 Mulcha tuproq namligini saqlashga yordam berishi mumkin.",
            "☀️ Juda issiqda sug‘orish ehtiyojini kuzating.",
            "🌸 Gullash davrida suv stressini kamaytiring.",
            "🍓 Mevalarning nam tuproq bilan uzoq aloqa qilishini kamaytiring.",
            "💨 Barglar uzoq vaqt nam qolmasligi uchun havo almashinuvi muhim.",
            "🦠 Mevada chirish belgilari bo‘lsa namlik sharoitini tekshiring.",
            "🌿 Begona o‘tlarni nazorat qiling.",
            "💧 Imkon qadar ildiz zonasiga sug‘oring.",
            "🌡 Kuchli issiqda mevalarni muntazam kuzating.",
            "🌧 Yom‘irli davrda sug‘orish rejasini kamaytirish kerak bo‘lishi mumkin.",
            "🧪 Oziqlantirishni meva hosil qilish bosqichiga moslang.",
            "📋 Namlik va havo almashinuvi qulupnayda birdek muhim.",
        ],
    },

    "uzum": {
        "name": "Uzum",
        "icon": "🍇",
        "description": (
            "Ko‘p yillik tok ekini. Quyosh, yaxshi drenaj va rivojlanish "
            "bosqichiga mos suv ta’minoti muhim."
        ),
        "min_temp": 15,
        "max_temp": 32,
        "water": "O‘rtacha",
        "humidity": "50–70%",
        "aliases": [
            "uzum", "uzumni", "tok", "uzumzor",
            "виноград", "виноградник",
        ],
        "tips": [
            "🍇 Uzum uchun quyoshli joy juda muhim.",
            "💧 Sug‘orish miqdorini tokning yoshiga moslang.",
            "🌧 Kuchli yom‘irdan keyin ildiz zonasida suv turib qolmasin.",
            "☀️ Issiq davrda tuproq namligini kuzating.",
            "🌿 Tokni to‘g‘ri shakllantirish havo aylanishiga yordam beradi.",
            "💨 Shamol kuchli bo‘lsa yosh novdalarni tekshiring.",
            "🌸 Gullash davrida ob-havoni alohida kuzatish foydali.",
            "🍇 Meva kattalashish davrida suv stressini kamaytiring.",
            "💧 Pishishga yaqin sug‘orish rejimini keskin o‘zgartirmang.",
            "🦠 Barg va shingillarda dog‘lar paydo bo‘lsa kuzating.",
            "🌧 Uzoq nam ob-havo kasallik xavfini oshirishi mumkin.",
            "☀️ Barglarning haddan tashqari qizib ketishini kuzating.",
            "🧪 O‘g‘itlashni tuproq va barg tahliliga asoslash ma’qul.",
            "🍇 Hosil pishish davrida namlikni ortiqcha oshirmang.",
            "📋 Tokda ob-havo, tuproq va rivojlanish bosqichi birgalikda baholanadi.",
        ],
    },

    "mevali_daraxtlar": {
        "name": "Mevali daraxtlar",
        "icon": "🍎",
        "description": (
            "Olma, nok, o‘rik, shaftoli va boshqa mevali daraxtlarni "
            "qamrab oluvchi umumiy guruh. Har bir tur va navning talabi farq qiladi."
        ),
        "min_temp": 10,
        "max_temp": 30,
        "water": "O‘rtacha",
        "humidity": "50–75%",
        "aliases": [
            "mevali daraxtlar",
            "mevali daraxt",
            "daraxtlar",
            "olma",
            "nok",
            "o'rik",
            "o‘rik",
            "shaftoli",
            "яблоня",
            "груша",
            "абрикос",
            "персик",
        ],
        "tips": [
            "🍎 Mevali daraxtlarda daraxt yoshini hisobga olish muhim.",
            "💧 Yosh daraxtlarning suv ehtiyoji kattalarnikidan farq qiladi.",
            "🌧 Kuchli yom‘irdan keyin ildiz zonasida suv turib qolmasin.",
            "☀️ Issiq davrda tuproq namligini chuqurroq qatlamda ham tekshiring.",
            "🌱 Daraxt tagidagi begona o‘tlar suv uchun raqobat qiladi.",
            "🌿 Tojning haddan tashqari zich bo‘lishi havo almashinuvini kamaytirishi mumkin.",
            "🌸 Gullash davrida keskin ob-havo o‘zgarishlarini kuzating.",
            "🦠 Barg va mevalardagi dog‘larni muntazam kuzatish foydali.",
            "💨 Kuchli shamoldan keyin singan yoki shikastlangan shoxlarni tekshiring.",
            "🍎 Meva kattalashish davrida namlik stressidan saqlanish muhim.",
            "💧 Sug‘orishni faqat daraxt tanasiga emas, ildizlarning asosiy zonasiga yo‘naltirish kerak.",
            "🌧 Yom‘ir ko‘p bo‘lsa sug‘orishni avtomatik davom ettirmang.",
            "🧪 O‘g‘itlashni tuproq tahliliga asoslash eng to‘g‘ri yondashuvlardan biridir.",
            "❄️ Kechki sovuq xavfi bo‘lsa ayniqsa gullayotgan daraxtlarni kuzating.",
            "📋 Mevali daraxtlarda ob-havo + daraxt yoshi + rivojlanish bosqichi birga baholanadi.",
        ],
    },
}


# =========================================================
# ALIAS INDEX
# =========================================================

_ALIAS_INDEX: dict[str, str] = {}


def _normalize(text: str) -> str:
    """
    Foydalanuvchi turlicha yozgan so‘zlarni bir xil ko‘rinishga keltiradi.
    """
    return (
        text.lower()
        .strip()
        .replace("’", "'")
        .replace("‘", "'")
        .replace("`", "'")
    )


for key, crop in CROPS.items():
    _ALIAS_INDEX[_normalize(key)] = key

    for alias in crop.get("aliases", []):
        _ALIAS_INDEX[_normalize(alias)] = key


# =========================================================
# GET CROP
# =========================================================

def get_crop(crop_key: str) -> dict | None:
    """
    Ekinni key yoki alias orqali topadi.
    """

    if not crop_key:
        return None

    normalized = _normalize(crop_key)

    # To‘g‘ridan-to‘g‘ri key
    if normalized in CROPS:
        return CROPS[normalized]

    # Alias orqali
    real_key = _ALIAS_INDEX.get(normalized)

    if real_key:
        return CROPS.get(real_key)

    # Foydalanuvchi gap ichida yozsa ham topishga harakat qiladi
    for alias, real_key in _ALIAS_INDEX.items():
        if len(alias) >= 4 and alias in normalized:
            return CROPS.get(real_key)

    return None


# =========================================================
# CROP KEY
# =========================================================

def resolve_crop_key(text: str) -> str | None:
    """
    Foydalanuvchi yozgan matndan ekin key'ini aniqlaydi.
    """

    if not text:
        return None

    normalized = _normalize(text)

    if normalized in CROPS:
        return normalized

    if normalized in _ALIAS_INDEX:
        return _ALIAS_INDEX[normalized]

    for alias, key in _ALIAS_INDEX.items():
        if len(alias) >= 4 and alias in normalized:
            return key

    return None


# =========================================================
# WEATHER ANALYSIS
# =========================================================

def _weather_advice(
    crop: dict,
    temperature: float,
    rain_probability: int,
) -> list[str]:

    advice: list[str] = []

    min_temp = crop["min_temp"]
    max_temp = crop["max_temp"]

    # HARORAT
    if temperature < min_temp:
        advice.append(
            f"❄️ Hozirgi harorat {temperature:.0f}°C — "
            f"{crop['name']} uchun tavsiya etilgan {min_temp}°C dan past."
        )

        advice.append(
            "🧣 Sovuq stressi ehtimoli sababli ayniqsa yosh o‘simliklarni kuzating."
        )

    elif temperature > max_temp:
        advice.append(
            f"🔥 Hozirgi harorat {temperature:.0f}°C — "
            f"{crop['name']} uchun yuqori diapazondan oshgan."
        )

        advice.append(
            "💧 Tuproq namligini tekshiring va suv stressi belgilariga e’tibor bering."
        )

    else:
        advice.append(
            f"✅ Hozirgi harorat {temperature:.0f}°C — "
            f"{crop['name']} uchun qulay diapazonda."
        )

    # YOMG‘IR
    if rain_probability >= 80:
        advice.append(
            f"🌧 Yom‘ir ehtimoli {rain_probability}% — "
            "bugun qo‘shimcha sug‘orishni shoshilmasdan rejalashtiring."
        )

        advice.append(
            "💦 Yom‘irdan keyin tuproqning namligini tekshirmasdan yana suv bermang."
        )

    elif rain_probability >= 60:
        advice.append(
            f"🌦 Yom‘ir ehtimoli {rain_probability}% — "
            "sug‘orish qarorini ob-havoga moslang."
        )

        advice.append(
            "🌧 Ayniqsa og‘ir tuproqda suv turib qolish ehtimolini hisobga oling."
        )

    elif rain_probability <= 20:
        advice.append(
            f"☀️ Yom‘ir ehtimoli {rain_probability}% — "
            "tabiiy yog‘ingarchilik kam bo‘lishi kutilmoqda."
        )

        advice.append(
            "💧 Tuproq namligini tekshirib, ekinning rivojlanish bosqichiga qarab sug‘orishni rejalashtiring."
        )

    else:
        advice.append(
            f"🌦 Yom‘ir ehtimoli {rain_probability}% — "
            "vaziyat o‘rtacha."
        )

    # KUCHLI ISSIQ
    if temperature >= 35:
        advice.append(
            "🔥 35°C va undan yuqori issiqda suvning bug‘lanishi tezlashadi."
        )

        advice.append(
            "🌅 Sug‘orish zarur bo‘lsa, odatda salqinroq vaqtda bajarish ma’qul."
        )

    # SOVUQ
    if temperature <= 5:
        advice.append(
            "❄️ 5°C atrofidagi yoki undan past haroratda sovuq stressi xavfini alohida baholang."
        )

    return advice


# =========================================================
# CROP ADVICE
# =========================================================

def crop_advice(
    crop_key: str,
    temperature: float,
    rain_probability: int,
) -> str:

    crop = get_crop(crop_key)

    if crop is None:
        return (
            "❌ Ekin topilmadi.\n\n"
            "Ekin nomini masalan: pomidor, pamidor, bodring, "
            "sabzi yoki boshqa nom bilan yozib ko‘ring."
        )

    advice: list[str] = []

    # 1. Ob-havo tahlili
    advice.extend(
        _weather_advice(
            crop=crop,
            temperature=temperature,
            rain_probability=rain_probability,
        )
    )

    # 2. Ekin uchun maxsus bilimlar
    advice.extend(crop["tips"])

    return "\n".join(
        f"{index}. {item}"
        for index, item in enumerate(advice, start=1)
    )


# =========================================================
# FORMAT CROP
# =========================================================

def format_crop(
    crop_key: str,
    temperature: float,
    rain_probability: int,
) -> str:

    crop = get_crop(crop_key)

    if crop is None:
        return (
            "❌ Ekin topilmadi.\n\n"
            "Iltimos, ekinni menyudan tanlang."
        )

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

        f"💦 Tavsiya etiladigan namlik: "
        f"{crop['humidity']}\n\n"

        f"🌦 BUGUNGI OB-HAVO\n"
        f"🌡 Harorat: {temperature:.0f}°C\n"
        f"🌧 Yom‘ir ehtimoli: "
        f"{rain_probability}%\n\n"

        f"🧠 DEHQON AI — BUGUNGI TAVSIYALAR\n\n"

        f"{advice}\n\n"

        f"⚠️ Eslatma: bu umumiy agrotexnik tavsiya. "
        f"Tuproq turi, nav, ekinning yoshi va rivojlanish bosqichi "
        f"aniq qarorga ta’sir qiladi."
    )