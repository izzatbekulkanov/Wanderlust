# Wanderlust Backend

Wanderlust – bu sayohatchilar uchun mobil ilovalar uchun backend xizmatlarini taqdim etuvchi loyiha. Ushbu loyiha React Native frontend ilovasi bilan birgalikda ishlaydi va Django asosida ishlab chiqilgan.

---

## Loyihaning Asosiy Xususiyatlari

### 1. Ma'lumotlar Bazasi Modellari
- **Foydalanuvchilar:**
  - Profil va shaxsiy ma'lumotlar.
  - Parolni tiklash imkoniyati.
  - Do'stlar ro'yxatini boshqarish.
- **Sayohatlar:**
  - Sayohat nomi, tavsifi, shaharlar, sanalar.
  - Do'stlarni sayohatlarga qo'shish imkoniyati.
- **Obunalar:**
  - Turli xil obuna turlari va foydalanuvchilarning obuna holati.
- **Xaritalar:**
  - Geolokatsiya orqali foydalanuvchi joylashuvini aniqlash.
  - Tashrif buyurilgan joylarni saqlash.
- **Valyuta ma'lumotlari:**
  - API orqali real vaqt rejimida valyuta kurslarini yangilash.
- **Kalkulyatorlar:**
  - Sayohat va yashash xarajatlarini hisoblash imkoniyatlari.
- **Statik ma'lumotlar:**
  - Mamlakatlar, shaharlar va yashash darajasi haqidagi statik ma'lumotlar.

### 2. API Interfeysi
- **Ro'yxatdan o'tish va avtorizatsiya:**
  - JWT yordamida xavfsiz autentifikatsiya.
  - Ro'yxatdan o'tish, login va logout funksiyalari.
- **Foydalanuvchi profili:**
  - Ma'lumotlarni ko'rish va tahrirlash.
  - Do'stlarni qo'shish va o'chirish.
- **Sayohatlar:**
  - Sayohat yaratish, o'zgartirish va o'chirish.
  - Kelajak va o'tgan sayohatlarni ajratib ko'rsatish.
- **Xaritalar va geolokatsiya:**
  - Foydalanuvchining joylashuvini aniqlash va qayd qilish.
- **Valyuta konvertatsiyasi:**
  - API orqali valyuta kurslarini olish va hisoblash.
- **Kalkulyatorlar:**
  - Sayohat va yashash xarajatlarini hisoblash API'lari.
- **Bildirishnomalar:**
  - Yangi sayohat, obuna yoki do'st qo'shilganida foydalanuvchilarga xabar yuborish.
- **Obunalar:**
  - Foydalanuvchilarning obuna holatini boshqarish va monitoring qilish.

### 3. Integratsiyalar
- **Valyuta API:** Exchange Rates API orqali valyuta kurslarini olish.
- **Geolokatsiya API:** Google Maps yoki OpenStreetMap API integratsiyasi.
- **To'lov tizimi:** Yukassa yoki boshqa to'lov tizimi bilan integratsiya.
- **Bildirishnoma tizimi:** FCM (Firebase Cloud Messaging) yoki APNs orqali mobil bildirishnomalar.

### 4. Xavfsizlik
- **Token boshqaruvi:** JWT tokenlarni yangilash va qora ro'yxatga olish.
- **Ma'lumotlarning shifrlanishi:** Parollarni `bcrypt` yoki `argon2` yordamida xavfsiz shifrlash.
- **API xavfsizligi:** Rate limiting va API kalitlari orqali xavfsizlikni ta'minlash.
- **HTTPS ulanish:** Ma'lumotlarni shifrlangan holda uzatish.

### 5. Admin Paneli
- Foydalanuvchilarni boshqarish.
- Sayohatlar va obunalarni kuzatish.
- Statik ma'lumotlarni boshqarish (mamlakatlar, shaharlar va yashash darajalari).

---

## Texnologiyalar
- **Backend platforma:** Django + Django REST Framework.
- **Ma'lumotlar ombori:** SQLite (ishlab chiqish uchun) yoki PostgreSQL (ishlab chiqarish uchun).
- **Caching:** Redis (bildirishnomalar va tokenlarni boshqarish uchun).
- **Testlash vositalari:** Postman, Swagger.

---

## Loyihani Ishga Tushirish

### Talablar
- Python 3.8 yoki undan yuqori.
- Virtual environment (`venv`).
- Django va talab qilinadigan kutubxonalar.

### O'rnatish
1. **Loyihani klonlash:**
   ```bash
   git clone https://github.com/username/wanderlust-backend.git
   cd wanderlust-backend
Virtual environment yaratish va faollashtirish:

bash
Copy code
python -m venv venv
source venv/bin/activate  # Windows uchun: venv\Scripts\activate
Kutubxonalarni o'rnatish:

bash
Copy code
pip install -r requirements.txt
Ma'lumotlar bazasini sozlash va migratsiyalarni qo'llash:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
Superuser yaratish:

bash
Copy code
python manage.py createsuperuser
Lokal serverni ishga tushirish:

bash
Copy code
python manage.py runserver
Admin panelga kirish:

URL: http://127.0.0.1:8000/admin
API Misollari
Ro'yxatdan o'tish:

URL: /register/
Method: POST
Misol:
json
Copy code
{
  "username": "user1",
  "email": "user1@example.com",
  "password": "securepassword",
  "full_name": "User One"
}
Avtorizatsiya:

URL: /login/
Method: POST
Misol:
json
Copy code
{
  "username": "user1",
  "password": "securepassword"
}
Sayohatlar ro'yxati:

URL: /trips/
Method: GET
Sayohat yaratish:

URL: /trips/
Method: POST
Misol:
json
Copy code
{
  "name": "Maldives Trip",
  "description": "A relaxing trip to the Maldives",
  "start_date": "2024-12-01",
  "end_date": "2024-12-10"
}
Muallif haqida
Ism: Izzatbek Ulkanov
Telegram: @izzatbekulkanov
Instagram: @izzatbekulkanov_
Hissa Qo'shish
Loyiha kodini fork qiling.
Yangi xususiyatlarni kiriting.
Pull Request yuboring.
Litsenziya
Ushbu loyiha MIT Litsenziyasi ostida tarqatilgan.

rust
Copy code

Bu README loyihani to'liq tushuntiradi va dasturchi sifatida sizni ko'rsatib beradi. Agar qo'shimcha 
