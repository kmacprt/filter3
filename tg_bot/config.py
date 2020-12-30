from tg_bot.sample_config import Config

class Development(Config):
    OWNER_ID = 1131653685  # your telegram ID
    OWNER_USERNAME = "Kavinduaj"  # your telegram username
    API_KEY = "1423025003:AAFoeqQp167vO8zMvH4ZHsLzK7sbooXpVms"  # your api key, as provided by the @botfather
    SQLALCHEMY_DATABASE_URI = 'postgresql://kmac:dkkaj0123456@postgresql/postgres'  # sample db credentials
    START_PHOTTO = 'https://telegra.ph/file/44706b57abb809b53c68d.png'
    WEBHOOK = False
    MESSAGE_DUMP = None
    STRICT_GBAN = False
