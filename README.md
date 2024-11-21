# 🧭 Wanderlust Backend
> **Sayohatchilar uchun mo'ljallangan backend xizmatlari.**
>
> Django asosida qurilgan backend, mobil ilovalar bilan integratsiya uchun tayyor. Bu loyiha foydalanuvchilar uchun shaxsiy profil, sayohatlar ro'yxati, xarajat kalkulyatori va yana ko'plab funksiyalarni taqdim etadi.

---

## 🚀 Loyihaning Asosiy Xususiyatlari
### 🌟 Ma'lumotlar Bazasi Modellari
- **Foydalanuvchilar:**
  - Profil yaratish va shaxsiy ma'lumotlarni boshqarish.
  - Parolni tiklash imkoniyati.
  - Do'stlar ro'yxatini boshqarish.
- **Sayohatlar:**
  - Sayohat yaratish, o'zgartirish va o'chirish.
  - Do'stlarni sayohatlarga qo'shish imkoniyati.
- **Obunalar:**
  - Turli obuna turlari va foydalanuvchilarning obuna holati.
- **Xaritalar:**
  - Geolokatsiya orqali foydalanuvchi joylashuvini aniqlash va saqlash.
- **Kalkulyatorlar:**
  - Sayohat va yashash xarajatlarini hisoblash imkoniyati.
- **Statik ma'lumotlar:**
  - Mamlakatlar, shaharlar va yashash darajalari haqidagi statik ma'lumotlar.

---

## 📋 O'rnatish Qo'llanmasi
Quyidagi qadamlarni bajarib, loyihani lokal muhitingizda ishga tushirishingiz mumkin:

### Talablar
- Python 3.8+
- Virtual environment (`venv`)
- Django va kerakli kutubxonalar (`requirements.txt` orqali).

### O'rnatish Bosqichlari
```bash
# 1. Loyihani klonlash:
git clone https://github.com/username/wanderlust-backend.git
cd wanderlust-backend

# 2. Virtual environment yaratish va faollashtirish:
python -m venv venv
source venv/bin/activate  # Windows uchun: venv\Scripts\activate

# 3. Kutubxonalarni o'rnatish:
pip install -r requirements.txt

# 4. Migratsiyalarni qo'llash:
python manage.py makemigrations
python manage.py migrate

# 5. Superuser yaratish:
python manage.py createsuperuser

# 6. Serverni ishga tushirish:
python manage.py runserver

```
🌐 API Qo'llanmasi
Avtorizatsiya
URL: /login/
Method: POST
Ma'lumot:
{
  "username": "user1",
  "password": "securepassword"
}

Sayohat Yaratish
URL: /trips/
Method: POST
Ma'lumot:
{
  "name": "Maldives Trip",
  "description": "A relaxing trip to the Maldives",
  "start_date": "2024-12-01",
  "end_date": "2024-12-10"
}

Sayohatlar Ro'yxati
URL: /trips/
Method: GET

🛡️ Xavfsizlik
Token boshqaruvi: JWT tokenlarni yangilash va qora ro'yxatga olish.
HTTPS: Ma'lumotlarni xavfsiz uzatish uchun shifrlangan ulanish.
API Rate Limiting: API hujumlaridan himoyalanish.
Parol xavfsizligi: Foydalanuvchi parollari bcrypt yoki argon2 yordamida shifrlanadi.
👥 Loyihaga Hissa Qo'shish
Hissa qo'shmoqchi bo'lsangiz:

Loyiha kodini fork qiling.
Yangi xususiyatlar yoki xatolarni tuzatish kiriting.
Pull Request yuboring.
📩 Muallif haqida
Muallif: Izzatbek Ulkanov
Telegram: @izzatbekulkanov
Instagram: @izzatbekulkanov_

📜 Litsenziya
Loyiha MIT Litsenziyasi asosida tarqatiladi.


---

### README haqida:
1. **Mazmunli tarkib:** Loyiha imkoniyatlari, API tavsiflari, xavfsizlik va o'rnatish jarayoni bosqichma-bosqich ko'rsatib berilgan.
2. **Format:** Emojilar, sarlavhalar va bo'limlar o'quvchiga qulay bo'lishi uchun ishlatilgan.
3. **Mualliflik:** Sizning ism va ijtimoiy tarmoq ma'lumotlaringiz kiritilgan.

Agar qo'shimcha o'zgarishlar kerak bo'lsa, bemalol ayting! 😊


