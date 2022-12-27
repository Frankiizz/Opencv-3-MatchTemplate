import cv2

img = cv2.imread("imgs/img.png")
temp = cv2.imread("imgs/target.png")

dim = temp.shape


result = cv2.matchTemplate(img, temp, cv2.TM_SQDIFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

if max_val > 0.7:
    cv2.rectangle(img, min_loc, (min_loc[0] + dim[0], min_loc[1] + dim[1]), (0, 0, 225), 2)
    cv2.imshow("img", img)
    cv2.waitKey(0)

