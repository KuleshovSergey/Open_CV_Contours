import cv2
import sys
import numpy as np
import math

gaussian_blur_size = (5, 5)

# Читаем изображение из файла
img_rgb = cv2.imread(sys.argv[1])
# Добавляем размытие
img_rgb = cv2.GaussianBlur(img_rgb, gaussian_blur_size, 0)
# Преобразовать изображение в оттенки серого
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
# Преобразуем в чёрнобелое изображение
T, img_gray = cv2.threshold(img_gray, 60, 255, cv2.THRESH_BINARY)
# Находим контуры
contours = cv2.findContours(img_gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
#img_res = cv2.drawContours(img_rgb, contours, -1, (0,255,0), 4)
for cont in contours:
        #сглаживание и определение количества углов
        sm = cv2.arcLength(cont, True)
        # Если периметр контура удоблетворяет условиям обрабатываем
        if sm > 300 and sm < 900:
            apd = cv2.approxPolyDP(cont, 0.1*sm, True)
        # Если у контура 4 угла отображаем его
        if len(apd) == 4:
            cv2.drawContours(img_rgb, [apd], -1, (0,255,0), 4)
cv2.imwrite('result.jpg', img_rgb)
while True:
    cv2.imshow('Result',img_rgb)
    if cv2.waitKey(1) == 27:
        break