# Установка
- Установить `Python` версии `>= 3.10`
- Команда `pip install poetry` или для linux `pip3 install poetry`
- `git clone https://github.com/kanewi11/telegram-notify-in-bot.git`
- Перейти в директорию `telegram-notify-in-bot/`
- `poetry install` - установка библиотек


# Перед запуском
- `cp .envs/.env.example .envs/.env` - копируем файл и переименовываем в `.env`
- В файле `.envs/.env` вписать токен бота
- В файле `text.txt` указать текст (форматирование HTML), там есть образец
- В файле `users.txt` указать id пользователей с новой строки, там есть образец

# Запуск
- `poetry shell`
- `python main.py`