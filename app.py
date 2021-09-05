import requests, re, os, time
from loader import session
from api import download as dlapi
from api import url as urlapi

print("Rule34 Tag Downloader by Knotoni")
time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')

print("Choose language\выберите язык:\n1 - русский\n2 - английский")
lang = int(input())

os.system('cls' if os.name == 'nt' else 'clear')

while lang != 1 and lang != 2:
    print("Error! Try again/Ошибка! Попробуйте снова:")
    time.sleep(4)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Choose language\выберите язык:\n1 - русский\n2 - английский")
    lang = int(input())

if lang == 1:
    print("Введите теги через пробел:\n")
elif lang == 2:
    print("Enter tags separated by a space:\n")


tag = str(input())
tags = re.split('\s', tag)

os.system('cls' if os.name == 'nt' else 'clear')

if lang == 1:
    print("Старт загрузки...")
elif lang == 2:
    print("Start download...")

url_pages = urlapi.get_post_url(tags)

folder = dlapi.make_dir(tags)
os.chdir(folder)

for url_page in url_pages:
    if not url_page:
        continue
    image_url = urlapi.get_image_url(url_page)
    post_id = urlapi.get_post_id(url_page)
    file_format = urlapi.get_file_format(image_url)
    if dlapi.file_exist_or_not(post_id, file_format) == True:
        continue
    dlapi.download_image(image_url, file_format, post_id)

os.system('cls' if os.name == 'nt' else 'clear')

if lang == 1:
    print("Загрузка завершена!")
if lang == 2:
    print("Download complete!")