
# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

image = cv2.imread('image2.jpg')

text = pytesseract.image_to_string(image,lang='spa')
print('Texto ', text)

cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
