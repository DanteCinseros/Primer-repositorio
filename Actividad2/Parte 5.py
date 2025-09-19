import cv2

cam_port = 0
cam = cv2.VideoCapture(cam_port, cv2.CAP_DSHOW) # back end que me funciono
if not cam.isOpened():
    print("No se pudo abrir la cámara")
    exit()

while True:
    result, frame = cam.read()    
    if result: 
        # Convertir a gris + blur antes de Canny 
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)               
        gray = cv2.GaussianBlur(gray, (3, 3), 0)                     
        edges = cv2.Canny(gray, 50, 150)                            

        cv2.imshow("Canny Edges - Press q to quit", edges)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("No image detected")
        break

cam.release()
cv2.destroyAllWindows()

