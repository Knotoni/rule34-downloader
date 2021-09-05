import requests, re, os
from loader import session

def make_dir(tags):
    if len(tags) >= 3:
        folder_name = str(tags[0] + "," + tags[1] + "," + tags[2])
    elif len(tags) == 2:
        folder_name = str(tags[0] + "," + tags[1])
    elif len(tags) == 1:
        folder_name = str(tags[0])
    
    if os.path.exists(folder_name) == False:
        os.mkdir(folder_name)
    return folder_name

def download_image(url_image, file_format, id_image):
    image = requests.get(url_image)
    out = open("id" + str(id_image) + "." + str(file_format), "wb")
    out.write(image.content)
    out.close()

def file_exist_or_not(id_image, file_format):
    if os.path.exists("id" + str(id_image) + "." + str(file_format)) == True:
        return True
    else:
        return False
