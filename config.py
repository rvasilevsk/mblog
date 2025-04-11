from os import environ as env
from pathlib import Path
from dotenv import load_dotenv


root = Path(__file__).parent
load_dotenv(root / ".env")

DEFAULT_DATABASE_URI = f"sqlite:///{root / 'app.db'}"


class Config:
    SECRET_KEY = env.get("SECRET_KEY") or "you-will-never-guess"
    SERVER_NAME = env.get("SERVER_NAME")
    SQLALCHEMY_DATABASE_URI = env.get("DATABASE_URL") or DEFAULT_DATABASE_URI
    LOG_TO_STDOUT = env.get("LOG_TO_STDOUT")
    MAIL_SERVER = env.get("MAIL_SERVER")
    MAIL_PORT = int(env.get("MAIL_PORT") or 25)
    MAIL_USE_TLS = env.get("MAIL_USE_TLS") is not None
    MAIL_USERNAME = env.get("MAIL_USERNAME")
    MAIL_PASSWORD = env.get("MAIL_PASSWORD")
    ADMINS = ["your-email@example.com"]
    LANGUAGES = ["en", "es"]
    MS_TRANSLATOR_KEY = env.get("MS_TRANSLATOR_KEY")
    ELASTICSEARCH_URL = env.get("ELASTICSEARCH_URL")
    REDIS_URL = env.get("REDIS_URL") or "redis://"
    POSTS_PER_PAGE = 25


def attrs_as_dict(klass):
    res = {k: getattr(klass, k) for k in dir(klass) if not k.startswith("__")}
    res = {k: v for k, v in res.items() if not callable(v)}
    return res


if __name__ == "__main__":
    from pprint import pp

    print(f"DEFAULT_DATABASE_URI: {DEFAULT_DATABASE_URI}")
    print()
    pp(attrs_as_dict(Config))
