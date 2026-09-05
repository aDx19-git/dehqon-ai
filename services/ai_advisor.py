from __future__ import annotations

import random
import re
from typing import Any


# =========================================================
# DEHQON AI — EKINLAR BAZASI
# =========================================================

CROPS: dict[str, dict[str, Any]] = {

    # =====================================================
    # POMIDOR
    # =====================================================
    "pomidor": {
        "name": "🍅 Pomidor",
        "aliases": [
            "pomidor", "pamidor", "pomdor", "pomdr", "pomidorni",
            "pamidorni", "помидор", "помидоры", "томат", "томаты"
        ],
        "advice": [
            "Pomidor ildiz zonasida namlikning keskin o‘zgarishini yoqtirmaydi. Tuproq bir necha santimetr chuqurlikda quruqlashganini tekshirib, keyin sug‘orish ma’qul.",
            "Sug‘orishda suvni barglarga sepishdan ko‘ra ildiz atrofiga sekin yetkazish foydaliroq. Nam barglar ayrim zamburug‘ kasalliklari uchun qulay sharoit yaratishi mumkin.",
            "Gullash va meva tugish davrida namlikni bir tekis ushlash muhim. Uzoq quruqlikdan keyin birdaniga ko‘p suv berish mevalarda yorilish xavfini oshirishi mumkin.",
            "Pomidor atrofida begona o‘tlarni nazorat qilish nafaqat oziqa uchun, balki havo aylanishi va zararkunandalarni kuzatish uchun ham muhim.",
            "Pastki barglar tuproqqa tegib tursa, ularni muntazam tekshirib boring. Sarg‘aygan yoki kasallik alomatli barglarni sog‘lom qismdan ajratib kuzatish kerak.",
            "Juda issiq kunlarda pomidorning barglari vaqtincha osilib qolishi mumkin. Avval tuproq namligini tekshiring, keyin qo‘shimcha suv berish haqida qaror qiling.",
            "Teplitsada pomidor gullayotgan paytda havo almashinuvi muhim. Haddan tashqari nam va dim muhit changlanish hamda kasalliklar uchun noqulay bo‘lishi mumkin.",
            "Pomidorni bir joyga yillar davomida ekish tuproqdagi ayrim kasallik va zararkunandalar bosimini oshirishi mumkin. Imkon bo‘lsa almashlab ekishni rejalashtiring.",
            "O‘g‘itni ko‘p berish har doim hosilni oshirmaydi. Ayniqsa azotning ortiqchaligi barg massasini kuchaytirib, meva rivojlanishini muvozanatdan chiqarishi mumkin.",
            "Meva hosil bo‘lish davrida o‘simlikning umumiy holatini, barg rangini va yangi o‘sishlarni birgalikda kuzating. Faqat bitta belgiga qarab o‘g‘it berishga shoshilmang.",
            "Yomg‘irdan keyin pomidor qatorlari orasida suv turib qolsa, drenajni tekshiring. Ildiz zonasining uzoq vaqt suvga to‘yingan bo‘lishi muammo tug‘dirishi mumkin.",
            "Pomidor ko‘chatlarini ko‘chirib o‘tkazgandan keyin dastlabki kunlarda namlikni keskin o‘zgartirmaslik va o‘simlikni asta-sekin yangi sharoitga moslashtirish foydali.",
            "Zararkunanda paydo bo‘lsa, avval barglarning ostki qismini ham tekshiring. Ko‘plab mayda hasharotlar aynan shu joylarda yashirinadi.",
            "Biror kasallikdan shubhalansangiz, zararlangan bargni boshqa o‘simliklarga tekkizmaslik va sug‘orish paytida barglarni ortiqcha ho‘llamaslik yaxshi amaliyot hisoblanadi.",
            "Pomidor uchun eng yaxshi qaror ob-havo, tuproq turi, o‘simlik yoshi va o‘sish bosqichini birga hisobga olgan holda qilinadi."
        ],
    },

    # =====================================================
    # BODRING
    # =====================================================
    "bodring": {
        "name": "🥒 Bodring",
        "aliases": [
            "bodring", "bodreng", "bodringni", "бодринг",
            "огурец", "огурцы", "ogurets"
        ],
        "advice": [
            "Bodring namlik yetishmasligiga sezgir, ammo ildiz atrofida doimiy suv turishi ham foydali emas.",
            "Issiq kunlarda tuproq tez qurishi mumkin. Sug‘orishdan oldin faqat ustki qatlamga emas, ildiz joylashgan qatlamga ham qarang.",
            "Bodring barglarini kechqurun uzoq vaqt nam holda qoldirmaslikka harakat qiling. Havo almashinuvi kasallik xavfini kamaytirishga yordam beradi.",
            "Teplitsada namlik yuqori bo‘lsa, shamollatish ayniqsa muhim. Issiq va dim havo zamburug‘li kasalliklar xavfini oshirishi mumkin.",
            "Bodring meva berayotgan paytda suvning keskin yetishmasligi mevalarning shakli va sifatiga ta’sir qilishi mumkin.",
            "Tuproq yuzasini mulchalash namlikning tez bug‘lanishini kamaytirishga yordam beradi.",
            "Bodringning barglari ostini muntazam tekshiring. Mayda zararkunandalar ko‘pincha aynan shu tomonda ko‘rinadi.",
            "Sarg‘aygan eski barglarni sababini aniqlamasdan ko‘plab o‘g‘it bilan davolashga shoshilmang.",
            "Yom‘g‘irdan keyin tuproq allaqachon nam bo‘lsa, odatdagi sug‘orish jadvalini avtomatik davom ettirmang.",
            "Bodring ildizi yuzaga nisbatan yaqin joylashishi mumkin, shuning uchun tuproqni juda chuqur kovlashda ildizlarni shikastlamang.",
            "Teplitsada kunduzgi issiqlik haddan oshsa, shamollatish vaqtini ob-havoga qarab moslashtiring.",
            "Gullash davrida o‘simlikning umumiy oziqlanishi va namligi barqaror bo‘lishi muhim.",
            "Bodring qatorlari juda zich bo‘lsa, havo aylanishi kamayadi. O‘simliklarni haddan tashqari zichlashtirmaslik foydali.",
            "Kasallik alomati ko‘ringan barglarni muntazam kuzating va sog‘lom o‘simliklarga tegishdan oldin qo‘llarni yoki asboblarni tozalashga e’tibor bering.",
            "Bodringda sug‘orish qarorini kalendar bo‘yicha emas, tuproq namligi va ob-havoga qarab qilish yaxshiroq."
        ],
    },

    # =====================================================
    # SABZI
    # =====================================================
    "sabzi": {
        "name": "🥕 Sabzi",
        "aliases": [
            "sabzi", "sabz", "sabzini", "sabzilar",
            "морковь", "морковка", "моркови"
        ],
        "advice": [
            "Sabzi ildizmevasi tuproq ichida rivojlanadi, shuning uchun tuproqning zichligi uning shakliga katta ta’sir qilishi mumkin.",
            "Juda qattiq yoki toshli tuproqda sabzi ildizi to‘g‘ri va bir xil rivojlanmasligi mumkin.",
            "Urug‘ unib chiqayotgan davrda tuproq yuzasining butunlay qurib qolishiga yo‘l qo‘ymaslik muhim.",
            "Sug‘orishdan keyin tuproq yuzasida qattiq qatlam hosil bo‘lsa, nihollarning chiqishi qiyinlashishi mumkin.",
            "Sabzini juda ko‘p azot bilan oziqlantirish faqat barglarning kuchayishiga olib kelishi mumkin; o‘g‘itni tuproq holatiga qarab tanlash kerak.",
            "Begona o‘tlarni erta nazorat qilish muhim, chunki yosh sabzi nihollari raqobatga sezgir.",
            "Sabzi qatorlarini haddan tashqari zich qoldirmaslik ildizmevalarning kattalashishiga yordam beradi.",
            "Yom‘irdan keyin dalada suv turib qolsa, drenajni tekshiring. Uzoq davom etgan ortiqcha namlik ildizlar uchun muammo bo‘lishi mumkin.",
            "Quruq davrdan keyin birdaniga juda ko‘p suv berish o‘rniga namlikni asta-sekin tiklash ma’qul.",
            "Sabzi dalasida bir xil ekinni ketma-ket ekish ayrim tuproq zararkunandalari bosimini oshirishi mumkin.",
            "Ildizmevalarda yoriqlar paydo bo‘lsa, sug‘orishning keskin o‘zgarishi sabablaridan biri bo‘lishi mumkin.",
            "Sabzi uchun yumshoq, yaxshi drenajlanadigan tuproq ildizning shakllanishi uchun qulay.",
            "Hosilni yig‘ishdan oldin ortiqcha sug‘orishni avtomatik ravishda ko‘paytirish shart emas.",
            "Sabzi barglaridagi o‘zgarishni kuzatish foydali, lekin muammoni aniqlashda tuproq namligi va ildiz holatini ham tekshirish kerak.",
            "Sabzi uchun eng yaxshi parvarish — bir tekis namlik, begona o‘t nazorati, yumshoq tuproq va me’yoriy oziqlantirishning kombinatsiyasidir."
        ],
    },

    # =====================================================
    # KARTOSHKA
    # =====================================================
    "kartoshka": {
        "name": "🥔 Kartoshka",
        "aliases": [
            "kartoshka", "kartoshkani", "kartosh", "картошка",
            "картофель", "картошку"
        ],
        "advice": [
            "Kartoshkada tuproq namligining keskin o‘zgarishi tuganaklarning rivojlanishiga salbiy ta’sir qilishi mumkin.",
            "Gullash va tuganak hosil bo‘lish davrida namlik yetishmasligiga alohida e’tibor bering.",
            "Dalada suv turib qolishi ildiz va tuganaklar uchun noqulay. Drenaj muammosi bo‘lsa, sug‘orishni ko‘paytirish emas, sababni bartaraf etish kerak.",
            "Tuproqni yumshatish va qator orasini begona o‘tlardan tozalash kartoshkaning rivojlanishiga yordam beradi.",
            "Tuganaklar quyoshga chiqib qolsa, yashil rangga kirishi mumkin. Shuning uchun tuproq bilan qoplanganligini kuzating.",
            "Juda issiq ob-havoda tuproq namligini tez-tez tekshirish foydali.",
            "Kartoshkani yillar davomida bir joyga ekish kasallik va zararkunanda bosimini oshirishi mumkin.",
            "Azotni ortiqcha berish poyaning kuchli o‘sishiga olib kelishi mumkin, shuning uchun oziqlantirish muvozanatli bo‘lishi kerak.",
            "Yom‘irdan keyin tuproq nam bo‘lsa, qo‘shimcha sug‘orishni shoshmasdan rejalashtiring.",
            "Kartoshka barglarida dog‘lar paydo bo‘lsa, faqat rangiga emas, dog‘ning shakli va tarqalish tezligiga ham qarang.",
            "Zararkunandalarni erta aniqlash uchun barglarning yuqori va pastki qismini tekshirish foydali.",
            "Tuproq juda zich bo‘lsa, tuganaklarning shakli va kattaligi bir tekis bo‘lmasligi mumkin.",
            "Sug‘orish jadvalini faqat kun sanog‘iga qarab emas, ob-havo va tuproq namligiga qarab moslang.",
            "Hosil yig‘ishdan oldin o‘simlikning poyasi va barglari holatini kuzatish yig‘im vaqtini rejalashtirishga yordam beradi.",
            "Kartoshkada yuqori hosil uchun suvning o‘zi yetarli emas: sog‘lom urug‘lik, almashlab ekish, tuproq va zararkunanda nazorati birgalikda muhim."
        ],
    },

    # =====================================================
    # PIYOZ
    # =====================================================
    "piyoz": {
        "name": "🧅 Piyoz",
        "aliases": [
            "piyoz", "piyozni", "пиёз", "лук", "луковица"
        ],
        "advice": [
            "Piyoz ildiz zonasida ortiqcha suv turib qolishini yoqtirmaydi.",
            "Yosh nihollar davrida begona o‘tlarni nazorat qilish ayniqsa muhim.",
            "Piyozning bosh hosil qilishi davrida suv rejimining keskin o‘zgarishidan saqlanish foydali.",
            "Yom‘irdan keyin tuproq namligini tekshirib, odatdagi sug‘orishni avtomatik davom ettirmang.",
            "Piyoz barglarida sarg‘ayish ko‘rinsa, darhol o‘g‘it bermasdan avval namlik, ildiz va zararkunandalarni tekshiring.",
            "Juda zich ekish havo almashinuvini kamaytirishi mumkin.",
            "Azotning ortiqcha miqdori barg o‘sishini kuchaytirishi mumkin.",
            "Hosil pishishiga yaqin namlikni boshqarish muhim, chunki ortiqcha namlik saqlanish sifatiga ta’sir qilishi mumkin.",
            "Piyoz uchun yaxshi drenajlanadigan tuproq foydali.",
            "Piyoz ekilgan joyda suv turib qolsa, sug‘orishni ko‘paytirish muammoni kuchaytirishi mumkin.",
            "Zararkunandalarni aniqlash uchun barglarning bukilgan va ichki qismlarini ham tekshiring.",
            "Almashlab ekish tuproqdagi ayrim muammolarni kamaytirishga yordam beradi.",
            "Quruq va issiq ob-havoda yosh piyozning tuproq namligini tez-tez tekshirish kerak.",
            "Hosil yig‘ilgach, piyozni yaxshi shamollatiladigan sharoitda quritish saqlanish sifatini yaxshilaydi.",
            "Piyozda parvarish qarorini o‘simlikning yoshiga, tuproq turiga va ob-havoga qarab o‘zgartirish kerak."
        ],
    },

    # =====================================================
    # SARIMSOQ
    # =====================================================
    "sarimsoq": {
        "name": "🧄 Sarimsoq",
        "aliases": [
            "sarimsoq", "sarimsoqni", "саримсоқ",
            "чеснок", "чеснока"
        ],
        "advice": [
            "Sarimsoq uchun yaxshi drenaj muhim, chunki doimiy ortiqcha namlik ildiz zonasiga zarar yetkazishi mumkin.",
            "Vegetatsiya boshida tuproq namligini barqaror ushlash foydali.",
            "Hosil pishishiga yaqin ortiqcha sug‘orishni kamaytirish ayrim sharoitlarda saqlanish sifatiga yordam beradi.",
            "Begona o‘tlarni erta yo‘qotish sarimsoqning oziqa va suv uchun raqobatini kamaytiradi.",
            "Barglarning sarg‘ayishi har doim azot yetishmasligini anglatmaydi; tabiiy pishish jarayoni ham shunday ko‘rinishi mumkin.",
            "Sarimsoq ekilgan joyda suv to‘planmasligini tekshiring.",
            "Almashlab ekish tuproqdagi kasallik bosimini kamaytirishga yordam berishi mumkin.",
            "Zich ekish havo aylanishini kamaytirishi mumkin.",
            "Juda issiq kunlarda tuproq namligini tekshirib, sug‘orishni shunga qarab moslang.",
            "Yom‘irdan keyin qo‘shimcha suv berishga shoshilmang.",
            "Barglarda dog‘lar paydo bo‘lsa, ularning qayerdan boshlanganini va tez tarqalayotganini kuzating.",
            "Sarimsoqni yig‘ishdan oldin boshlarning rivojlanishi va barglarning tabiiy qurishini hisobga olish kerak.",
            "Hosildan keyin yaxshi shamollatish sarimsoqni saqlashda muhim.",
            "O‘g‘it miqdorini faqat o‘simlikning tashqi ko‘rinishiga qarab oshirmang.",
            "Sarimsoq uchun namlik, drenaj, tuproq unumdorligi va almashlab ekish birgalikda boshqarilganda natija yaxshiroq bo‘ladi."
        ],
    },

    # =====================================================
    # QALAMPIR
    # =====================================================
    "qalampir": {
        "name": "🫑 Qalampir",
        "aliases": [
            "qalampir", "qalampirni", "bolgar qalampiri",
            "bulg'or qalampiri", "перец", "болгарский перец"
        ],
        "advice": [
            "Qalampir issiqsevar ekin bo‘lib, keskin sovuq sharoitda o‘sishi sekinlashishi mumkin.",
            "Tuproq namligini keskin o‘zgartirmaslik gullash va meva hosil bo‘lish davrida ayniqsa muhim.",
            "Juda issiq kunlarda tuproq tez qurishi mumkin, shuning uchun namlikni qo‘l bilan tekshirib turing.",
            "Barglarni doimiy namlab sug‘orishdan ko‘ra ildiz zonasini namlash ma’qul.",
            "Teplitsada ortiqcha namlik va yomon havo almashinuvi kasallik xavfini oshirishi mumkin.",
            "Azotni haddan tashqari ko‘paytirish vegetativ o‘sishni kuchaytirishi mumkin.",
            "Meva hosil bo‘lish davrida o‘simlikning suv va oziqa holatini barqaror saqlash foydali.",
            "Barglarning pastki qismini zararkunandalar uchun muntazam tekshiring.",
            "Yom‘irdan keyin tuproq namligini tekshirib, sug‘orishni shunga qarab belgilang.",
            "Qalampir ildizlari shikastlanmasligi uchun qator orasini juda chuqur kovlamang.",
            "Ko‘chatni yangi joyga o‘tkazganda dastlabki davrda namlik va quyosh ta’sirini kuzatish kerak.",
            "Keskin issiqdan keyin o‘simlikni faqat ko‘rinishiga qarab ortiqcha sug‘orishdan saqlaning.",
            "Kasallik belgilari ko‘rinsa, zararlangan barglarni kuzatib, havo aylanishini yaxshilang.",
            "Hosilni muntazam yig‘ib turish ayrim navlarda yangi mevalarning rivojlanishiga yordam beradi.",
            "Qalampir parvarishida nav xususiyati, tuproq, ob-havo va o‘simlikning rivojlanish bosqichi birga hisobga olinishi kerak."
        ],
    },

    # =====================================================
    # BAQLAJON
    # =====================================================
    "baqlajon": {
        "name": "🍆 Baqlajon",
        "aliases": [
            "baqlajon", "baqlajonni", "баклажан",
            "баклажаны", "баклажанни"
        ],
        "advice": [
            "Baqlajon issiq sharoitni yaxshi ko‘radi, sovuqda o‘sishi sekinlashishi mumkin.",
            "Tuproq namligini bir tekis saqlash gullash va meva hosil bo‘lishida muhim.",
            "Ildiz zonasida suv turib qolmasligi uchun drenajni tekshiring.",
            "Juda issiq kunlarda sug‘orishdan oldin tuproq namligini tekshirish kerak.",
            "Barglarning pastki qismini zararkunandalar uchun tekshirib turing.",
            "Teplitsada shamollatish havo namligini boshqarishga yordam beradi.",
            "Azotning ortiqcha berilishi barg va poyaning haddan tashqari o‘sishiga olib kelishi mumkin.",
            "Yom‘irdan keyin qo‘shimcha sug‘orishga shoshilmang.",
            "Meva tugish davrida namlikning keskin o‘zgarishi o‘simlikka stress berishi mumkin.",
            "O‘simliklar orasida yetarli havo almashinuvi bo‘lishi foydali.",
            "Ko‘chatni ko‘chirib o‘tkazishda ildizlarni imkon qadar kam bezovta qilish kerak.",
            "Barglarda dog‘ paydo bo‘lsa, ularning shakli va tarqalishiga e’tibor bering.",
            "Begona o‘tlar suv va oziqa uchun raqobat qiladi, ayniqsa yosh o‘simliklarda.",
            "Hosilni haddan tashqari kechiktirmaslik ayrim navlarda sifatni saqlashga yordam beradi.",
            "Baqlajonda parvarishning asosiy nuqtalari — issiqlik, barqaror namlik, drenaj va zararkunandalarni erta aniqlash."
        ],
    },

    # =====================================================
    # KARAM
    # =====================================================
    "karam": {
        "name": "🥬 Karam",
        "aliases": [
            "karam", "karamni", "капуста", "капусту"
        ],
        "advice": [
            "Karam barg massasi katta bo‘lgani uchun vegetatsiya davrida yetarli namlikka ehtiyoj sezadi.",
            "Tuproqning doimiy suvga to‘yingan bo‘lishi ildizlar uchun zararli.",
            "Yosh karamda begona o‘tlarni erta nazorat qilish muhim.",
            "Barglarning ichki va tashqi qismini zararkunandalar uchun muntazam tekshiring.",
            "Karam kapalagi va boshqa zararkunandalar tuxumlarini erta aniqlash katta zarar oldini olishga yordam beradi.",
            "Yom‘irdan keyin qo‘shimcha sug‘orishni tuproq namligiga qarab belgilang.",
            "Juda issiq kunlarda namlikni muntazam kuzatish kerak.",
            "Karam uchun tuproqning unumdorligi muhim, ammo o‘g‘it miqdorini tuproq holatiga moslashtirish kerak.",
            "Juda zich ekish havo almashinuvini kamaytirishi mumkin.",
            "Karam bosh hosil qilayotgan davrda namlikning keskin o‘zgarishi sifatga ta’sir qilishi mumkin.",
            "Almashlab ekish tuproqdagi ayrim kasallik va zararkunandalar bosimini kamaytirishga yordam beradi.",
            "Barglar sarg‘aysa, namlik, ildiz holati va oziqa muammolarini birgalikda tekshiring.",
            "Kasallangan barglarni uzoq vaqt dalada qoldirmaslik foydali.",
            "Tuproq yuzasini mulchalash namlikni ushlab turishga yordam berishi mumkin.",
            "Karamda yaxshi natija uchun suv, oziqa, havo almashinuvi va zararkunanda nazoratini birgalikda boshqaring."
        ],
    },

    # =====================================================
    # BUG‘DOY
    # =====================================================
    "bug'doy": {
        "name": "🌾 Bug‘doy",
        "aliases": [
            "bug'doy", "bug‘doy", "bugdoy", "bugdoyni",
            "бугдой", "пшеница", "пшеницу"
        ],
        "advice": [
            "Bug‘doyda namlik ehtiyoji o‘sish bosqichiga qarab o‘zgaradi; barcha davrda bir xil sug‘orish talab qilinmaydi.",
            "Yom‘irdan keyin dalada suv turib qolsa, drenaj holatini tekshiring.",
            "Nihollik davrida begona o‘tlar bilan raqobatni kamaytirish muhim.",
            "Azotli oziqlantirishni faqat o‘simlik rangiga qarab emas, tuproq va rivojlanish bosqichiga qarab rejalashtirish ma’qul.",
            "Juda zich ekin maydonida havo almashinuvi kamayishi mumkin.",
            "Issiq va quruq davrda tuproq namligi hosil shakllanishiga ta’sir qilishi mumkin.",
            "Kasalliklarni erta aniqlash uchun barglarning yuqori va pastki qismlarini kuzatish foydali.",
            "Almashlab ekish tuproq unumdorligi va ayrim kasalliklarni boshqarishda yordam beradi.",
            "Urug‘lik sifati kelajakdagi nihol zichligi va ekin bir xilligiga ta’sir qiladi.",
            "Kuchli yom‘irdan keyin tuproq qobig‘i hosil bo‘lsa, nihollarning chiqishiga ta’sir qilishi mumkin.",
            "Shamolli sharoitda tuproq namligi tezroq kamayishi mumkin.",
            "Hosilga yaqin davrda ortiqcha sug‘orish har doim foydali emas; ob-havo va pishish bosqichini hisobga olish kerak.",
            "Daladagi ayrim joylarda o‘sish sust bo‘lsa, butun maydonga bir xil o‘g‘it berishdan oldin sababni aniqlang.",
            "Zararkunanda soni ko‘payayotgan bo‘lsa, tarqalish maydonini kuzatish va iqtisodiy zarar chegarasini hisobga olish foydali.",
            "Bug‘doyda hosilni faqat o‘g‘it bilan emas, urug‘lik, ekish muddati, namlik, begona o‘t va kasallik nazorati bilan birgalikda boshqarish kerak."
        ],
    },

    # =====================================================
    # MAKKAJO‘XORI
    # =====================================================
    "makkajo'xori": {
        "name": "🌽 Makkajo‘xori",
        "aliases": [
            "makkajo'xori", "makkajo‘xori", "makkajoxori",
            "makkajo", "кукуруза", "кукурузу"
        ],
        "advice": [
            "Makkajo‘xorida suvga ehtiyoj o‘sish bosqichiga qarab o‘zgaradi.",
            "Gullash va don shakllanish davrida namlik tanqisligiga alohida e’tibor berish kerak.",
            "Juda issiq kunlarda tuproq namligini muntazam tekshiring.",
            "Yom‘irdan keyin qo‘shimcha sug‘orishni tuproq holatiga qarab belgilang.",
            "Dalada suv turib qolishi ildizlar uchun muammo bo‘lishi mumkin.",
            "Yosh makkajo‘xorida begona o‘tlar bilan raqobat hosilga sezilarli ta’sir qilishi mumkin.",
            "Azotli oziqlantirishni o‘simlikning rivojlanish bosqichiga moslashtirish foydali.",
            "Shamol kuchli bo‘ladigan hududlarda o‘simliklarning yotib qolish xavfini hisobga oling.",
            "Tuproq yuzasida qattiq qatlam hosil bo‘lsa, yosh nihollarning chiqishini kuzating.",
            "Kasallik yoki zararkunanda alomatlari ko‘ringanda butun dalani emas, avval zararlangan joylarning tarqalishini baholang.",
            "Makkajo‘xori uchun tuproq unumdorligi va ildiz rivojlanishi muhim.",
            "Almashlab ekish tuproq va kasalliklarni boshqarishga yordam beradi.",
            "Quruq davrdan keyin birdaniga haddan tashqari ko‘p suv berish o‘rniga namlikni me’yorida tiklash ma’qul.",
            "Hosilga yaqin davrda ob-havo va donning pishish holatini birga kuzating.",
            "Makkajo‘xorida eng muhim boshqaruv nuqtalari — namlik, begona o‘t, oziqlanish va gullash davridagi stressni kamaytirish."
        ],
    },

    # =====================================================
    # TARVUZ
    # =====================================================
    "tarvuz": {
        "name": "🍉 Tarvuz",
        "aliases": [
            "tarvuz", "tarvuzni", "арбуз", "арбузы"
        ],
        "advice": [
            "Tarvuz issiqsevar ekin bo‘lib, sovuq tuproqda boshlang‘ich rivojlanishi sekinlashishi mumkin.",
            "Meva kattalashayotgan davrda namlik muhim, ammo suv turib qolishi ildizlar uchun zararli.",
            "Yom‘irdan keyin sug‘orishni tuproq namligiga qarab belgilang.",
            "Meva pishishiga yaqin sug‘orish rejimini ob-havo va tuproq holatiga moslashtirish kerak.",
            "Juda quruq davrdan keyin birdaniga ko‘p suv berish mevalarning yorilish xavfini oshirishi mumkin.",
            "Tarvuzda begona o‘tlarni erta nazorat qilish muhim.",
            "Barglarning ostini zararkunandalar uchun tekshiring.",
            "Tez-tez barglarni ho‘llashdan ko‘ra ildiz zonasini sug‘orish ma’qul.",
            "Tuproqni mulchalash namlikning bug‘lanishini kamaytirishi mumkin.",
            "O‘g‘itni ortiqcha berish meva sifatini har doim yaxshilamaydi.",
            "Bir joyda takroriy ekish ayrim tuproq kasalliklari bosimini oshirishi mumkin.",
            "Meva yotgan joyda doimiy ortiqcha namlik bo‘lmasligiga e’tibor bering.",
            "Kuchli shamol va issiqda barglarning holatini kuzating.",
            "Mevaning pishish belgilarini faqat bitta belgiga qarab emas, bir nechta belgini birgalikda baholab aniqlash yaxshiroq.",
            "Tarvuzda hosil sifati uchun issiqlik, ildiz zonasidagi namlik, tuproq va o‘simlikning oziqlanishini birga boshqarish kerak."
        ],
    },

    # =====================================================
    # QOVUN
    # =====================================================
    "qovun": {
        "name": "🍈 Qovun",
        "aliases": [
            "qovun", "qovunni", "дыня", "дыни"
        ],
        "advice": [
            "Qovun issiqsevar ekin bo‘lib, quyosh va issiqlik yetarli bo‘lishi muhim.",
            "O‘sish davrida namlik kerak, ammo ildiz zonasida suv turib qolmasligi kerak.",
            "Meva rivojlanayotgan davrda quruqlik stressini kamaytirish foydali.",
            "Meva pishishiga yaqin suv rejimini ob-havo va tuproq namligiga qarab moslang.",
            "Yom‘irdan keyin qo‘shimcha sug‘orishga shoshilmang.",
            "Begona o‘tlar yosh qovun nihollari bilan suv va oziqa uchun raqobat qiladi.",
            "Barglarning pastki qismini zararkunandalar uchun muntazam tekshiring.",
            "Mulcha tuproq namligini saqlashga yordam berishi mumkin.",
            "Juda zich o‘sish havo almashinuvini kamaytirishi mumkin.",
            "Kasallik alomatlari ko‘ringan barglarni muntazam kuzatib boring.",
            "Azotning ortiqcha miqdori vegetativ o‘sishni kuchaytirishi mumkin.",
            "Quruq davrdan keyin keskin sug‘orish rejimi o‘zgarishidan saqlanish foydali.",
            "Tuproqning drenaji yomon bo‘lsa, sug‘orishni ko‘paytirish muammoni hal qilmaydi.",
            "Hosilga yaqin davrda ob-havo va mevaning pishish belgilarini birgalikda kuzating.",
            "Qovunda sifatli hosil uchun issiqlik, namlikning barqarorligi, yaxshi drenaj va zararkunanda nazorati muhim."
        ],
    },

    # =====================================================
    # QULUPNAY
    # =====================================================
    "qulupnay": {
        "name": "🍓 Qulupnay",
        "aliases": [
            "qulupnay", "qulubnay", "qulupnayni",
            "клубника", "клубнику", "земляника"
        ],
        "advice": [
            "Qulupnay ildizlari nisbatan yuza joylashishi sababli tuproq namligini tez-tez kuzatish foydali.",
            "Namlik yetishmasligi gullash va meva kattalashishiga ta’sir qilishi mumkin.",
            "Ortiqcha namlik esa ildiz kasalliklari xavfini oshirishi mumkin.",
            "Mevalarni uzoq vaqt nam qoldirmaslikka harakat qiling.",
            "Somon yoki boshqa mos mulch mevalarning tuproqqa tegishini kamaytirishga yordam beradi.",
            "Qator orasidagi begona o‘tlarni nazorat qilish muhim.",
            "Barglarning pastki qismini zararkunandalar uchun tekshiring.",
            "Yom‘irdan keyin sug‘orishni tuproq namligiga qarab belgilang.",
            "Qulupnay ekilgan joyda suv turib qolsa, drenajni yaxshilang.",
            "Kasallangan barglarni muntazam kuzatib, o‘simliklar orasida havo aylanishiga e’tibor bering.",
            "Bir joyda juda uzoq vaqt yetishtirish kasallik va zararkunanda bosimini oshirishi mumkin.",
            "O‘g‘itni me’yoridan ortiq berish barg o‘sishini kuchaytirib, meva sifatiga salbiy ta’sir qilishi mumkin.",
            "Issiq davrda mulch tuproq harorati va namligini barqarorlashtirishga yordam beradi.",
            "Hosilni muntazam yig‘ish pishgan mevalarning dalada ortiqcha qolib ketishining oldini oladi.",
            "Qulupnayda namlik, drenaj, havo almashinuvi va mevalarni quruq saqlash juda muhim."
        ],
    },

    # =====================================================
    # UZUM
    # =====================================================
    "uzum": {
        "name": "🍇 Uzum",
        "aliases": [
            "uzum", "uzumni", "виноград", "виноградник"
        ],
        "advice": [
            "Uzumda sug‘orish rejimi nav, tuproq va ob-havoga qarab o‘zgaradi.",
            "Gullash va meva shakllanish davrida o‘simlik stressini kamaytirish muhim.",
            "Yom‘irdan keyin qo‘shimcha sug‘orishdan oldin tuproq namligini tekshiring.",
            "Tokzor ichida havo aylanishi yaxshi bo‘lishi barglarning uzoq vaqt nam qolishini kamaytiradi.",
            "Juda zich barg massasini nazorat qilish quyosh nuri va havo almashinuviga yordam beradi.",
            "Kasallik va zararkunandalarni barglarning ikki tomonida tekshiring.",
            "Azotni ortiqcha berish haddan tashqari vegetativ o‘sishni kuchaytirishi mumkin.",
            "Tuproqda suv turib qolmasligi uchun drenaj holatini kuzating.",
            "Meva pishish davrida suv rejimining keskin o‘zgarishidan saqlanish foydali.",
            "Tokni kesish va shakllantirish ishlarini nav va o‘sish kuchiga moslashtirish kerak.",
            "Quruq va issiq davrda yosh toklar alohida nazorat talab qilishi mumkin.",
            "Begona o‘tlar suv va oziqa uchun raqobat qiladi.",
            "Hosil zichligi juda yuqori bo‘lsa, havo almashinuvi va meva sifati bilan bog‘liq muammolar paydo bo‘lishi mumkin.",
            "Yom‘g‘irli davrda kasallik alomatlarini tez-tez kuzatish foydali.",
            "Uzumchilikda sug‘orish, kesish, barg massasini boshqarish, tuproq va kasallik nazoratini bir tizim sifatida olib borish kerak."
        ],
    },

    # =====================================================
    # MEVALI DARAXTLAR
    # =====================================================
    "mevali daraxtlar": {
        "name": "🍎 Mevali daraxtlar",
        "aliases": [
            "mevali daraxt", "mevali daraxtlar", "olma", "olmani",
            "nok", "nokni", "shaftoli", "shaftolini",
            "o'rik", "o‘rik", "olcha", "gilos",
            "яблоня", "яблоню", "груша", "персик",
            "абрикос", "вишня"
        ],
        "advice": [
            "Mevali daraxtlarda sug‘orish faqat daraxt tanasi yoniga ozgina suv berish bilan cheklanmasligi kerak; ildizlar tarqalgan zona ham hisobga olinadi.",
            "Yosh daraxtlarning ildiz tizimi hali kichik bo‘lgani uchun issiq va quruq davrda alohida kuzatuv kerak.",
            "Yom‘irdan keyin qo‘shimcha sug‘orishdan oldin tuproq namligini tekshiring.",
            "Daraxt tagida suv doimiy turib qolsa, drenaj muammosini tekshirish kerak.",
            "Azotni ko‘p berish meva o‘rniga kuchli barg va novda o‘sishini rag‘batlantirishi mumkin.",
            "Meva tugish davrida namlikning keskin yetishmasligi hosilning rivojlanishiga ta’sir qilishi mumkin.",
            "Daraxtning tanasi va asosiy shoxlarini zararkunandalar va kasallik alomatlari uchun tekshirib turing.",
            "Quruq shoxlarni o‘z vaqtida olib tashlash daraxt tojining sog‘lom shakllanishiga yordam beradi.",
            "Toj juda zich bo‘lsa, ichki qismlarga havo va yorug‘lik kamroq kirishi mumkin.",
            "Mulchalash ildiz zonasida namlikni saqlashga yordam beradi, ammo mulchni daraxt tanasiga bevosita bosib qo‘ymaslik kerak.",
            "Meva hosili juda ko‘p bo‘lsa, ayrim daraxtlarda mevalarni me’yorlash foydali bo‘lishi mumkin.",
            "Kuchli shamol, issiq yoki sovuqdan keyin yangi novdalar va barglarning holatini tekshiring.",
            "Mevali daraxtni bir marta ko‘rib, butun muammoni aniqlash qiyin; barg, novda, meva, tuproq va ildiz zonasini birgalikda baholash kerak.",
            "Kasallik yoki zararkunanda gumoni bo‘lsa, alomatlarning qachondan boshlanganini va qaysi shoxlarda ko‘proq ekanini kuzating.",
            "Mevali daraxtlarda hosil sifati uchun sug‘orish, kesish, oziqlantirish, tuproq, changlanish va kasallik nazoratini birgalikda boshqarish kerak."
        ],
    },
}


# =========================================================
# NORMALIZATSIYA
# =========================================================

def normalize_text(text: str) -> str:
    """
    Foydalanuvchi yozgan matnni qidirish uchun
    soddalashtirilgan ko‘rinishga keltiradi.
    """

    text = text.lower().strip()

    replacements = {
        "’": "'",
        "‘": "'",
        "ʻ": "'",
        "`": "'",
        "´": "'",
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    # Ruscha/uzbekcha yozuvdagi ayrim farqlar
    text = text.replace("ё", "е")

    # Ortiqcha belgilarni bo‘sh joyga aylantirish
    text = re.sub(r"[^\w\s']", " ", text, flags=re.UNICODE)

    # Bir nechta bo‘sh joyni bittaga tushirish
    text = re.sub(r"\s+", " ", text).strip()

    return text


# =========================================================
# EKINNI ANIQLASH
# =========================================================

def detect_crop(question: str) -> str | None:
    text = normalize_text(question)

    # Avval uzun aliaslarni tekshiramiz
    aliases: list[tuple[str, str]] = []

    for crop_key, crop_data in CROPS.items():
        for alias in crop_data["aliases"]:
            aliases.append((normalize_text(alias), crop_key))

    aliases.sort(key=lambda item: len(item[0]), reverse=True)

    for alias, crop_key in aliases:
        if not alias:
            continue

        # So‘z ichidan qidirish
        if re.search(rf"(?<!\w){re.escape(alias)}(?!\w)", text):
            return crop_key

    return None


# =========================================================
# SAVOL TURINI ANIQLASH
# =========================================================

def detect_topic(question: str) -> str:
    text = normalize_text(question)

    topics = {
        "watering": [
            "sugor", "sug'or", "suv", "namlik",
            "полив", "поливать", "вода", "влажность"
        ],
        "rain": [
            "yomgir", "yomg'ir", "yomg'ir", "yomgirli",
            "дождь", "дождик"
        ],
        "heat": [
            "issiq", "issiqda", "jazirama", "harorat",
            "qizib", "жара", "жарко", "температура"
        ],
        "cold": [
            "sovuq", "sovuqda", "muz", "sovuq tush",
            "холод", "мороз"
        ],
        "disease": [
            "kasallik", "kasal", "dog", "dog'lar",
            "sargay", "sarg'ay", "chir", "zamburug",
            "болезнь", "болеет", "пятна", "гниль", "грибок"
        ],
        "pest": [
            "zararkunanda", "hasharot", "qurt", "kana",
            "shira", "kapalak", "вредитель", "насекомое",
            "червь", "клещ", "тля"
        ],
        "fertilizer": [
            "ogit", "o'g'it", "oziqa", "azot",
            "fosfor", "kaliy", "удобрение", "азот",
            "калий", "фосфор"
        ],
        "soil": [
            "tuproq", "yer", "dala", "unumdor",
            "почва", "земля", "грунт"
        ],
    }

    for topic, keywords in topics.items():
        for keyword in keywords:
            if normalize_text(keyword) in text:
                return topic

    return "general"


# =========================================================
# MAVZUGA MOS MASLAHATNI TANLASH
# =========================================================

def get_relevant_advice(
    crop_key: str,
    topic: str,
    limit: int = 5,
) -> list[str]:

    crop = CROPS[crop_key]
    advice = crop["advice"]

    # Har bir maslahatni topic bo‘yicha taxminiy kalit so‘zlar bilan
    # moslashtirishga harakat qilamiz.
    topic_keywords = {
        "watering": [
            "namlik", "sug‘or", "sug'or", "suv", "quruq"
        ],
        "rain": [
            "yom‘ir", "yomg‘ir", "yomg'ir", "yomgir", "nam"
        ],
        "heat": [
            "issiq", "harorat", "bug‘lan", "bug'lan"
        ],
        "cold": [
            "sovuq", "muz", "harorat"
        ],
        "disease": [
            "kasallik", "zamburug", "dog", "sarg‘ay",
            "sarg'ay", "chir", "nam"
        ],
        "pest": [
            "zararkunanda", "hasharot", "qurt", "kana",
            "shira", "kapalak"
        ],
        "fertilizer": [
            "o‘g‘it", "o'g'it", "azot", "oziqa"
        ],
        "soil": [
            "tuproq", "drenaj", "begona", "mulch"
        ],
    }

    if topic == "general":
        selected = random.sample(
            advice,
            min(limit, len(advice))
        )
        return selected

    keywords = topic_keywords.get(topic, [])

    relevant = [
        item
        for item in advice
        if any(
            normalize_text(keyword) in normalize_text(item)
            for keyword in keywords
        )
    ]

    # Yetarli maslahat topilmasa umumiy maslahatdan to‘ldiramiz
    if len(relevant) < limit:
        remaining = [
            item
            for item in advice
            if item not in relevant
        ]

        random.shuffle(remaining)
        relevant.extend(remaining)

    random.shuffle(relevant)

    return relevant[:limit]


# =========================================================
# ASOSIY AI MASLAHAT FUNKSIYASI
# =========================================================

def get_ai_advice(question: str) -> str:
    """
    Dehqon AI uchun asosiy maslahat funksiyasi.

    Foydalanuvchi:
    - o‘zbekcha
    - ruscha
    - qisqartirib
    - xato yozib
    - emoji bilan
    yozsa ham ekinni aniqlashga harakat qiladi.
    """

    original_question = question.strip()

    if not original_question:
        return (
            "🌱 <b>DEHQON AI</b>\n\n"
            "Savolingizni yozing.\n\n"
            "Masalan:\n"
            "🍅 pamidorni qachon sugoray?\n"
            "🥕 sabziga qancha suv kerak?\n"
            "🥒 bodringim sargayapti\n"
            "🥔 kartoshkaga yomgir yog'sa nima qilaman?\n"
            "🌾 bugdoyga ogit kerakmi?"
        )

    crop_key = detect_crop(original_question)

    if crop_key is None:
        return (
            "🧠 <b>DEHQON AI</b>\n\n"
            "Savolingizni tushunishga harakat qildim, "
            "lekin qaysi ekin haqida gapirayotganingizni aniqlay olmadim.\n\n"
            "🌱 Masalan:\n"
            "🍅 pamidorni sugorish kerakmi?\n"
            "🥕 sabzi sargayapti\n"
            "🥒 bodringda dog paydo bo'ldi\n"
            "🥔 kartoshkaga yomgir yogdi\n"
            "🌾 bugdoyga qaysi ogit kerak?\n\n"
            "💡 Ekin nomini oddiy yoki qisqartirib yozishingiz mumkin."
        )

    crop = CROPS[crop_key]
    topic = detect_topic(original_question)

    selected_advice = get_relevant_advice(
        crop_key=crop_key,
        topic=topic,
        limit=5,
    )

    topic_titles = {
        "watering": "💧 SUG‘ORISH",
        "rain": "🌧 YOMG‘IR",
        "heat": "🔥 ISSIQ OB-HAVO",
        "cold": "❄️ SOVUQ OB-HAVO",
        "disease": "🦠 KASALLIK",
        "pest": "🐛 ZARARKUNANDA",
        "fertilizer": "🌱 OZIQLANTIRISH",
        "soil": "🌍 TUPROQ",
        "general": "🌱 PARVARISH",
    }

    title = topic_titles.get(topic, "🌱 PARVARISH")

    result = (
        f"{crop['name']}\n\n"
        f"<b>{title}</b>\n\n"
    )

    for index, advice in enumerate(selected_advice, start=1):
        result += f"{index}. {advice}\n\n"

    result += (
        "━━━━━━━━━━━━━━\n"
        "🧠 <b>Dehqon AI tavsiyasi</b>\n"
        "Maslahat ob-havo, tuproq turi, ekinning yoshi "
        "va rivojlanish bosqichiga qarab o‘zgarishi mumkin.\n\n"
        "📌 Aniqroq maslahat uchun ekinning holatini "
        "ham yozing: masalan, <i>“pamidor bargi sarg‘ayapti”</i>."
    )

    return result


# =========================================================
# EKINLAR RO‘YXATI
# =========================================================

def get_crop_list() -> list[tuple[str, str]]:
    """Menyu uchun barcha ekinlarni qaytaradi."""
    return [
        (crop_key, crop_data["name"])
        for crop_key, crop_data in CROPS.items()
    ]       