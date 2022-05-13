import cv2 as cv


for i in range(3):
    img = cv.imread(f'img/rooms/background{i}.png')
    img = cv.resize(img, (320, 180), interpolation=cv.INTER_NEAREST)
    cv.imwrite(f"img/background{i}.png", img)
    #cv.imwrite(f"img/bg{i}", img)
