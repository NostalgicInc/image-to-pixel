import configparser
from operator import length_hint
from pathlib import Path

fi = "config.ini"
config = configparser.RawConfigParser()
config.read('config.ini')
with open(fi, 'w') as configfile:
    config.write(configfile)

from PIL import Image, ImageEnhance
img = Image.open("yourimage.png")
length = config.getint('img', 'length')
width = config.getint('img', 'width')
newsize = (width, length) 
img_resized = img.resize(newsize) 
print(img_resized.size)