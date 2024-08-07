# Установка
- Установить `Python` версии `>= 3.10`
- `pip install poetry` или для linux `pip3 install poetry`
- `poetry install` - установка библиотек


# Перед запуском
- `cp .envs/.env.example .envs/.env` - копируем файл и переименовываем в `.env`
- В файле `.envs/.env` вписать токен бота
- В файле `text.txt` указать текст (форматирование HTML), там есть образец
- В файле `users.txt` указать id пользователей с новой строки, там есть образец

# Запуск
- `poetry shell`
- `python main.py`