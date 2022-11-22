import numpy as np
from PIL import Image, ImageDraw

dirName = 'C:/Users/79371/Desktop/hui-project/tools/'

imIn = Image.open(dirName + 'hui.png')
bbox = imIn.getbbox()
wIn = bbox[2] - bbox[0]
hIn = bbox[3] - bbox[1]

h = 7
w = round(wIn * h / hIn)

tones = np.zeros(w * h)
pixNums = np.zeros(w * h)

for i in range(bbox[0], bbox[2]):
    for j in range(bbox[1], bbox[3]):
        k = (int)(j*h/hIn) + h*(int)(i*w/wIn)
        pixel = imIn.getpixel((i, j))
        tones[k] += (pixel[0]+pixel[1]+pixel[2])/3
        pixNums[k] += 1

tones /= pixNums

min0 = min(tones)
max0 = max(tones)
tones = (tones - min0)/(max0 - min0)

gtPixels = np.array([(22, 27, 34), (14, 68, 41), (0, 109, 50), (38, 166, 65), (57, 211, 83)])

gtPixelsNorm = np.zeros(6)
for i in range(5):
    gtPixelsNorm[i+1] = (gtPixels[i][0]+gtPixels[i][1]+gtPixels[i][2])/3
min1 = min(gtPixelsNorm)
max1 = max(gtPixelsNorm)
gtPixelsNorm = (gtPixelsNorm - min1)/(max1 - min1)

rez = np.zeros(w * h, dtype=int)
for i in range(w * h):
    for j in range(1, 6):
        if tones[i] <= gtPixelsNorm[j]:
            rez[i] = j - 1
            break
        if j == 4:
            rez[i] = 4

for i in range(w * h):
    print(rez[i], ', ', end = '')

def getTuple(arr):
    return (arr[0], arr[1], arr[2])

squareSide = 10
imOut = Image.new('RGB', (w * squareSide, h * squareSide), getTuple(gtPixels[0]))
draw = ImageDraw.Draw(imOut)

for i in range(w):
    for j in range(h):
        if rez[j + i*h] > 0:
            gtColor = getTuple(gtPixels[rez[j + i*h]])
            for ii in range(squareSide):
                for jj in range(squareSide):
                    draw.point((i*squareSide + ii, j*squareSide + jj), gtColor)


imOut.save(dirName + 'preview.png')