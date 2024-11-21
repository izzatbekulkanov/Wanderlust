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

# 🌐 API Qo'llanmasi

---

## 1. Ro'yxatdan o'tish
- **URL:** `/register/`  
- **Method:** `POST`  
- **Tavsif:** Foydalanuvchi yangi hisob yaratadi.  
- **Ma'lumot:**
```json
{
  "username": "newuser",
  "email": "newuser@example.com",
  "password": "strongpassword",
  "full_name": "New User"
}
```

---

## 2. Sayohatlar Ro'yxati
- **URL:** `/trips/`  
- **Method:** `GET`  
- **Tavsif:** Foydalanuvchining barcha sayohatlarini ko'rish.  
- **Javob:**
```json
[
  {
    "id": 1,
    "name": "Maldives Trip",
    "description": "A relaxing trip to the Maldives",
    "start_date": "2024-12-01",
    "end_date": "2024-12-10",
    "friends": []
  }
]
```

---

## 3. Sayohat Yaratish
- **URL:** `/trips/`  
- **Method:** `POST`  
- **Tavsif:** Yangi sayohat yaratish.  
- **Ma'lumot:**
```json
{
  "name": "Adventure in Paris",
  "description": "Exploring the beauty of Paris",
  "start_date": "2025-01-15",
  "end_date": "2025-01-20",
  "friends": [2, 3]
}
```

---

## 🛡️ Xavfsizlik
- **Token boshqaruvi:** JWT tokenlarni yangilash va qora ro'yxatga olish.
- **HTTPS:** Ma'lumotlarni xavfsiz uzatish uchun shifrlangan ulanish.
- **API Rate Limiting:** API hujumlaridan himoyalanish.
- **Parol xavfsizligi:** Foydalanuvchi parollari `bcrypt` yoki `argon2` yordamida shifrlanadi.

---

## 👥 Loyihaga Hissa Qo'shish
Hissa qo'shmoqchi bo'lsangiz:
1. Loyiha kodini `fork` qiling.
2. Yangi xususiyatlar yoki xatolarni tuzatish kiriting.
3. `Pull Request` yuboring.

---

## 📩 Muallif haqida
> **Muallif:** Izzatbek Ulkanov  
> **Telegram:** [@izzatbekulkanov](https://t.me/izzatbekulkanov)  
> **Instagram:** [@izzatbekulkanov_](https://instagram.com/izzatbekulkanov_)
