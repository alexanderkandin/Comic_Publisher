import telegram
import os
import random
import requests
import time


from dotenv import load_dotenv

from download import download_image


def get_total_comics(url):
    response = requests.get(url)
    response.raise_for_status()
    comics = response.json()
    total_comics = comics.get('num')
    return total_comics

def get_random_comics(total_comics):
    random_comic = random.randint(1,int(total_comics))

    random_comic_url = f"https://xkcd.com/{random_comic}/info.0.json"

    response = requests.get(random_comic_url)
    response.raise_for_status()
    comics = response.json()
    image_url = comics.get('img')
    comment = comics.get('alt')
    file_name = comics.get('safe_title')
    return image_url, comment, file_name


def main():
    load_dotenv()
    tg_api_key = os.getenv("TELEGRAM_API_KEY")
    bot = telegram.Bot(token=tg_api_key)
    tg_chat_id = os.getenv("TG_CHAT_ID")
    directory = 'images'

    url = "https://xkcd.com/info.0.json"
    total_comics = get_total_comics(url)
    image_url, comment, file_name = get_random_comics(total_comics)
    download_image(image_url, directory, f'{file_name}.png')

    file_path = os.path.join(directory, f'{file_name}.png')
    with open(file_path, "rb") as file:
        bot.send_document(chat_id=tg_chat_id, document=file)
        bot.send_message(chat_id=tg_chat_id,text=comment)


    time.sleep(1)
    if os.path.exists(file_path):
        os.remove(file_path)


if __name__ == "__main__":
    main()
