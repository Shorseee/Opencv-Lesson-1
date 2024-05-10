import cv2

img=cv2.imread("pika.png", 1)

B, G, R = cv2.split(img)

cv2.imshow("original", img)
cv2.imshow("blue saturated", B)
cv2.imshow("green saturated", G)
cv2.imshow("red saturated", R)

cv2.waitKey(0)

cv2.destroyAllWindows()