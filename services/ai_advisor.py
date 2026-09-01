# services/ai_advisor.py

from __future__ import annotations

import re
from typing import Dict, List, Optional


# =========================================================
# DEHQON AI — UNIVERSAL AGRICULTURE ADVISOR
# =========================================================

# Bu fayl:
# 1. foydalanuvchi yozgan matnni tozalaydi;
# 2. o‘zbekcha/ruscha/xato/slang variantlarni taniydi;
# 3. ekinni aniqlaydi;
# 4. muammoni aniqlaydi;
# 5. mos, batafsil maslahat beradi.


# =========================================================
# 1. EKINLAR
# =========================================================

CROPS: Dict[str, Dict[str, object]] = {

    "pomidor": {
        "name": "🍅 Pomidor",
        "aliases": [
            "pomidor",
            "pamidor",
            "pomdor",
            "pomidr",
            "помидор",
            "памидор",
            "томаты",
            "томат",
            "tomat",
        ],
        "advice": [
            "Pomidor ildiz zonasida namlikning keskin o‘zgarishini yoqtirmaydi.",
            "Sug‘orishdan oldin tuproqning ildiz joylashgan qatlamidagi namligini tekshirish foydali.",
            "Faqat tuproq yuzasiga qarab sug‘orish haqida qaror qilmang.",
            "Issiq kunlarda suv bug‘lanishi tezlashadi, shuning uchun namlikni tez-tez nazorat qilish kerak.",
            "Yom‘irdan keyin qo‘shimcha sug‘orishga shoshilmang.",
            "Suvni asosan ildiz atrofiga berish barglarni doimiy ho‘l qoldirishdan ko‘ra ma’qul.",
            "Barglarning uzoq vaqt nam qolishi ayrim zamburug‘li kasalliklar xavfini oshirishi mumkin.",
            "Teplitsada havo aylanishi yaxshi bo‘lishi muhim.",
            "Juda zich barglar orasida namlik yig‘ilib qolmasligiga e’tibor bering.",
            "Barg sarg‘ayishi faqat suv yetishmasligidan bo‘lmaydi; oziqa, ildiz va kasallik holatini ham tekshirish kerak.",
            "Bargdagi dog‘larning rangi, shakli va qaysi barglarda paydo bo‘layotganini kuzating.",
            "Bargning pastki tomonini ham zararkunandalar uchun tekshiring.",
            "Gullash davrida keskin suv stressi o‘simlikning hosil shakllantirishiga ta’sir qilishi mumkin.",
            "Azotli o‘g‘itni ortiqcha berish ko‘p barg va kamroq meva muvozanatiga olib kelishi mumkin.",
            "Tuproqda suv uzoq turib qolsa, drenajni tekshiring.",
            "Yovvoyi o‘tlarni nazorat qilish pomidorning suv va oziqa uchun raqobatini kamaytiradi.",
            "Muammoni aniqlashda o‘simlikning yoshi va rivojlanish bosqichini hisobga oling.",
            "Bir dona bargdagi belgiga qarab butun o‘simlik haqida xulosa qilishga shoshilmang.",
        ],
    },

    "bodring": {
        "name": "🥒 Bodring",
        "aliases": [
            "bodring",
            "bodr",
            "бодринг",
            "огурец",
            "огурцы",
            "ogurets",
        ],
        "advice": [
            "Bodring namlikka talabchan ekin hisoblanadi.",
            "Tuproqning uzoq vaqt quruq qolishi o‘simlikni stressga tushirishi mumkin.",
            "Namlikning keskin o‘zgarishi mevalarning shakliga ta’sir qilishi mumkin.",
            "Issiq kunlarda tuproq namligini tez-tez tekshiring.",
            "Yom‘irdan keyin qo‘shimcha suv berishdan oldin tuproqni tekshiring.",
            "Barglarni doimiy ho‘l saqlashdan saqlanish foydali.",
            "Teplitsada yuqori namlik va yomon shamollatish kasallik xavfini oshirishi mumkin.",
            "Issiqxonada havo aylanishini nazorat qiling.",
            "Barglarning pastki qismini mayda zararkunandalar uchun tekshiring.",
            "Bargda oq kukunsimon qatlam paydo bo‘lsa, uni e’tiborsiz qoldirmang.",
            "Barglarning cheti qurishi faqat suv yetishmasligidan bo‘lmasligi mumkin.",
            "Mevalar g‘alati shakllansa, suv, changlanish va oziqlanishni birga tekshiring.",
            "O‘simliklarni haddan tashqari zich joylashtirish havo aylanishini yomonlashtiradi.",
            "Azotning ortiqcha berilishi vegetativ o‘sishni kuchaytirishi mumkin.",
            "Ildiz atrofida suv uzoq turib qolmasligi kerak.",
            "Kasallangan barglarning qayerdan boshlanganini kuzatib boring.",
            "Hosilni muntazam yig‘ib turish o‘simlikning keyingi meva hosil qilishiga yordam beradi.",
        ],
    },

    "qalampir": {
        "name": "🌶 Qalampir",
        "aliases": [
            "qalampir",
            "kalampir",
            "qalamp",
            "перец",
            "перчик",
            "pepper",
        ],
        "advice": [
            "Qalampir issiqsevar ekin bo‘lib, keskin sovuqdan zarar ko‘rishi mumkin.",
            "Tuproq namligini barqaror saqlash muhim.",
            "Juda quruq tuproqdan keyin birdan ko‘p suv berish o‘simlikka stress berishi mumkin.",
            "Sug‘orishdan oldin ildiz zonasidagi namlikni tekshiring.",
            "Issiqda barglarning vaqtincha osilishi kuzatilishi mumkin, lekin tuproq holatini ham tekshirish kerak.",
            "Barglarning doimiy osilib turishi qo‘shimcha tekshiruv talab qiladi.",
            "Gullash davrida suv va oziqa ta’minotiga alohida e’tibor bering.",
            "Meva shakllanishida namlikning keskin o‘zgarishidan saqlaning.",
            "Barglarning yuqori va pastki tomonini zararkunandalar uchun tekshiring.",
            "Teplitsada harorat va namlikni birgalikda kuzating.",
            "Zich barglar orasida havo aylanishini yaxshilang.",
            "Azotli o‘g‘itni me’yoridan oshirmang.",
            "Ildiz atrofida suv to‘planib qolmasligi kerak.",
            "Yovvoyi o‘tlarni nazorat qilish foydali.",
            "Barglarning burishishi issiqdan tashqari zararkunanda yoki boshqa stress bilan ham bog‘liq bo‘lishi mumkin.",
            "O‘simlikning yoshi va gullash bosqichi tashxisda muhim.",
        ],
    },

    "baqlajon": {
        "name": "🍆 Baqlajon",
        "aliases": [
            "baqlajon",
            "baqlaj",
            "баклажан",
            "баклажаны",
        ],
        "advice": [
            "Baqlajon issiqsevar ekin bo‘lib, iliq sharoitda yaxshi rivojlanadi.",
            "Tuproq namligini keskin o‘zgartirmang.",
            "Ortiqcha suv ildiz zonasida kislorod kamayishiga sabab bo‘lishi mumkin.",
            "Issiq kunlarda tuproq namligini nazorat qiling.",
            "Barglarning osilishi sababini suv bilan birga harorat va ildiz holati orqali tekshiring.",
            "Gullash paytida keskin suv stressidan saqlaning.",
            "Barglarning pastki tomonida mayda hasharotlarni qidiring.",
            "Barglarda mayda nuqtalar ko‘payayotgan bo‘lsa, zararkunandalarni tekshiring.",
            "Teplitsada shamollatish muhim.",
            "Zich barglar orasida namlik uzoq saqlanmasin.",
            "Azotli o‘g‘itni ortiqcha bermang.",
            "Meva hosil bo‘lishida oziqlanish muvozanatini saqlang.",
            "Suv to‘planadigan joylarda drenajni tekshiring.",
            "Yovvoyi o‘tlarni vaqtida nazorat qiling.",
            "Kasallikning qaysi barglardan boshlanganini kuzating.",
            "Birgina alomat asosida kasallik nomini aniq deb qabul qilmang.",
        ],
    },

    "kartoshka": {
        "name": "🥔 Kartoshka",
        "aliases": [
            "kartoshka",
            "kartosh",
            "картошка",
            "картофель",
        ],
        "advice": [
            "Kartoshkada tuproq namligi hosil shakllanishi uchun muhim.",
            "Uzoq davom etgan qurg‘oqchilik o‘simlikka stress beradi.",
            "Ortiqcha namlik ildiz va tuganaklar bilan bog‘liq muammolarni kuchaytirishi mumkin.",
            "Dalada suv to‘planadigan joylarni tekshiring.",
            "Yom‘irdan keyin tuproqning qurish holatini kuzating.",
            "Barglarda dog‘lar paydo bo‘lsa, ularning tarqalishini kuzating.",
            "Barglarning pastki tomonini ham tekshiring.",
            "Zararkunandalarni muntazam nazorat qiling.",
            "Issiq va quruq davrda namlikni ko‘proq kuzating.",
            "Yovvoyi o‘tlar suv va oziqa uchun raqobat qiladi.",
            "Zich tuproq ildiz rivojlanishini cheklashi mumkin.",
            "O‘g‘itlashni imkon qadar tuproq tahliliga asoslang.",
            "Faqat barg rangiga qarab o‘g‘itni keskin oshirmang.",
            "Hosilga yaqin davrda sug‘orish rejasini ob-havo bilan birga ko‘rib chiqing.",
            "Kasallik belgilari ko‘payayotgan bo‘lsa, zararlangan joylarni alohida kuzating.",
            "Bir xil muammo butun dalada bor-yo‘qligini bir nechta joydan tekshiring.",
        ],
    },

    "piyoz": {
        "name": "🧅 Piyoz",
        "aliases": [
            "piyoz",
            "пиёз",
            "лук",
            "луковица",
        ],
        "advice": [
            "Piyozda ortiqcha namlik ildiz va piyozbosh muammolarini kuchaytirishi mumkin.",
            "Sug‘orishni tuproq namligiga qarab rejalashtiring.",
            "Yom‘irdan keyin darhol qo‘shimcha suv bermang.",
            "Tuproqning suvni qanchalik ushlab turishini hisobga oling.",
            "Barglarning sarg‘ayishi rivojlanish bosqichiga qarab turli sababga ega bo‘lishi mumkin.",
            "Barglarda mayda hasharotlar borligini tekshiring.",
            "Piyoz ekilgan joyda suv uzoq turmasligi kerak.",
            "Zich tuproq ildiz rivojlanishini qiyinlashtirishi mumkin.",
            "Yovvoyi o‘tlarni nazorat qiling.",
            "Azotli o‘g‘itni me’yoridan oshirmang.",
            "Issiq va quruq havoda namlikni tekshiring.",
            "Barglarda dog‘lar paydo bo‘lsa, ularning tarqalishini kuzating.",
            "Sug‘orish vaqtini ob-havo bilan birga rejalashtiring.",
            "Hosil pishishiga yaqin sug‘orish rejimi o‘zgarishi mumkin.",
            "Kasallikni baholashda bargning qaysi qismidan boshlanganiga qarang.",
            "Muammo davom etsa, tuproq tahlili foydali bo‘lishi mumkin.",
        ],
    },

    "sarimsoq": {
        "name": "🧄 Sarimsoq",
        "aliases": [
            "sarimsoq",
            "sarmsoq",
            "чеснок",
        ],
        "advice": [
            "Sarimsoqda tuproqning ortiqcha nam bo‘lib qolishidan ehtiyot bo‘ling.",
            "Suv to‘planadigan joylarda drenajni tekshiring.",
            "Yom‘irdan keyin tuproq namligini baholang.",
            "Barglarning sarg‘ayishini rivojlanish bosqichi bilan birga baholang.",
            "Barglarda dog‘lar paydo bo‘lsa, tarqalishini kuzating.",
            "Zararkunandalarni barg va tuproq yuzasida tekshiring.",
            "Yovvoyi o‘tlarni nazorat qiling.",
            "Tuproq zichlashib qolmasligi ildiz rivojlanishi uchun foydali.",
            "O‘g‘itni me’yorida qo‘llang.",
            "Azotni ortiqcha berish o‘simlik muvozanatini buzishi mumkin.",
            "Issiq va quruq davrda namlikni nazorat qiling.",
            "Sug‘orishni kalendar emas, tuproq holati bilan bog‘lang.",
            "Hosilga yaqin davrda sug‘orish rejasini alohida baholang.",
            "Kasallangan o‘simliklarni erta aniqlash muhim.",
            "Bir nechta joydan o‘simliklarni tekshiring.",
        ],
    },

    "sabzi": {
        "name": "🥕 Sabzi",
        "aliases": [
            "sabzi",
            "сабзи",
            "морковь",
            "morkov",
        ],
        "advice": [
            "Sabzi uchun yumshoq va ildiz rivojlanishiga qulay tuproq muhim.",
            "Zich tuproq ildizning shakllanishiga xalaqit berishi mumkin.",
            "Sug‘orishda keskin quruq-nam almashinuvidan saqlaning.",
            "Yom‘irdan keyin tuproq namligini tekshiring.",
            "Ortiqcha suv drenaj muammolarini kuchaytirishi mumkin.",
            "Yovvoyi o‘tlarni yosh davrda nazorat qilish juda muhim.",
            "Tuproq yuzasida qattiq qatlam hosil bo‘lishiga yo‘l qo‘ymaslikka harakat qiling.",
            "Barglarning rangidagi o‘zgarishlarni kuzating.",
            "Sarg‘ayish sababini aniqlashda suv va oziqa holatini birga tekshiring.",
            "Barglarda hasharotlar borligini tekshiring.",
            "O‘g‘itlashni tuproq holatiga qarab qiling.",
            "Azotni ortiqcha berish ildiz hosilining sifatiga ta’sir qilishi mumkin.",
            "Issiq va quruq havoda namlikni muntazam kuzating.",
            "Dalada suv turib qoladigan joylarni nazorat qiling.",
            "Ildizning shakli tuproqning fizik holati bilan bog‘liq bo‘lishi mumkin.",
            "Hosil rivojlanishini muntazam tekshirib boring.",
        ],
    },

    "karam": {
        "name": "🥬 Karam",
        "aliases": [
            "karam",
            "кочан",
            "капуста",
            "капустa",
        ],
        "advice": [
            "Karamda suv va oziqa ta’minotining barqarorligi muhim.",
            "Tuproq uzoq vaqt quruq qolmasligi kerak.",
            "Ortiqcha namlik ildiz muammolarini kuchaytirishi mumkin.",
            "Sug‘orishdan oldin tuproq namligini tekshiring.",
            "Barglarning pastki tomonini zararkunandalar uchun tekshiring.",
            "Barglarda teshiklar paydo bo‘lsa, sababini tekshiring.",
            "Teshiklarning shakli va qayerda paydo bo‘layotganini kuzating.",
            "Yovvoyi o‘tlar bilan raqobatni kamaytiring.",
            "Zich ekish havo aylanishini yomonlashtirishi mumkin.",
            "Yom‘irdan keyin barglarning uzoq nam qolishiga e’tibor bering.",
            "Issiq havoda tuproq namligini tez-tez tekshiring.",
            "O‘g‘itlashni rivojlanish bosqichiga moslashtiring.",
            "Azotni ortiqcha bermang.",
            "Barglarning sarg‘ayishini suv, oziqa va kasallik bilan birga baholang.",
            "Karam bosh hosil qilayotgan paytda namlikni keskin o‘zgartirmang.",
            "Bir nechta belgini birga tahlil qilish aniqroq xulosa beradi.",
        ],
    },

    "lavlagi": {
        "name": "🟣 Lavlagi",
        "aliases": [
            "lavlagi",
            "lavlag",
            "свекла",
            "svekla",
        ],
        "advice": [
            "Lavlagi uchun tuproq namligining barqarorligi muhim.",
            "Juda quruq tuproq ildiz rivojlanishini cheklashi mumkin.",
            "Ortiqcha suv ildiz zonasida muammo tug‘dirishi mumkin.",
            "Yom‘irdan keyin sug‘orishni shoshilmasdan rejalashtiring.",
            "Tuproq zichligini tekshiring.",
            "Yovvoyi o‘tlarni erta nazorat qilish foydali.",
            "Barglarning rangini muntazam kuzating.",
            "Sarg‘ayish sababini aniqlashda tuproq va suv holatini tekshiring.",
            "Barglarda dog‘lar bo‘lsa, ularning tarqalishini kuzating.",
            "Zararkunandalarni bargning ikki tomonida tekshiring.",
            "O‘g‘itni tuproq holatiga qarab tanlang.",
            "Azotni ortiqcha berishdan saqlaning.",
            "Issiq havoda namlik tezroq kamayishi mumkin.",
            "Drenaj yomon joylarda suv to‘planishiga yo‘l qo‘ymang.",
            "Ildiz shakli tuproqning fizik holatiga bog‘liq bo‘lishi mumkin.",
            "Hosil rivojlanishini muntazam kuzating.",
        ],
    },

    "makkajo'xori": {
        "name": "🌽 Makkajo‘xori",
        "aliases": [
            "makkajo'xori",
            "makkajoxori",
            "makkajo",
            "makkajo‘xori",
            "маккажўхори",
            "кукуруза",
            "кукурўза",
            "kukuruza",
        ],
        "advice": [
            "Makkajo‘xorida suv talabi rivojlanish bosqichiga qarab o‘zgaradi.",
            "Faol o‘sish davrida tuproq namligini muntazam nazorat qilish muhim.",
            "Yom‘irdan keyin qo‘shimcha sug‘orishdan oldin tuproqni tekshiring.",
            "Uzoq qurg‘oqchilik o‘sish va hosil shakllanishiga ta’sir qilishi mumkin.",
            "Ortiqcha namlik ildiz zonasida havo kamayishiga olib kelishi mumkin.",
            "Dalada suv turib qoladigan joylarni aniqlang.",
            "Yovvoyi o‘tlar yosh o‘simlik bilan kuchli raqobat qiladi.",
            "Barglarning burishishi yoki osilishi suv stressini ko‘rsatishi mumkin.",
            "Barg rangidagi o‘zgarishlarni oziqlanish bilan birga baholang.",
            "Azotli oziqlanishda me’yor juda muhim.",
            "Azotni ortiqcha qo‘llash samarasiz bo‘lishi va ayrim muammolarni kuchaytirishi mumkin.",
            "Issiq va quruq davrda namlikni tez-tez tekshiring.",
            "Kuchli shamol va issiq birga kelganda stress oshishi mumkin.",
            "Ildiz zonasining holatini tekshiring.",
            "Kasallik va zararkunanda belgilarini erta aniqlash muhim.",
            "Barglarda dog‘ paydo bo‘lsa, tarqalishini kuzating.",
            "Sug‘orishni faqat kalendar bo‘yicha emas, tuproq va ob-havoga qarab belgilang.",
        ],
    },

    "bug'doy": {
        "name": "🌾 Bug‘doy",
        "aliases": [
            "bug'doy",
            "bugdoy",
            "bug'doy",
            "бугдой",
            "пшеница",
            "pshenitsa",
        ],
        "advice": [
            "Bug‘doyning suvga ehtiyoji rivojlanish bosqichiga qarab o‘zgaradi.",
            "Tuproq namligi ekinning umumiy holatini baholashda muhim.",
            "Kuchli yom‘irdan keyin dalada suv turib qolmaganini tekshiring.",
            "Ortiqcha namlik ildiz zonasida muammo tug‘dirishi mumkin.",
            "Quruq davrda barg va poya holatini kuzating.",
            "Barg rangining o‘zgarishi oziqa yetishmasligi bilan bog‘liq bo‘lishi mumkin.",
            "Bargdagi dog‘lar kasallik belgisi bo‘lishi mumkin, ammo aniq tashxis uchun qo‘shimcha belgilar kerak.",
            "Zararkunandalarni dalada muntazam tekshiring.",
            "Yovvoyi o‘tlar suv va oziqa uchun raqobat qiladi.",
            "Azotli o‘g‘itni rivojlanish bosqichiga mos qo‘llang.",
            "Azotni ortiqcha berish o‘simlikning yotib qolish xavfini oshirishi mumkin.",
            "Shamolli va nam ob-havoda o‘simlik holatini diqqat bilan kuzating.",
            "Hosilga yaqin davrda ob-havo prognozini hisobga oling.",
            "Sug‘orish qarorini tuproq turi va yog‘ingarchilik bilan birga baholang.",
            "Dalaning bir nechta joyidan tekshiruv o‘tkazing.",
            "Faqat bitta o‘simlikka qarab butun dala haqida xulosa qilmang.",
            "Muammo keng tarqalgan bo‘lsa, agronom bilan maslahatlashish ma’qul.",
        ],
    },

    "qovoq": {
        "name": "🎃 Qovoq",
        "aliases": [
            "qovoq",
            "qovo",
            "тыква",
            "тыквы",
        ],
        "advice": [
            "Qovoq issiq sharoitda yaxshi rivojlanadi.",
            "Tuproq namligini barqaror ushlash muhim.",
            "Yosh o‘simliklarda suv stressi tezroq sezilishi mumkin.",
            "Yom‘irdan keyin sug‘orishni tuproq holatiga qarab belgilang.",
            "Ortiqcha namlik ildiz muammolarini kuchaytirishi mumkin.",
            "Barglarda dog‘lar paydo bo‘lsa, ularning tarqalishini kuzating.",
            "Barglarning pastki tomonini zararkunandalar uchun tekshiring.",
            "Yovvoyi o‘tlarni nazorat qiling.",
            "Gullash paytida suv va oziqa ta’minotiga e’tibor bering.",
            "Issiq va quruq havoda namlikni tez-tez tekshiring.",
            "Zich barglar orasida havo aylanishini yaxshilang.",
            "Azotli o‘g‘itni me’yoridan oshirmang.",
            "Meva hosil bo‘lish davrida namlikni keskin o‘zgartirmang.",
            "Suv to‘planadigan joylarda drenajni tekshiring.",
            "Kasallikni birgina alomat bilan aniqlashga shoshilmang.",
        ],
    },

    "qovoqcha": {
        "name": "🥒 Qovoqcha",
        "aliases": [
            "qovoqcha",
            "kabachki",
            "кабачок",
            "кабачки",
            "zucchini",
        ],
        "advice": [
            "Qovoqcha namlikni yaxshi ko‘radi, ammo suvning uzoq turib qolishi zararli bo‘lishi mumkin.",
            "Sug‘orishdan oldin ildiz zonasini tekshiring.",
            "Issiq havoda tuproq namligini nazorat qiling.",
            "Yom‘irdan keyin qo‘shimcha suvga shoshilmang.",
            "Barglarni uzoq vaqt ho‘l qoldirmaslikka harakat qiling.",
            "Barglarning pastki tomonini zararkunandalar uchun tekshiring.",
            "Oq dog‘ yoki qatlam paydo bo‘lsa, kuzatuvni kuchaytiring.",
            "Gullash davrida suv stressidan saqlaning.",
            "Yovvoyi o‘tlarni nazorat qiling.",
            "Zich o‘simliklar orasida havo aylanishini yaxshilang.",
            "Azotni ortiqcha bermang.",
            "Mevalarni muntazam yig‘ib turish foydali.",
            "Suv to‘planadigan joylarda drenajni tekshiring.",
            "Barglarning keskin sarg‘ayish sababini tekshiring.",
            "Muammoni aniqlashda ob-havo va sug‘orish tarixini ham hisobga oling.",
        ],
    },

    "no'xat": {
        "name": "🫛 No‘xat",
        "aliases": [
            "no'xat",
            "noxat",
            "nohat",
            "нохот",
            "горох",
            "gorox",
        ],
        "advice": [
            "No‘xatda ortiqcha namlik ildiz zonasiga zarar yetkazishi mumkin.",
            "Tuproqning suvni ushlab turish xususiyatini hisobga oling.",
            "Yom‘irdan keyin sug‘orishga shoshilmang.",
            "Issiq va quruq davrda o‘simlik holatini kuzating.",
            "Barg rangidagi o‘zgarishlarni muntazam tekshiring.",
            "Yovvoyi o‘tlar bilan raqobatni kamaytiring.",
            "Barglarning pastki tomonini zararkunandalar uchun tekshiring.",
            "Kasallik alomatlari paydo bo‘lsa, tarqalish tezligini kuzating.",
            "Zich ekilgan joylarda havo aylanishiga e’tibor bering.",
            "O‘g‘itni me’yorida qo‘llang.",
            "Azotli o‘g‘itni ortiqcha berishga ehtiyot bo‘ling.",
            "Gullash davrida namlik sharoitini nazorat qiling.",
            "Suv turib qoladigan joylarni yaxshilang.",
            "Muammoni baholashda o‘simlikning rivojlanish bosqichini hisobga oling.",
            "Bir nechta joydan o‘simliklarni tekshirish aniqroq xulosa beradi.",
        ],
    },

    "loviya": {
        "name": "🫘 Loviya",
        "aliases": [
            "loviya",
            "lovya",
            "fasol",
            "фасоль",
            "lovi",
        ],
        "advice": [
            "Loviya uchun namlik muhim, lekin ortiqcha suvdan ehtiyot bo‘lish kerak.",
            "Sug‘orishdan oldin ildiz zonasidagi namlikni tekshiring.",
            "Issiq havoda suv stressini kuzating.",
            "Yom‘irdan keyin qo‘shimcha sug‘orishni tuproq holatiga qarab belgilang.",
            "Barglarda dog‘ yoki rang o‘zgarishini kuzating.",
            "Barglarning pastki tomonini zararkunandalar uchun tekshiring.",
            "Yovvoyi o‘tlarni nazorat qiling.",
            "Zich ekilgan joylarda havo aylanishini yaxshilang.",
            "Gullash davrida suv stressidan saqlanish muhim.",
            "Azotni ortiqcha berishdan saqlaning.",
            "O‘simlikning umumiy holatini bir nechta joydan tekshiring.",
            "Suv turib qoladigan tuproqlarda drenajni yaxshilang.",
            "Kasallik tarqalishini erta kuzatish foydali.",
            "Ob-havo keskin o‘zgarsa, sug‘orish rejasini qayta ko‘rib chiqing.",
            "Hosil shakllanishida namlikni barqaror saqlashga e’tibor bering.",
        ],
    },

    "tarvuz": {
        "name": "🍉 Tarvuz",
        "aliases": [
            "tarvuz",
            "tarbus",
            "арбуз",
            "arbuз",
        ],
        "advice": [
            "Tarvuz issiqsevar ekin bo‘lib, quyoshli sharoitni yaxshi ko‘radi.",
            "Yosh o‘simliklarda tuproq namligini nazorat qilish muhim.",
            "Meva shakllanish davrida suv stressidan saqlanish kerak.",
            "Yom‘irdan keyin sug‘orishga shoshilmang.",
            "Ortiqcha namlik ildiz muammolarini kuchaytirishi mumkin.",
            "Suvni ildiz zonasiga yetkazish ma’qul.",
            "Barglarning uzoq nam qolishidan saqlaning.",
            "Barglarda dog‘ va zararkunandalarni muntazam tekshiring.",
            "Yovvoyi o‘tlar bilan raqobatni kamaytiring.",
            "Issiq va shamolli kunlarda namlik tezroq kamayishi mumkin.",
            "Azotni ortiqcha berish vegetativ o‘sishni kuchaytirishi mumkin.",
            "Gullash davrida o‘simlik holatini diqqat bilan kuzating.",
            "Meva rivojlanishida sug‘orishni keskin o‘zgartirmang.",
            "Suv to‘planadigan joylarda drenajni tekshiring.",
            "Ob-havo va tuproq holatini birgalikda hisobga oling.",
        ],
    },

    "qovun": {
        "name": "🍈 Qovun",
        "aliases": [
            "qovun",
            "ковун",
            "дыня",
            "dinya",
        ],
        "advice": [
            "Qovun issiq va yorug‘ sharoitni yaxshi ko‘radi.",
            "Tuproq namligini rivojlanish bosqichiga qarab kuzating.",
            "Yom‘irdan keyin sug‘orishga shoshilmang.",
            "Ortiqcha namlik ildiz zonasiga zarar yetkazishi mumkin.",
            "Gullash davrida keskin suv stressidan saqlaning.",
            "Meva rivojlanishida sug‘orish rejimini barqaror tutish foydali.",
            "Barglarda dog‘ paydo bo‘lsa, tarqalishini kuzating.",
            "Zararkunandalarni bargning ikki tomonidan tekshiring.",
            "Yovvoyi o‘tlarni nazorat qiling.",
            "Issiq va shamolli havoda tuproq tez qurishi mumkin.",
            "Azotni ortiqcha bermang.",
            "Suv turib qoladigan joylarda drenajni tekshiring.",
            "Barglarning keskin sarg‘ayishi sababini tekshiring.",
            "Hosilga yaqin davrda sug‘orish rejasini ob-havo bilan birga baholang.",
            "O‘simlikning bir nechta joyini tekshirib, umumiy holatni baholang.",
        ],
    },

    "redis": {
        "name": "🌱 Redis",
        "aliases": [
            "redis",
            "rediska",
            "редис",
            "редиска",
        ],
        "advice": [
            "Redis tez rivojlanadigan ekin bo‘lgani uchun namlikning keskin o‘zgarishi sezilarli ta’sir qilishi mumkin.",
            "Tuproqni haddan tashqari quritib yubormang.",
            "Ortiqcha suvdan ham ehtiyot bo‘ling.",
            "Tuproqning yumshoq bo‘lishi ildizmeva shakllanishi uchun muhim.",
            "Yovvoyi o‘tlarni yosh davrda nazorat qiling.",
            "Issiq sharoitda tuproq namligini tez-tez tekshiring.",
            "Barglarning rangini kuzating.",
            "Barglarda hasharotlar borligini tekshiring.",
            "Yom‘irdan keyin sug‘orishga shoshilmang.",
            "Tuproq yuzasida qattiq qatlam paydo bo‘lishiga yo‘l qo‘ymang.",
            "O‘g‘itni me’yorida qo‘llang.",
            "Azotni ortiqcha bermang.",
            "Hosilni kechiktirib yubormaslik kerak.",
            "Bir nechta o‘simlikni tekshirib, rivojlanish bir xilligini baholang.",
            "Muammoni ob-havo va tuproq holati bilan birga tahlil qiling.",
        ],
    },

    "ismaloq": {
        "name": "🥬 Ismaloq",
        "aliases": [
            "ismaloq",
            "исмалоқ",
            "шпинат",
            "shpinat",
        ],
        "advice": [
            "Ismaloq salqinroq sharoitda yaxshi rivojlanadi.",
            "Issiq havoda o‘simlik tezroq stressga tushishi mumkin.",
            "Tuproq namligini muntazam nazorat qiling.",
            "Yom‘irdan keyin qo‘shimcha suv bermang.",
            "Ortiqcha namlik ildiz muammolarini kuchaytirishi mumkin.",
            "Barglarning rangini kuzating.",
            "Barglarning pastki tomonini zararkunandalar uchun tekshiring.",
            "Zich ekilgan joylarda havo aylanishiga e’tibor bering.",
            "Yovvoyi o‘tlarni nazorat qiling.",
            "Azotli o‘g‘itni me’yorida qo‘llang.",
            "Barglarda dog‘ paydo bo‘lsa, tarqalishini kuzating.",
            "Issiqda namlikni tez-tez tekshiring.",
            "Sug‘orish vaqtini ob-havo bilan birga belgilang.",
            "Kasallik belgilarini erta aniqlash foydali.",
            "Hosilni o‘z vaqtida yig‘ish muhim.",
        ],
    },
}


# =========================================================
# 2. SO‘ZLARNI NORMALIZATSIYA QILISH
# =========================================================

WORD_REPLACEMENTS = {
    # -------------------------
    # O‘zbekcha xatolar
    # -------------------------
    "pamidor": "pomidor",
    "pomidr": "pomidor",
    "pomdor": "pomidor",

    "bodr": "bodring",
    "bodrin": "bodring",

    "kalampir": "qalampir",
    "qalamp": "qalampir",

    "baqlaj": "baqlajon",

    "kartosh": "kartoshka",

    "sarmsoq": "sarimsoq",

    "noxat": "no'xat",
    "nohat": "no'xat",

    "lovya": "loviya",

    "makkajo": "makkajo'xori",
    "makkajoxori": "makkajo'xori",

    "bugdoy": "bug'doy",

    # -------------------------
    # Sug‘orish
    # -------------------------
    "sugor": "sug'orish",
    "sugorish": "sug'orish",
    "sug'orish": "sug'orish",
    "sugoraman": "sug'orish",
    "sug'oraman": "sug'orish",
    "sugorsam": "sug'orish",
    "sug'orsam": "sug'orish",
    "sugoray": "sug'orish",
    "sug'oray": "sug'orish",
    "suvber": "suv",
    "suvberay": "suv",

    # -------------------------
    # Slang / qisqartmalar
    # -------------------------
    "kere": "kerak",
    "keremi": "kerakmi",
    "boladi": "bo'ladi",
    "boladimi": "bo'ladimi",
    "qiliw": "qilish",
    "qilw": "qilish",
    "qilaman": "qilish",
    "qivor": "qilish",
    "qivur": "qilish",
    "qanaqa": "qanday",
    "qando": "qanday",
    "qanday": "qanday",
    "nma": "nima",
    "nima": "nima",
    "nmaga": "nimaga",
    "nega": "nima uchun",
    "qachon": "qachon",

    # -------------------------
    # Ruscha yozuvlar
    # -------------------------
    "памидор": "помидор",
    "помидоры": "помидор",
    "томаты": "помидор",
    "томата": "помидор",

    "огурцы": "огурец",
    "огурца": "огурец",

    "баклажаны": "баклажан",

    "картофель": "картошка",

    "морковь": "морковь",

    "капуста": "капуста",

    "перчик": "перец",

    # Ruscha mavzular
    "поливать": "sug'orish",
    "полив": "sug'orish",
    "полива": "sug'orish",
    "поливаю": "sug'orish",
    "полить": "sug'orish",
    "вода": "suv",
    "воды": "suv",

    "дождь": "yomg'ir",
    "дождя": "yomg'ir",
    "дожди": "yomg'ir",

    "жара": "issiq",
    "жарко": "issiq",
    "горячо": "issiq",

    "болезнь": "kasallik",
    "болеет": "kasallik",

    "вредитель": "zararkunanda",
    "вредители": "zararkunanda",
    "насекомые": "zararkunanda",

    "желтеет": "sarg'ayish",
    "желтые": "sarg'ayish",
    "желтый": "sarg'ayish",

    "сохнет": "qurish",
    "вянет": "so'lish",
    "вянут": "so'lish",

    "теплица": "teplitsa",
    "парник": "teplitsa",
}


def normalize_text(text: str) -> str:
    """
    Foydalanuvchi matnini:
    - kichik harfga;
    - apostroflarni bir xil ko‘rinishga;
    - ortiqcha belgilarni olib;
    - xato/slang/ruscha variantlarni standart shaklga
    keltiradi.
    """

    text = str(text or "").lower().strip()

    # Apostrof variantlari
    text = (
        text
        .replace("‘", "'")
        .replace("’", "'")
        .replace("`", "'")
        .replace("ʻ", "'")
    )

    # Harf orasidagi ortiqcha belgilar
    text = re.sub(r"[!?.,;:(){}\[\]\"/\\]+", " ", text)
    text = re.sub(r"\s+", " ", text).strip()

    # Uzun variantlarni oldin almashtirish
    replacements = sorted(
        WORD_REPLACEMENTS.items(),
        key=lambda item: len(item[0]),
        reverse=True,
    )

    for old, new in replacements:
        pattern = rf"(?<!\w){re.escape(old)}(?!\w)"
        text = re.sub(pattern, new, text)

    return text


# =========================================================
# 3. EKINNI ANIQLASH
# =========================================================

def find_crop(text: str) -> Optional[str]:
    """
    Savolda qaysi ekin borligini aniqlaydi.
    """

    normalized = normalize_text(text)

    # Avval aliaslardan foydalanamiz.
    for crop_key, crop_data in CROPS.items():
        aliases = crop_data.get("aliases", [])

        for alias in aliases:
            alias = normalize_text(alias)

            if alias and alias in normalized:
                return crop_key

    # Standart nomlar
    for crop_key in CROPS:
        if crop_key in normalized:
            return crop_key

    return None


# =========================================================
# 4. MAVZUNI ANIQLASH
# =========================================================

TOPIC_KEYWORDS = {

    "sug'orish": [
        "sug'orish",
        "suv",
        "полив",
        "поливать",
        "полить",
        "sugor",
    ],

    "yomg'ir": [
        "yomg'ir",
        "yomgir",
        "дождь",
        "дожди",
    ],

    "issiq": [
        "issiq",
        "juda issiq",
        "жара",
        "жарко",
        "qizib",
        "qizigan",
    ],

    "sovuq": [
        "sovuq",
        "muz",
        "sovub",
        "холод",
        "холодно",
        "замороз",
    ],

    "kasallik": [
        "kasallik",
        "kasal",
        "dog'",
        "dog",
        "mog'or",
        "mogor",
        "chir",
        "грибок",
        "болезнь",
    ],

    "zararkunanda": [
        "zararkunanda",
        "hasharot",
        "qurt",
        "kana",
        "bit",
        "kapalak",
        "вредитель",
        "насеком",
        "червь",
    ],

    "sarg'ayish": [
        "sarg'ay",
        "sargay",
        "sariq",
        "желте",
        "желтый",
        "желтые",
    ],

    "so'lish": [
        "so'lish",
        "solish",
        "so'lib",
        "solib",
        "osilib",
        "вянет",
        "вянут",
    ],

    "teplitsa": [
        "teplitsa",
        "issiqxona",
        "теплица",
        "парник",
    ],

    "o'g'it": [
        "o'g'it",
        "og'it",
        "o'g'itlash",
        "gubre",
        "удобр",
        "подкорм",
    ],

    "tuproq": [
        "tuproq",
        "yer",
        "земля",
        "почва",
    ],
}


def find_topics(text: str) -> List[str]:
    """
    Savolda bir nechta mavzu bo‘lsa, hammasini qaytaradi.
    """

    normalized = normalize_text(text)
    found = []

    for topic, keywords in TOPIC_KEYWORDS.items():
        for keyword in keywords:
            keyword = normalize_text(keyword)

            if keyword and keyword in normalized:
                found.append(topic)
                break

    return found


# =========================================================
# 5. UMUMIY MAVZU MASLAHATLARI
# =========================================================

GENERAL_TOPIC_ADVICE = {

    "sug'orish": [
        "Sug‘orish vaqtini faqat soat yoki kalendarga qarab emas, tuproq namligiga qarab belgilang.",
        "Yom‘irdan keyin tuproq namligini tekshirmasdan yana suv berish ortiqcha namlikka olib kelishi mumkin.",
        "Issiq va shamolli havoda suv bug‘lanishi tezlashadi.",
        "Ortiqcha sug‘orish ham o‘simlikka zarar yetkazishi mumkin.",
        "Ildiz zonasida suv uzoq turib qolsa, drenajni tekshirish kerak.",
    ],

    "yomg'ir": [
        "Yom‘irdan keyin qo‘shimcha sug‘orishga shoshilmang.",
        "Dalada suv to‘planib qolgan joylarni tekshiring.",
        "Teplitsada tashqi namlik yuqori bo‘lsa, havo almashinuvini nazorat qiling.",
        "Barglar uzoq vaqt nam qolsa, ayrim kasalliklar xavfi oshishi mumkin.",
        "Yom‘ir miqdorini tuproq turi bilan birga baholash kerak.",
    ],

    "issiq": [
        "Issiq havoda tuproq namligini tez-tez tekshiring.",
        "O‘simlikning barglari kunning qaysi vaqtida osilayotganini kuzating.",
        "Sug‘orishni ortiqcha ko‘paytirishdan oldin ildiz zonasidagi haqiqiy namlikni tekshiring.",
        "Tuproq yuzasining juda tez qurishi mulchalash kabi usullarni ko‘rib chiqishga sabab bo‘lishi mumkin.",
        "Teplitsada harorat haddan tashqari oshmasligi uchun shamollatishni nazorat qiling.",
    ],

    "sovuq": [
        "Sovuq tushishi kutilayotgan bo‘lsa, issiqsevar ekinlarning holatini oldindan tekshiring.",
        "Sovuqdan keyin barg va yosh novdalardagi o‘zgarishlarni kuzating.",
        "Zararlangan o‘simlikka darhol ortiqcha o‘g‘it yoki suv berishga shoshilmang.",
        "Ob-havo yana sovuqlashishi mumkin bo‘lsa, himoya choralarini oldindan rejalashtiring.",
        "Ekinning sovuqqa chidamliligi turiga va rivojlanish bosqichiga bog‘liq.",
    ],

    "kasallik": [
        "Kasallikni aniqlashda faqat bitta belgiga emas, bir nechta belgiga qarang.",
        "Bargning yuqori va pastki tomonini tekshiring.",
        "Dog‘ning rangi, shakli va kattalashish tezligini kuzating.",
        "Muammo bir o‘simlikdami yoki butun qatordami — aniqlang.",
        "Oxirgi kunlardagi yom‘ir, namlik va sug‘orish holatini hisobga oling.",
    ],

    "zararkunanda": [
        "Barglarning yuqori va pastki tomonini tekshiring.",
        "Yangi barglar va yosh novdalarni alohida kuzating.",
        "Mayda hasharotlar, tuxumlar yoki yopishqoq izlar borligini tekshiring.",
        "Zararkunanda sonining oshib borayotganini kuzatish muhim.",
        "Zararkunandaning turi noma’lum bo‘lsa, kuchli vositani tasodifiy ishlatishga shoshilmang.",
    ],

    "sarg'ayish": [
        "Barg sarg‘ayishi suv, oziqa, ildiz, tabiiy qarish yoki kasallik bilan bog‘liq bo‘lishi mumkin.",
        "Avval sarg‘ayish qaysi barglardan boshlanganini aniqlang.",
        "Tuproq namligini tekshiring.",
        "Bargning pastki tomonini zararkunandalar uchun ko‘ring.",
        "Sarg‘ayish bilan birga dog‘, qurish yoki chirish bor-yo‘qligini tekshiring.",
    ],

    "so'lish": [
        "So‘lishni faqat suv yetishmasligi deb qabul qilmang.",
        "Avval ildiz zonasidagi tuproq namligini tekshiring.",
        "Tuproq haddan tashqari nam bo‘lsa, ildiz muammosi ehtimolini ham hisobga oling.",
        "Issiq paytda so‘lish kuchliroq ko‘rinishi mumkin.",
        "Barglarning qaysi vaqtda so‘lishini kuzatish sababni aniqlashga yordam beradi.",
    ],

    "teplitsa": [
        "Teplitsada harorat va namlikni birgalikda kuzatish kerak.",
        "Yuqori namlik va yomon shamollatish kasallik xavfini oshirishi mumkin.",
        "Issiq paytda havo almashinuvini kuchaytirish kerak bo‘lishi mumkin.",
        "Kechasi ortiqcha namlik yig‘ilib qolmasligiga e’tibor bering.",
        "Sug‘orish rejimini teplitsa ichidagi mikroiqlim bilan birga belgilang.",
    ],

    "o'g'it": [
        "O‘g‘it miqdorini faqat o‘simlik rangiga qarab keskin oshirmang.",
        "Imkon bo‘lsa, tuproq tahlili asosida oziqlantirish rejasini tuzing.",
        "Azotning ortiqchaligi har doim yaxshi hosil degani emas.",
        "O‘g‘itlashda ekinning rivojlanish bosqichini hisobga oling.",
        "Ortiqcha o‘g‘it ildiz zonasidagi tuz konsentratsiyasini oshirishi mumkin.",
    ],

    "tuproq": [
        "Tuproqning mexanik tarkibi sug‘orish rejasiga katta ta’sir qiladi.",
        "Qumli tuproq suvni tezroq o‘tkazishi mumkin.",
        "Og‘ir tuproqda suv uzoqroq saqlanishi mumkin.",
        "Tuproqning zichlashib qolishi ildizlarning rivojlanishiga xalaqit berishi mumkin.",
        "Drenaj muammosi bo‘lsa, faqat sug‘orishni kamaytirish bilan cheklanib qolmaslik kerak.",
    ],
}


# =========================================================
# 6. SAVOL MAQSADINI ANIQLASH
# =========================================================

def detect_intent(text: str) -> str:
    """
    Foydalanuvchi aslida nima so‘rayotganini taxmin qiladi.
    """

    text = normalize_text(text)

    if any(x in text for x in [
        "qachon",
        "когда",
    ]):
        return "when"

    if any(x in text for x in [
        "qancha",
        "necha",
        "сколько",
        "много",
    ]):
        return "amount"

    if any(x in text for x in [
        "nega",
        "nimaga",
        "sababi",
        "почему",
        "отчего",
    ]):
        return "why"

    if any(x in text for x in [
        "qanday",
        "qanaqa",
        "qando",
        "как",
        "что делать",
    ]):
        return "how"

    if any(x in text for x in [
        "mumkinmi",
        "boladimi",
        "bo'ladimi",
        "можно",
    ]):
        return "can"

    return "general"


# =========================================================
# 7. SAVOLGA MOS KIRISH QISMI
# =========================================================

def intent_intro(intent: str) -> str:

    if intent == "when":
        return "🕐 Qachon qilish masalasi bo‘yicha:"

    if intent == "amount":
        return "📏 Miqdor bo‘yicha muhim jihatlar:"

    if intent == "why":
        return "🔎 Mumkin bo‘lgan sabablar:"

    if intent == "how":
        return "🛠 Qanday qilish bo‘yicha:"

    if intent == "can":
        return "✅ Mumkin yoki mumkin emasligini baholashda:"

    return "📌 Muhim jihatlar:"


# =========================================================
# 8. BATAFSIL JAVOB YARATISH
# =========================================================

def build_crop_answer(
    crop_key: str,
    topics: List[str],
    intent: str,
    question: str,
) -> str:

    crop = CROPS[crop_key]
    crop_name = str(crop["name"])
    advice = list(crop["advice"])

    response: List[str] = [
        f"{crop_name}",
        "",
        "🧠 DEHQON AI MASLAHATI",
        "",
    ]

    # Savol mavzusi
    if topics:
        response.append(intent_intro(intent))
        response.append("")

        # Eng muhim mavzularni birinchi chiqaramiz.
        topic_order = [
            "sug'orish",
            "kasallik",
            "zararkunanda",
            "sarg'ayish",
            "so'lish",
            "issiq",
            "sovuq",
            "yomg'ir",
            "teplitsa",
            "o'g'it",
            "tuproq",
        ]

        selected_topics = [
            topic
            for topic in topic_order
            if topic in topics
        ]

        for topic in selected_topics[:3]:
            response.append(
                f"🔸 {topic.replace('_', ' ').upper()}"
            )

            for item in GENERAL_TOPIC_ADVICE.get(topic, [])[:5]:
                response.append(f"• {item}")

            response.append("")

    # Ekin bo‘yicha bilimlar
    response.append("🌱 EKIN BO‘YICHA BATAFSIL:")
    response.append("")

    # Agar topic bor bo‘lsa, umumiy maslahatlarni ham chiqaramiz.
    # Lekin javobni keragidan ortiq cho‘zmaymiz.
    for index, item in enumerate(advice[:18], start=1):
        response.append(f"{index}. {item}")

    response.extend([
        "",
        "⚠️ Eslatma:",
        "Aniq tavsiya ekinning yoshi, tuproq turi, oxirgi sug‘orish vaqti va mahalliy ob-havoga qarab o‘zgarishi mumkin.",
        "",
        "💬 Yanada aniq maslahat uchun savolingizga ekinning holatini qo‘shing.",
        "Masalan: «Barglari sarg‘aygan», «3 kundan beri suv bermadim», «bugun yom‘ir yog‘di»."
    ])

    return "\n".join(response)


# =========================================================
# 9. EKIN TOPILMAGAN HOLAT
# =========================================================

def build_general_answer(
    topics: List[str],
    intent: str,
) -> str:

    response: List[str] = [
        "🧠 DEHQON AI",
        "",
    ]

    if topics:
        response.append(intent_intro(intent))
        response.append("")

        for topic in topics[:3]:
            response.append(
                f"🔸 {topic.replace('_', ' ').upper()}"
            )

            for item in GENERAL_TOPIC_ADVICE.get(topic, [])[:5]:
                response.append(f"• {item}")

            response.append("")

    response.extend([
        "🌱 Aniqroq maslahat uchun ekin nomini ham yozing.",
        "",
        "Masalan:",
        "🍅 pamidorni qachon sugoraman",
        "🥒 bodringga suv beraymi",
        "🥔 картошка почему желтеет",
        "🌶 qalampir bargi sargayib qopti",
        "🌽 makkajo‘xori issiqda nima qilaman",
        "🏡 теплица ichida namlik ko‘p",
    ])

    return "\n".join(response)


# =========================================================
# 10. ASOSIY FUNKSIYA
# =========================================================

def get_ai_advice(question: str) -> str:
    """
    Telegram bot uchun asosiy funksiya.

    main.py:
        answer = get_ai_advice(question)
    """

    if not question or not str(question).strip():
        return (
            "🧠 DEHQON AI\n\n"
            "Savolingizni yozing.\n\n"
            "Masalan:\n"
            "🍅 Pomidor barglari sarg‘ayib qoldi.\n"
            "🥒 bodring qachon sugoriladi?\n"
            "🥔 картошка почему желтеет?\n"
            "🌶 qalampirga suv beraymi?\n"
            "🏡 теплица juda issiq."
        )

    normalized = normalize_text(question)

    crop_key = find_crop(normalized)
    topics = find_topics(normalized)
    intent = detect_intent(normalized)

    # Ekin topilgan bo‘lsa — chuqur javob.
    if crop_key:
        return build_crop_answer(
            crop_key=crop_key,
            topics=topics,
            intent=intent,
            question=question,
        )

    # Ekin topilmasa — umumiy maslahat.
    return build_general_answer(
        topics=topics,
        intent=intent,
    )


# =========================================================
# 11. TEST UCHUN
# =========================================================

if __name__ == "__main__":

    test_questions = [
        "pamidorni qachon sugorish kere",
        "памидор когда поливать",
        "bodring bargi sargayib qopti",
        "картошка почему желтеет",
        "qalampirni issiqda qanaqa qaray",
        "makkajo qachon suv beraman",
        "теплица ichida namlik kop",
        "pomidor yomgir yogandan keyin nima qilay",
    ]

    for question in test_questions:
        print("=" * 70)
        print("SAVOL:", question)
        print()
        print(get_ai_advice(question))
        print()