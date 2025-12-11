import os
from pathlib import Path

# -------------------------------
# Путь к корню проекта
# -------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------------
# Основные настройки
# -------------------------------
SECRET_KEY = 'django-insecure-replace-this-with-your-own-key'
DEBUG = True  # Можно менять на False для production
ALLOWED_HOSTS = ['*']  # Для Render достаточно '*'

# -------------------------------
# Приложения
# -------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',  # обязательно для collectstatic
    'coasters_app',               # твоё приложение
]

# -------------------------------
# Middleware
# -------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'beer_coasters.urls'

# -------------------------------
# Шаблоны
# -------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'coasters_app' / 'templates'],
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

WSGI_APPLICATION = 'beer_coasters.wsgi.application'

# -------------------------------
# База данных (SQLite)
# -------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# -------------------------------
# Пароли (можно потом настроить)
# -------------------------------
AUTH_PASSWORD_VALIDATORS = []

# -------------------------------
# Локализация
# -------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# -------------------------------
# Статика
# -------------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'coasters_app' / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# -------------------------------
# Медиа (загрузка изображений)
# -------------------------------
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# -------------------------------
# Кастомная модель пользователя
# -------------------------------
AUTH_USER_MODEL = 'coasters_app.User'

# -------------------------------
# Файл логов (опционально, для Render удобно)
# -------------------------------
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}
