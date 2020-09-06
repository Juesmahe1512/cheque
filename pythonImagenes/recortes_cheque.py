from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
I = Image.open("./cheque.jpg")

I1 = I.convert('L') # convierte a escala de grises
print(I1.mode)
I1.save('cheque_gris.tif')

a = np.asarray(I1, dtype=np.float32)
Image.fromarray(a.astype(np.uint8)).save("prueba.jpg")
fecha = a[90:110, 290:435]
plt.figure()
plt.imshow(a, cmap='gray', interpolation='nearest')
plt.title('cheque')
plt.figure()
plt.imshow(fecha, cmap='gray', interpolation='nearest')
plt.title('fecha')

valor_num = a[83:110, 462:605]
plt.figure()
plt.imshow(valor_num, cmap='gray', interpolation='nearest')
plt.title('Valor numérico')

nombre = a[105:139, 70:480]
plt.figure()
plt.imshow(nombre, cmap='gray', interpolation='nearest')
plt.title('nombre cliente')

valor_tex=a[132:165, 70:640]
plt.figure()
plt.imshow(valor_tex, cmap='gray', interpolation='nearest')
plt.title('valor_tex')

firma=a[165:280, 400:525]
plt.figure()
plt.imshow(firma, cmap='gray', interpolation='nearest')
plt.title('firma')

plt.show()








