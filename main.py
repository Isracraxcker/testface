import cv2 


# Se hace referencia a la haarcascade.
face_cascade = cv2.CascadeClassifier ('haarcascade_frontalface_default.xml')


#Referencia hacia la camara.
cap = cv2.VideoCapture(0)

# While infinito para detectar fotogramas.
while True:
    _, img = cap.read()
    #Convertimos a escala de grises
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #almacenar todas las caras
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    #Se presenta un cuadrado para las caras que detectan
    for (x, y, w,h) in faces:
        cv2.rectangle(img, (x, y),(x+w, y+h),(255, 0, 0), 2)
    #Se muetra el fotograma ya modificado    
    cv2.imshow('img', img)
    k = cv2.waitKey(30)
    if k == 27: # 27 es el ascii para esc
      break
cap.release() 
