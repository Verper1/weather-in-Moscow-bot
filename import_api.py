from imports import find_dotenv, load_dotenv, telebot, os


# Для загрузки данных с .env файла.
load_dotenv(find_dotenv())

# Нужна для работы самого бота в Telegram.
bot = telebot.TeleBot(token=os.getenv('TOKEN'))

# Нужна для получения информации о погоде.
key_api = os.getenv('WEATHER_API')
