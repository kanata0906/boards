import os

from apps.settings import BASE_DIR

# ... 既存の設定 ...

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
