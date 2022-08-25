import configparser
from operator import length_hint
from pathlib import Path
import cv2
import numpy as np
from PIL import Image, ImageEnhance, ImageChops

#loads config file
fi = "config.ini"
config = configparser.RawConfigParser()
config.read('config.ini')
with open(fi, 'w') as configfile:
    config.write(configfile)

#splits image into the three color channels
img = cv2.imread('yourimage.png', cv2.IMREAD_UNCHANGED)
cv2.imwrite('green_channel.png',img[:,:,1])
cv2.imwrite('red_channel.png',img[:,:,2])
cv2.imwrite('blue_channel.png',img[:,:,0])

#increases contrast on each the color channel images
ImageEnhance.Contrast(Image.open("red_channel.png")).enhance(15).save('red_channel.png')
ImageEnhance.Contrast(Image.open("green_channel.png")).enhance(15).save('green_channel.png')
ImageEnhance.Contrast(Image.open("blue_channel.png")).enhance(15).save('blue_channel.png')

#removes any other colors except for the dedicated color channel colors
def convertImage(imageprob):
    img = Image.open(imageprob).convert("RGBA")
    datas = img.getdata()
    newData = []
 
    for item in datas:
        if item[0] == 0 and item[1] == 0 and item[2] == 0:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    img.putdata(newData)
    img.save(imageprob, "PNG")

def colorImage(imageprob):
    img = Image.open(imageprob).convert("RGBA")
 
    datas = img.getdata()
    newData = []
 
    for item in datas:
        if item[3] == 255:
            newData.append((255, 0, 0, 255))
        else:
            newData.append(item)
    img.putdata(newData)
    img.save(imageprob, "PNG")

convertImage("red_channel.png")
convertImage("green_channel.png")
convertImage("blue_channel.png")
colorImage("red_channel.png")
colorImage("green_channel.png")
colorImage("blue_channel.png")
#resizes image
length = config.getint('img', 'length')
width = config.getint('img', 'width')
newsize = (width, length) 
# img.resize(newsize).save("output.png")