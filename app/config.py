import os
from typing import Any
from pathlib import Path

from dotenv import load_dotenv

# load .env file
mode = os.environ.get("MODE", "").lower()
for file in [".env", f".env.{mode}.local", f".env.{mode}"]:
    if Path(file).exists():
        print(f"Loading environment variables from {file}")
        load_dotenv(file)
        break


def get_env(key: str, default: Any | None = None, required: bool = True):
    value = os.environ.get(key, default)

    if required and not value:
        raise ValueError(f"Environment variable {key} is not set")

    return value


CORS_ORIGINS = get_env("CORS_ORIGINS", "", False)

# Google OAuth
GOOGLE_CLIENT_ID = get_env("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = get_env("GOOGLE_CLIENT_SECRET")


class Config:
    # Flask
    TESTING = get_env("TESTING", "False", False) == "True"
    DEBUG = get_env("DEBUG", "False", False) == "True"
    TEMPLATES_AUTO_RELOAD = get_env("TEMPLATES_AUTO_RELOAD", "False", False) == "True"
    STATIC_AUTO_RELOAD = get_env("STATIC_AUTO_RELOAD", "False", False) == "True"
    EXPLAIN_TEMPLATE_LOADING = (
        get_env("EXPLAIN_TEMPLATE_LOADING", "False", False) == "True"
    )
    SECRET_KEY = get_env("SECRET_KEY", "YOUR-FALLBACK-SECRET-KEY")

    # Flask-Login
    SESSION_COOKIE_SAMESITE = get_env("SESSION_COOKIE_SAMESITE", "Lax")

    # Flask-SQLAlchemy
    SQLALCHEMY_DATABASE_URI = get_env("SQLALCHEMY_DATABASE_URI", "sqlite:///db.sqlite")
    SQLALCHEMY_TRACK_MODIFICATIONS = (
        get_env("SQLALCHEMY_TRACK_MODIFICATIONS", "False", False) == "True"
    )

    # Flask-Mail
    MAIL_ENABLE = get_env("MAIL_ENABLE", None, True) == "True"
    MAIL_SERVER = get_env("MAIL_SERVER", None, True)
    MAIL_PORT = get_env("MAIL_PORT", None, True)
    MAIL_USERNAME = get_env("MAIL_USERNAME", None, True)
    MAIL_PASSWORD = get_env("MAIL_PASSWORD", None, True)
    MAIL_DEFAULT_SENDER = get_env("MAIL_DEFAULT_SENDER", None, True)
    MAIL_USE_TLS = get_env("MAIL_USE_TLS", None, True) == "True"
    MAIL_USE_SSL = get_env("MAIL_USE_SSL", None, True) == "True"

    # Crypto
    AES_KEY = get_env("AES_KEY")

    # Ratelimit
    RATELIMIT_ENABLED = get_env("RATELIMIT_ENABLED", "False") == "True"
    RATELIMIT_STORAGE_URI = get_env("RATELIMIT_STORAGE_URI", "memory://")
    RATELIMIT_STRATEGY = "fixed-window"
    RATELIMIT_IN_MEMORY_FALLBACK_ENABLED = True
    RATELIMIT_HEADERS_ENABLED = True
