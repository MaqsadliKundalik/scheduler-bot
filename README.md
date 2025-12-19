# 🤖 Schedule Bot

Telegram bot foydalanuvchilarga vaqtga qarab avtomatik xabarlar yuborish uchun. Bot foydalanuvchilarni ro'yxatdan o'tkazadi va admin tomonidan belgilangan vaqtdan keyin ularga xabarlar yuboradi.

## ✨ Xususiyatlar

### 👤 Foydalanuvchilar uchun
- ✅ **Ro'yxatdan o'tish** - Ism va telefon raqam bilan avtomatik ro'yxatga olish
- 📱 **Telefon raqam validatsiya** - O'zbekiston barcha operator kodlarini qo'llab-quvvatlash
- 📬 **Avtomatik xabarlar** - Belgilangan vaqtda xabar qabul qilish

### 👨‍💼 Admin uchun
- 📢 **Post yuborish** (`/post`) - Barcha foydalanuvchilarga bir vaqtda xabar yuborish
- ⏰ **Rejalashtirilgan postlar** (`/schedule`) - Vaqtga qarab xabar yuborish
- 📊 **Ma'lumotlarni eksport** (`/data`) - Foydalanuvchilar ro'yxatini Excel formatida yuklab olish
- 👀 **Postlarni ko'rish** (`/scheduled_posts`) - Barcha rejalashtirilgan postlarni ko'rish va boshqarish
- 🗑️ **Postlarni o'chirish** - Kerak bo'lmagan postlarni o'chirish

## 🚀 O'rnatish

### 1️⃣ Talablar
- Python 3.10 yoki yuqori
- pip (Python package manager)

### 2️⃣ Repository'ni klonlash
```bash
git clone <repository-url>
cd schedule-bot
```

### 3️⃣ Virtual environment yaratish
```bash
# Windows
python -m venv myenv
myenv\Scripts\activate

# Linux/Mac
python3 -m venv myenv
source myenv/bin/activate
```

### 4️⃣ Kerakli kutubxonalarni o'rnatish
```bash
pip install -r requirements.txt
```

Yoki qo'lda o'rnatish:
```bash
pip install aiogram==3.23.0
pip install tortoise-orm==0.25.2
pip install aiosqlite==0.20.0
pip install python-dotenv==1.2.1
pip install openpyxl
```

### 5️⃣ Konfiguratsiya
`.env` fayl yaratish va quyidagi ma'lumotlarni kiritish:

```env
BOT_TOKEN=your_bot_token_here
ADMIN_ID=your_telegram_id
```

**Bot token olish:**
1. [@BotFather](https://t.me/BotFather) ga murojaat qiling
2. `/newbot` buyrug'ini yuboring
3. Bot nomi va username'ini kiriting
4. Token'ni oling va `.env` fayliga qo'ying

**Admin ID olish:**
1. [@userinfobot](https://t.me/userinfobot) ga `/start` yuboring
2. O'z Telegram ID'ingizni oling

## 📂 Loyiha strukturasi

```
schedule-bot/
├── bot.py                  # Asosiy bot fayli
├── config.py               # Konfiguratsiya
├── states.py               # FSM state'lar
├── filters.py              # Custom filterlar
├── msges.py               # Xabar matnlari
├── models/                # Database modellari
│   ├── __init__.py
│   ├── users.py          # Foydalanuvchi modeli
│   └── admin.py          # Post va ViewsPosts modellari
├── message/              # Handler'lar
│   ├── __init__.py
│   ├── user.py          # Foydalanuvchi handler'lari
│   ├── admin.py         # Admin handler'lari
│   └── tasks.py         # Background task'lar
├── .env                 # Konfiguratsiya fayli (yaratish kerak)
├── .gitignore
└── README.md
```

## 🎯 Ishga tushirish

```bash
python bot.py
```

Bot ishga tushgandan keyin:
```
INFO:aiogram:Bot started successfully
INFO:asyncio:Posts checked and sent if needed.
```

## 📖 Foydalanish

### Foydalanuvchilar uchun

1. Botga `/start` yuboring
2. Ismingizni kiriting
3. Telefon raqamingizni kiriting:
   - `+998901234567`
   - `998901234567`
   - `901234567`
   - `90 123 45 67`
   - `+998 90 123 45 67`

### Admin uchun

#### 📢 Xabar yuborish (broadcast)
```
/post
```
Keyin xabaringizni yuboring - barcha foydalanuvchilarga yuboriladi.

#### ⏰ Rejalashtirilgan xabar
```
/schedule
```
1. Xabarni yuboring
2. Vaqtni kiriting:
   - `1 minut`
   - `2 soat`
   - `1 kun`
   - `1 kun 20 soat 30 minut`

**Qanday ishlaydi:**
- Foydalanuvchi ro'yxatdan o'tganidan keyin belgilangan vaqt o'tgach xabar yuboriladi
- Masalan: "1 soat" deb belgilasangiz, har bir yangi foydalanuvchiga ro'yxatdan o'tganidan 1 soat o'tgach xabar yuboriladi

#### 📊 Foydalanuvchilarni eksport qilish
```
/data
```
Barcha foydalanuvchilar ma'lumotlari Excel faylida yuklanadi.

#### 👀 Rejalashtirilgan postlarni ko'rish
```
/scheduled_posts
```
Barcha saqlangan postlar ro'yxati ko'rsatiladi.

#### 🗑️ Postni o'chirish
Post ko'rinishidan "O'chirish" tugmasini bosing.

## 🗄️ Database

Loyihada **SQLite** database ishlatiladi (`db.sqlite3`).

### Modellar:

**User** (Foydalanuvchi)
- `id` - Noyob ID
- `telegram_id` - Telegram ID
- `name` - Ism
- `phone_number` - Telefon raqam
- `created_at` - Ro'yxatdan o'tgan vaqt

**Post** (Rejalashtirilgan xabar)
- `id` - Noyob ID
- `from_chat_id` - Chat ID
- `message_id` - Xabar ID
- `send_time` - Yuborish vaqti (timedelta)

**ViewsPosts** (Ko'rilgan xabarlar)
- `id` - Noyob ID
- `post` - Post'ga havola
- `user_telegram_id` - Foydalanuvchi Telegram ID
- `message_id` - Yuborilgan xabar ID
- `viewed_at` - Ko'rilgan vaqt

## ⚙️ Sozlamalar

### Telefon raqam validatsiya

Qo'llab-quvvatlanadigan O'zbekiston operator kodlari:
- `90, 91, 93, 94, 95, 97, 98, 99` - Mobil operatorlar
- `33, 88, 20, 50, 55, 56, 58` - Boshqa operatorlar

### Xabarlar o'chirish

Foydalanuvchilarga yuborilgan xabarlar **1 kun** o'tgandan keyin avtomatik o'chiriladi.

### Task check interval

Bot har **10 sekund**da rejalashtirilgan xabarlarni tekshiradi.

## 🛡️ Xavfsizlik

- ✅ Bot `protect_content=True` bilan ishlamoqda (xabarlarni forward qilish mumkin emas)
- ✅ Admin komandalar faqat ADMIN_ID uchun mavjud
- ✅ `.env` fayli `.gitignore` da (maxfiy ma'lumotlar saqlanadi)

## 🐛 Muammolarni hal qilish

### Bot ishga tushmayapti
```bash
# Virtual environment faollashganligini tekshiring
# Token va Admin ID to'g'riligini tekshiring
```

### aiosqlite xatosi
```bash
pip install "aiosqlite==0.20.0"
```

### Database xatosi
```bash
# db.sqlite3 faylini o'chiring va botni qayta ishga tushiring
rm db.sqlite3  # Linux/Mac
del db.sqlite3  # Windows
```

## 📝 Litsenziya

Bu loyiha ochiq kodli va o'quv maqsadlari uchun yaratilgan.

## 👨‍💻 Muallif

Agar savollar bo'lsa, GitHub Issues'da so'rang.

## 🤝 Hissa qo'shish

Pull request'lar qabul qilinadi! Loyihani yaxshilash uchun o'z hissangizni qo'shing.

---

**⭐ Agar loyiha foydali bo'lsa, star bering!**
