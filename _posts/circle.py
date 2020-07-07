import cv2
from cv2 import imread
import numpy as np

# 仅输出坐标点
img = imread('img.bmp')
cv2.imshow('ori', img)
cv2.waitKey(0)
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#ret = cv2.adaptiveThreshold(imgray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 5)
#cv2.imshow('ret', ret)
#cv2.waitKey(0)



ret, thresh = cv2.threshold(imgray, 80, 255, 0)

image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_NONE)
cv2.imshow('img', image)
cv2.waitKey(0)

img_new = cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
cv2.imshow('img_new', img_new)
cv2.waitKey(0)
#print(contours)
#print(hierarchy)
print(contours[0])
tmp = contours[0]
tmp.sort(key=lambda x: x)

for i in range(len(hierarchy[0])):
    if hierarchy[0][i][2] == -1:
        big_circle_idx = hierarchy[0][i][3]
        big_circle = contours[big_circle_idx]
        small_circle = contours[i]

        mask_small = np.zeros(img.shape, np.uint8)
        img_small = cv2.drawContours(mask_small, [small_circle], -1, (0, 255, 0), -1)

        mask_big = np.zeros(img.shape, np.uint8)
        img_big = cv2.drawContours(mask_big, [big_circle], -1, (0, 255, 0), -1)

        new_img = cv2.bitwise_xor(img_big, img_small)
        pp = np.transpose(np.nonzero(new_img))
        #print(pp)
        #cv2.imshow('new_img', new_img)
        #cv2.waitKey(0)

"""
# 整图库函数测试
img = imread('dd2.bmp')
cv2.imshow('ori', img)
cv2.waitKey(0)
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 30, 255, 0)
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

new_contour = []
for i in range(len(contours)):
    area = cv2.contourArea(contours[i])
    if area < 11000 and area > 1000:
        x_axis = [item[0][0] for item in contours[i]]
        if max(x_axis) - min(x_axis) < 300:
            new_contour.append(contours[i])

img = cv2.drawContours(img, new_contour, -1, (0,255,0), 3)
cv2.imshow('img', img)
cv2.waitKey(0)

for i in range(len(new_contour)):
    (x, y), radius = cv2.minEnclosingCircle(new_contour[i])
    cv2.circle(img, (int(x), int(y)), 1, (0, 255, 0), 3)
    print(x, y)
cv2.imshow('img', img)
cv2.waitKey(0)

"""
""" 测试
img2 = img
#img2 = cv2.drawContours(img2, [contours[2]], -1, (0, 255, 0), -1)
mask = np.zeros(img2.shape, np.uint8)
img2 = cv2.drawContours(mask, [contours[2]], -1, 255, -1)
#pp1 = np.transpose(np.nonzero(img2))

img1 = img
#img1 = cv2.drawContours(img1, [contours[1]], -1, (0, 255, 0), -1)
mask = np.zeros(img1.shape, np.uint8)
img1 = cv2.drawContours(mask, [contours[1]], -1, 255, -1)
#pp2 = np.transpose(np.nonzero(img1))

new_img = cv2.bitwise_xor(img1, img2)
pp = np.transpose(np.nonzero(new_img))
print(pp)
cv2.imshow('new_img', new_img)
cv2.waitKey(0)
"""
