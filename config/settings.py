from pathlib import Path
import os
import dj_database_url

# BASE_DIR 設定
BASE_DIR = Path(__file__).resolve().parent.parent

# --------------------------------------------------
# セキュリティ設定（環境変数優先）
SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-default")
DEBUG = os.getenv("DEBUG", "True") == "True"

# ✅ Renderの動的URLに対応（環境変数 or デフォルト）
RENDER_EXTERNAL_HOSTNAME = os.getenv("RENDER_EXTERNAL_HOSTNAME", "is-2025-xx.onrender.com")
ALLOWED_HOSTS = ["127.0.0.1", "localhost", RENDER_EXTERNAL_HOSTNAME]

# ✅ CSRF信頼オリジンも同様に動的に設定
CSRF_TRUSTED_ORIGINS = [f"https://{RENDER_EXTERNAL_HOSTNAME}"]
# --------------------------------------------------

# アプリケーション定義
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "channels",
    "community_app",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "community_app.middleware.RequireLoginMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# ✅ ASGI 設定（Daphne/Channels 用）
ASGI_APPLICATION = "config.asgi.application"

# ✅ Redis チャネルレイヤー設定（Upstash Redis を環境変数から使用）
REDIS_URL = os.environ["REDIS_URL"]  # Render の環境変数に rediss://... を設定

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [REDIS_URL],
        },
    },
}

# ✅ データベース設定（環境変数 DATABASE_URL にも対応）
DATABASES = {
    "default": dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}", conn_max_age=600
    )
}

# パスワードバリデーション
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ローカライズ
LANGUAGE_CODE = "ja"
TIME_ZONE = "Asia/Tokyo"
USE_I18N = True
USE_TZ = True

# 静的ファイル
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ---------------------------------------------------------
# ログイン・セッション設定
SESSION_COOKIE_AGE = 30  # 秒
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_SAVE_EVERY_REQUEST = False

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/accounts/login/'
# ---------------------------------------------------------
