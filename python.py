import configparser
from pathlib import Path
import cv2
from PIL import Image, ImageEnhance

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

def colorImage(imageprob, red, green, blue):
    img = Image.open(imageprob).convert("RGBA")
 
    datas = img.getdata()
    newData = []
 
    for item in datas:
        if item[3] == 255:
            newData.append((red, green, blue, 255))
        else:
            newData.append(item)
    img.putdata(newData)
    img.save(imageprob, "PNG")

convertImage("red_channel.png")
convertImage("green_channel.png")
convertImage("blue_channel.png")
colorImage("red_channel.png", 255, 0, 0)
colorImage("green_channel.png", 0, 255, 0)
colorImage("blue_channel.png", 0, 0, 255)

#resizes image
def resize(imageprob):
    img = Image.open(imageprob)
    length = config.getint('img', 'length')
    width = config.getint('img', 'width')
    newsize = (width, length) 
    img.resize(newsize).save(imageprob)
resize("red_channel.png")
resize("green_channel.png")
resize("blue_channel.png")

r = cv2.imread("red_channel.png")
g = cv2.imread("green_channel.png")
b = cv2.imread("blue_channel.png")
final = cv2.add(r, g, b)
cv2.imshow("cum", final)
cv2.waitKey(0)
