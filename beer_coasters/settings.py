from pathlib import Path

# Сначала BASE_DIR
BASE_DIR = Path(__file__).resolve().parent.parent

# Потом можно использовать BASE_DIR
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'coasters_app' / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # движок БД
        'NAME': BASE_DIR / 'db.sqlite3',        # файл базы данных
    }
}
