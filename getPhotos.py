import os
import json

photosList = os.listdir('E:/projects/photoGallery-flask/static/assets/images')

photosDict = {'photos':[{'id' : 0, 'name' : 'start of list', 'link' : 'url'}]}
currentIndex = 1

for photo in photosList:
    photoEntry = {'id' : currentIndex, 'name' : photo, 'link' : 'assets/images/'+photo}
    photosDict['photos'].append(photoEntry)
    currentIndex += 1

with open('photos.json', 'w') as jsonFile:
    json.dump(photosDict, jsonFile, indent=2)