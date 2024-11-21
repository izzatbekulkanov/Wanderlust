from pathlib import Path
import os

# Loyihaning asosiy katalogi
BASE_DIR = Path(__file__).resolve().parent.parent

# Maxfiy kalit (ishlab chiqarishda sir saqlang)
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-=u*x)g$r*%a%r=rln7bh4o*62*@brungv_w8j^_$z3ls8-j^v=')

# Ishlab chiqarish muhiti uchun DEBUG ni o'chiring
DEBUG = os.getenv('DJANGO_DEBUG', 'True') == 'True'

# Ruxsat berilgan xostlar
ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '').split(',')

# Dastur modullari
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Qo'shimcha kutubxonalar
    'rest_framework',              # DRF (Django REST Framework)
    'rest_framework.authtoken',    # Token orqali autentifikatsiya
    'corsheaders',                 # CORS qo'llab-quvvatlash
]

# Oraliq dastur (middleware)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',  # Shartli GET qo'llab-quvvatlash
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',            # CORS
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Asosiy URL konfiguratsiyasi
ROOT_URLCONF = 'wanderlust_backend.urls'

# Shablonlar sozlamalari
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI dasturi
WSGI_APPLICATION = 'wanderlust_backend.wsgi.application'

# Ma'lumotlar bazasi sozlamalari (SQLite uchun)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Parol tekshirish qoidalari
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 12,  # Minimal uzunlik oshirildi
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Til va vaqt mintaqasi
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Statik fayllar uchun URL
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Media fayllar uchun sozlamalar
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Birlamchi kalitning standart turi
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Django REST Framework sozlamalari
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

# CORS sozlamalari
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',  # Frontend uchun
    'https://your-production-domain.com',  # Ishlab chiqarish muhiti
]
CORS_ALLOW_CREDENTIALS = True

# Xavfsizlik sozlamalari
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
CSRF_COOKIE_SECURE = not DEBUG
SESSION_COOKIE_SECURE = not DEBUG
SECURE_SSL_REDIRECT = not DEBUG
SECURE_HSTS_SECONDS = 31536000 if not DEBUG else 0
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Bildirishnoma va loglash
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'debug.log'),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# Secret kalitlarni .env faylda saqlash
try:
    from dotenv import load_dotenv
    load_dotenv()
except ModuleNotFoundError:
    pass
