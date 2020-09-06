import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

#Redimenciona la imagen
#cv2.namedWindow('image', cv2.WINDOW_NORMAL)


image = cv2.imread('cheque.jpg', 0)
#image = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
fecha = image[78:109, 350:570]
valor_cheque = image[78:109, 590:730]
apellido2 = image[112:148, 520:610]
apellido1 = image[110:148, 370:510]
nombre2 = image[106:141, 192:360]
nombre1 = image[102:138, 88:200]
letras = image[134:188, 88:720]
firma = image[175:333, 516:690]

#informativo
#print('image.shape', image.shape)

valor = pytesseract.image_to_string(valor_cheque, lang='spa')
ap1 = pytesseract.image_to_string(apellido1, lang='spa')
ap2 = pytesseract.image_to_string(apellido2, lang='spa')
nom2 = pytesseract.image_to_string(nombre2, lang='spa')
nom1 = pytesseract.image_to_string(nombre1, lang='spa')
letras_out = pytesseract.image_to_string(letras, lang='spa')
fecha_out = pytesseract.image_to_string(fecha, lang='spa')
print('Fecha '+ fecha_out)
print('Cliente: '+valor+' '+nom1+' '+nom2+' '+ap1+' '+ap2)
#print('Valor: '+letras_out+' '+pesos_out)

##text = pytesseract.image_to_string(imageOut, lang='spa')
#escala_grises = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#canny = cv2.Canny(escala_grises, 10, 150)
#print('Texto ', text)
cv2.imshow('Valor', image)
cv2.imshow('text_valor', letras)
cv2.imshow('Firma', firma)
cv2.imshow('Fecha', fecha)
cv2.imshow('Nombre1', nombre1)
cv2.imshow('Nombre2', nombre2)
cv2.imshow('Apellido1', apellido1)
cv2.imshow('Apellido2', apellido2)
cv2.imshow('Valor cheque', valor_cheque)
cv2.waitKey(0)
cv2.destroyAllWindows()
