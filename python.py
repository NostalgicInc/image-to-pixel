import configparser
from operator import length_hint
from pathlib import Path

fi = "config.ini"
config = configparser.ConfigParser()
# Add the structure to the file we will create
config.add_section('img')
config.set('img', 'width')
config.set('img', 'length')
# Write the new structure to the new file
with open(fi, 'w') as configfile:
    config.write(configfile)

from PIL import Image, ImageEnhance
length = config.getint('img', 'length')
width = config.getint('img', 'width')