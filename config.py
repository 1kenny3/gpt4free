import os
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()

# Токен бота
BOT_TOKEN = "7720792784:AAFqpwlvehPbeLq3fTHf0bAA5CLvt2XBd5o"

# Проверка наличия токена
if not BOT_TOKEN:
    raise ValueError(
        "Пожалуйста, установите токен бота!\n"
        "1. Получите токен у @BotFather в Telegram\n"
        "2. Создайте файл .env и добавьте строку: BOT_TOKEN=ваш_токен\n"
        "   или замените значение BOT_TOKEN в config.py"
    )

# Настройки для отладки
DEBUG = True 