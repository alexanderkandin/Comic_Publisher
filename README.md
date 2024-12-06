# Telegram Bot. Отправка рандомного комикса

Этот скрипт автоматически загружает случайный комикс с сайта XKCD и отправляет его в Telegram-чат. Комикс сохраняется локально, затем отправляется в чат, и после этого удаляется.

## Установка и настройка

### 1. Установите зависимости
Скачайте и установите необходимые библиотеки с помощью следующей команды:

```bash
pip install -r requirements.txt
```
### Содержимое requirements.txt:
```
python-dotenv==1.0.1
python-telegram-bot==13.15
requests==2.32.3
```
В репозитории также есть скрипт `download.py`, который отвечает за скачивание изображений с комиксами. Он использует функцию download_image для загрузки изображений.


## Настройте переменные окружения
Создайте файл .env в корне проекта и добавьте в него следующие строки:
```
TELEGRAM_API_KEY=ваш_токен_бота
TG_CHAT_ID=ваш_chat_id
```
## Запуск скрипта
После настройки переменных окружения и установки зависимостей, вы можете запустить скрипт:
```
python main.py
```
Скрипт выберет случайный комикс с сайта XKCD, загрузит его, отправит в ваш чат Telegram и удалит локальный файл.