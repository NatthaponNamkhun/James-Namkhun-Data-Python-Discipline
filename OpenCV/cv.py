import cv as cv

# face-detection
img = cv.imread("me_image.jpg")

cv.imshow("image", img)
cv.waitkey(0)
cv.destroyAllWindows()