import configparser
from operator import length_hint
from pathlib import Path
import cv2
import numpy as np

fi = "config.ini"
config = configparser.RawConfigParser()
config.read('config.ini')
with open(fi, 'w') as configfile:
    config.write(configfile)

from PIL import Image, ImageEnhance
img = cv2.imread('yourimage.png', cv2.IMREAD_UNCHANGED)
green_channel = img[:,:,1]
cv2.imwrite('green_channel.png',green_channel)
red_channel = img[:,:,2]
cv2.imwrite('red_channel.png',red_channel)
blue_channel = img[:,:,0]
cv2.imwrite('blue_channel.png',blue_channel)

x, y, c = cv2.imread('yourimage.png').shape
print(x)
print(y)
length = config.getint('img', 'length')
width = config.getint('img', 'width')
newsize = (width, length) 
# img.resize(newsize).save("output.png")