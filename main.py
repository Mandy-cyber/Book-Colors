from hsvItemColors import RGB2HSV, color_model, books
import math
# import cv2
from PIL import Image
import matplotlib.pyplot as plt

#-----------------------------------------------------------------------------------------------------------------#
#FROM EARLIER EXPERIMENTATION
# book = cv2.imread('1.jpg')
# print("The type of this input is {}".format(type(book)))
# print("Shape: {}".format(book.shape)) #first two values = pixels of the image, the last shows that it represents 3 colors (rgb)
# plt.axis("off")
# plt.imshow(book) #display the book
# book = cv2.cvtColor(book, cv2.COLOR_BGR2RGB) #change from BGR to RGB format

#-----------------------------------------------------------------------------------------------------------------#

directory = r"C:\Users\amand\OneDrive\Desktop\CH\BookColors\items"
rgb_c = color_model(directory) #get main rgb color of each pic
# hsv_c = RGB2HSV(rgb_c) #convert rgb color to hsv color

#-----------------------------------------------------------------------------------------------------------------#
#CREATING A DICTIONARY OF COLORS

for x in books:
    #next two lines because organizing ugly looking arrays
    c = books.get(x)[0]
    sum_rgb = 0
    for y in c: 
        sum_rgb += y #adding the r, g and b numbers together
    books[x] = math.sqrt(sum_rgb) #adding the image number and sqrt value of sum to the dictionary

#-----------------------------------------------------------------------------------------------------------------#
#SORTING DICTIONARY IN ASCENDING ORDER OF VALUES

sortedColorInfo = {} #new dict to use
sortedKeys = sorted(books, key=books.get) #sort the key values of the old dict
for w in sortedKeys:
    sortedColorInfo[w] = books[w] #put those values into the new dict


for z in sortedColorInfo:
    im = Image.open(z)
    im.show()

