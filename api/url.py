import requests, re, urllib
from loader import session


def get_post_url(tags):
    url = "https://rule34.xxx/index.php?page=post&s=list&tags="
    for tag in tags:
        url = str(url + "+" + tag)
    
    page_text = session.get(url).text

    last_page_id = str(re.findall('pid\=\d{1,50}\".alt\=\"last.page\"', page_text))
    last_page_id = re.findall("\d{1,20}", last_page_id)
    
    page_url = re.findall('index.php\?page\=post\&s\=view\&id\=\d{1,15}', page_text)

    all_pages = 1

    if len(last_page_id) != 0:
        all_pages = int(last_page_id[0]) // 42

    i = 1

    while i <= all_pages:
        url = str(url + "&pid=" + str(i*42))
        page_text = session.get(url).text
        page_url.append(re.findall('index.php\?page\=post\&s\=view\&id\=\d{1,15}', page_text))
        i = i + 1
    return page_url

def get_image_url(url_page):
    page_text = session.get("https://rule34.xxx/" + str(url_page)).text
    image_url = re.findall('src\=\"\S{10,1000}\".id\=\"image\"', page_text)
    image_url = str(image_url[0])
    image_url = image_url.split('"')[1]
    return image_url

def get_post_id(url_page):
    id_image = re.findall('id\=\d{1,15}', url_page)
    id_image = str(id_image[0])
    id_image = id_image.split('=')[1]
    return id_image

def get_file_format(image_url):
    file_format = requests.get(image_url).headers['content-type']
    file_format = file_format.split('/')[1]
    return file_format