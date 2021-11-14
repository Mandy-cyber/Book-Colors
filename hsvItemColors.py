from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import cv2
from collections import Counter
import colorsys
import os 

#-----------------------------------------------------------------------------------------------------------------#
#FUNCTION TO FIND THE item AND SORT IT OUT TO BE FITTED IN MODEL
def user_item(imagePath):
  item = cv2.imread(imagePath) #find the item
  item = cv2.cvtColor(item, cv2.COLOR_BGR2RGB) #change the color of the image from BGR to RGB
  modItem = cv2.resize(item, (600, 400), interpolation = cv2.INTER_AREA) #resize for quicker processing
  modItem = modItem.reshape(modItem.shape[0]*modItem.shape[1], 3) #reshape two 2 dimensions for KMeans
  return modItem

#-----------------------------------------------------------------------------------------------------------------#
#FUNCTION TO CONVERT RGB COLOR TO HEX COLOR
def RGB2HEX(color):
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))
# RGB2HEX((255,255,255)) #testing to see if it works

#-----------------------------------------------------------------------------------------------------------------#
#FUNCTION TO CONVERT RGB COLORS TO HSV COLORS SO THAT WE CAN DO COLOR SORTING LATER ON

def RGB2HSV(rgbColors):
  allHSVColors = []
  for rgbColor in rgbColors:
    r = rgbColor[0][0]
    g = rgbColor[0][1]
    b = rgbColor[0][2]
    allHSVColors.append(colorsys.rgb_to_hsv(r,g,b))
  return allHSVColors


#-----------------------------------------------------------------------------------------------------------------#
#CREATE CLUSTER MODEL AND IDENTIFY PRIMARY COLOR(S)

books = {}
def color_model(directory):
    allRGBColors = []
    numOfImages = 0
    imageFileLocs = []
    for imageFile in os.listdir(directory): #iterate through all the files in the folder
      if imageFile.endswith('.png') or imageFile.endswith('.jpg'): #only look at image files
        numOfImages += 1
        imageFileLocs.append(os.path.join(directory, imageFile))
      else:
        continue
    

    while numOfImages > 0:
      for imgLoc in imageFileLocs:
        result = user_item(imgLoc)
        # print(result)
        numOfImages -= 1

        k = 1 #You can change this value to create as many or few color clusters. I want only 1 for now.
        clf = KMeans(n_clusters = k) #using KMeans model for clustering
        labels = clf.fit_predict(result) #using the reshaped modItem

        counts = Counter(labels) #count occurences of unique labels (colors)
        center_colors = clf.cluster_centers_ #to find the colors
        ordered_colors = [center_colors[i] for i in counts.keys()]
        hex_colors = [RGB2HEX(ordered_colors[i]) for i in counts.keys()]
        rgb_colors = [ordered_colors[i] for i in counts.keys()]
        books[imgLoc] = rgb_colors

        #Show a pie chart of the colors (just for funsies)
        # plt.figure(figsize = (8, 6))
        # plt.pie(counts.values(), labels = hex_colors, colors = hex_colors)
        # plt.show()
        allRGBColors.append(rgb_colors)
    return allRGBColors

#-----------------------------------------------------------------------------------------------------------------#

