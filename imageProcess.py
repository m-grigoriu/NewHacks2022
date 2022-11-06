import numpy as np
import cv2 as cv
import os

totalNodes = 500
sensitivityC = 0.2
friendGap = 20

def imgProc(totalNodes, sensitivityC, friendGap) -> None:
    img = cv.imread('images/map3.jpg')

    def crop(img):      # CROP THE IMAGE FIRST
        if(img.shape[1] > img.shape[0]):   # width > height
            img = img[0:img.shape[0], 0:img.shape[0]]
        elif (img.shape[1] < img.shape[0]):  # height > width
            img = img[0:img.shape[1], 0:img.shape[1]]
        
        return img

    img = crop(img)     # resize image to fit global 742 size
    scaleFactor = int(img.shape[1]/742)
    width = int(img.shape[1] * scaleFactor)
    height = int(img.shape[0] * scaleFactor)

    img = cv.resize(img, (width, height), interpolation=cv.INTER_AREA)
    # rescale image to 742 x 742

    gray = gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    threshold, thresh = cv.threshold(gray, 240, 255, cv.THRESH_BINARY )

    blur = cv.GaussianBlur(thresh, (5,5), cv.BORDER_DEFAULT)

    # cv.imshow("blur", blur)

    corners = cv.goodFeaturesToTrack(blur, totalNodes, sensitivityC, friendGap)

    for corner in corners:
        x, y = corner.ravel()
        cv.circle(img, (int(x), int(y)), 5, (0, 0, 255), -1)
    # cv.imshow("coordinates", img)

    newCorners = []
    for i in range(len(corners)):
        newCorners.append([corners[i][0][0], corners[i][0][1]])

    return newCorners

    # with open ("textFiles/nodes.txt", "w") as file:
    #     for corner in corners:  # WHAT WE ACTUALLY WANT
    #         x, y = corner.ravel()[0], corner.ravel()[1]
    #         file.write("[" + str(x) + "," + str(y) + "]" + "\n")
            
    # print(corners)    :   analyse the graph for accuracy.
    # for corner in corners:
    #     x, y = corner.ravel()
    #     cv.circle(img, (int(x), int(y)), 5, (0, 0, 255), -1)

    # img = cv.circle(img, (292, 481), 5, (255, 0, 0), -1)    # find bahen point.