import cv2
image = cv2.imread("cartoon.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite("gray.png", gray_image)
inverted_image = 255 - gray_image
cv2.imwrite("inverted.png", inverted_image)
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
cv2.imwrite("blured.png", blurred)
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
cv2.imwrite("cartoonSketch.png", pencil_sketch)
