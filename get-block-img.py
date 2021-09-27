import requests
import time

url = "https://collectionapi.metmuseum.org/public/collection/v1/"


def getObjectList(params):
    data = requests.get(url + "search", params=params).json()
    return data["objectIDs"]


def getPrimaryImage(objectID):
    data = requests.get(url + "objects/" + str(objectID)).json()
    if "primaryImageSmall" in data:
        return data["primaryImageSmall"]
    return None


def getImageURLs(objectList):
    images = []
    num = 0
    for objectID in objectList:
        image = getPrimaryImage(objectID)
        if image:
            images.append(image)
            num += 1
        if num >= 500:
            break
        time.sleep(1)
    return images


params = {"hasImages": "true", "isPublicDomain": "true", "q": "flowers"}
objList = getObjectList(params)
imageURLs = getImageURLs(objList)

with open("img_url.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(imageURLs))
