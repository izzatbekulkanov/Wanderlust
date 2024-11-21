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

### 🌐 API Interfeysi
- **Ro'yxatdan o'tish va avtorizatsiya:**
  - JWT token orqali autentifikatsiya.
  - Ro'yxatdan o'tish, login va logout funksiyalari.
- **Foydalanuvchi profili:**
  - Ma'lumotlarni ko'rish va tahrirlash.
  - Do'stlarni qo'shish va o'chirish.
- **Sayohatlar:**
  - Sayohat yaratish, kelajak va o'tgan sayohatlarni ajratish.
- **Valyuta konvertatsiyasi:**
  - API orqali valyuta kurslarini olish va hisoblash.
- **Kalkulyatorlar:**
  - Xarajatlarni hisoblash uchun moslashuvchan API.
- **Bildirishnomalar:**
  - Yangi sayohat, obuna yoki do'st qo'shilganida foydalanuvchilarga xabar yuborish.

---

## ⚙️ Texnologiyalar
| Texnologiya | Tavsif                          |
|-------------|----------------------------------|
| **Django**  | Backend uchun asosiy ramka      |
| **SQLite**  | Ishlab chiqish bosqichi uchun DBMS |
| **JWT**     | Foydalanuvchi autentifikatsiyasi |
| **CORS**    | Frontend va backend integratsiyasi |
| **Redis**   | Caching va bildirishnomalar     |

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
