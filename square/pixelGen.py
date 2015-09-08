# 
# Your previous Plain Text content is preserved below:
# 
# This is just a simple shared plaintext pad, with no execution capabilities.
# 
# When you know what language you'd like to use for your interview,
# simply choose it from the dropdown in the top bar.
# 
# You can also change the default language your pads are created with
# in your account settings: https://coderpad.io/profile
# 
# Enjoy your interview!
# 
# 1. Randomly generate an array of 1,000 pixels (R, G, and B values between 0 and 255 inclusive

import random
def getRandomNumber():
    return random.randint(0, 255)

def getRandomPixel():
    return (getRandomNumber() for x in range(3))

def getThousandPixels():
    return [getRandomPixel() for x in range(10000)]

def printPixel(pixel):
    print(' '.join([str(x) for x in pixel]))
        
thousandPixels = getThousandPixels()
# for pixel in thousandPixels[len(thousandPixels) - 15:]:
#     printPixel(pixel)
pixelHash = {}

def lowPixelVal(val):
    return 0 if val <= 4 else val - 4

def highPixelVal(val):
    return 255 if val >= 251 else val + 4

def checkInHash(pixelHash, pixel):
    r,g,b = pixel
    lowR = lowPixelVal(r)
    lowG = lowPixelVal(g)
    lowB = lowPixelVal(b)
    highR = highPixelVal(r)
    highG = highPixelVal(g)
    highB = highPixelVal(b)
    for rVal in range(lowR, highR + 1):
        for gVal in range(lowG, highG + 1):
            for bVal in range(lowB, highB + 1):
                resultPixel = tuple([rVal, gVal, bVal])
                if resultPixel in pixelHash:
                    return resultPixel
    return None

for pixel in thousandPixels:
    pixTuple = tuple(pixel)
    resultPixel = checkInHash(pixelHash, pixTuple)
    if resultPixel is None:
        pixelHash[pixTuple] = 1
    else:
        pixelHash[resultPixel] += 1        

maxVal = 0
maxPixel = (0, 0, 0)
for pixel in pixelHash:
    if pixelHash[pixel] > maxVal:
        maxVal = pixelHash[pixel]
        maxPixel = pixel
print("(", ' '.join([str(x) for x in maxPixel]), "):", maxVal)
print(len(pixelHash))
        
    

# (0, 0, 0) / 4 = (0, 0, 0)
# (0, 0, 3) / 4 ()
# (0, 3, 0)
# (3, 0, 0)
# (3, 3, 3) / 4 = (0, 0, 0)

# (2, 8, 2)
# (3, 7, 3)
