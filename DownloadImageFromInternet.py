#Following program downloads an image from internet

import random

#urllib.request - an extensile library for opening URLS(mostly HTTP)
import urllib.request

def download_web_image(url):
    name  = random.randrange(1, 1000)
    file_name = str(name) + ".jpg"

    #urllib.request.urlretrieve(url, filename, reporthook, data) - copy a network object denoted by url to local file
    urllib.request.urlretrieve(url, file_name)

download_web_image("https://s-media-cache-ak0.pinimg.com/236x/0f/41/80/0f4180e569266d88417ec59d58e533d5.jpg")