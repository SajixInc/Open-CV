import cv2
import numpy as np
import pytesseract
import os
import datetime


pytesseract.pytesseract.tesseract_cmd = r"C:\Users\madhu\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"


#     print('convert function exception')
def covert(x, y, w, h, im2):
    # if h >= 400 and h < 1000 and w > 400:
        # print(h,w)
      
        # print(width,'--------')
        lis = []
        f = open('test.txt', 'a')
        rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 5)

        # rect = cv2.rectangle(im2, (x, y), (x + width2, y + h), (0, 255, 255), 3)
        # print(h,width)
        
        cropped = im2[y:y + h, x:x + w]
        # print(w,'----------')
        img = cv2.resize(rect, (1020, 750))
        cv2.imshow('d', img)
        cv2.waitKey(3)
        text = pytesseract.image_to_string(cropped)
        print(text)
        f = open('text.txt', 'a')
        f.write(text)
        f.close()

area = []
value = []
def ima(x, y, w, h, im2, img_file):
    # #print(x,y)
    im2 = cv2.imread(im2)
    cv2.putText(im2, 'Rectangle', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
    rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 5)
    # img = cv2.resize(rect, (1020, 750))
    # cv2.imshow('d', img)
    # cv2.waitKey(0)
    # print(x, y)
    covert(x, y, w, h, im2)
   

area = []
value = []

def img_detect(img_path, img_file):
        # try:
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 50, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, 1, 2)
    for cnt in contours:
        x1, y1 = cnt[0][0]
        approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(cnt)

            ratio = float(w) / h
            if ratio >= 0.9 and ratio <= 1.1:
                pass
            else:
                area.append((h * w))
                value.append((h, w, x, y))
                # he.append(h)
    for i in range(len(area)):
        # if value[i][1]>=0 and value[i][1]>100:
        xa = value[i][2]
        ya = value[i][3]
        l = value[i][0]
        w = value[i][1]
        # cv2.rectangle(img, (xa, ya), (xa + w, ya + l), (0, 255, 0), 2)
        ima(x=xa, y=ya, w=w, h=l, im2=img_path, img_file=img_file)

def image_upload(image_file):
    l = os.listdir(image_file)
    path = image_file
    for k in range(len(l)):
        print(k, 'started')
        area.clear()
        value.clear()
        # he.clear()
        img_detect(img_path=f"{path}\{l[k]}", img_file=l[k])
        # print(k, 'done')

# image_upload(r"D:\projects\conversion\cinverstion1\google\pytesseract\pytessract\pdf to image\images")
image_upload(r"D:\projects\pro_liar_repo\ocr_tesseract\OCR_tesseract\images")