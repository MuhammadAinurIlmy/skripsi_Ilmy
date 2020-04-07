import cv2
import numpy as np
# library riquest
# from imutils.video import VideoStream
import time
import array
import datetime


# =======Variabel pada mouse========
drawing = False
point1 = ()
point2 = ()

Mouse_count = False
# ==================================

# def untuk membuat fungsi
# membuat fungsi garis mouse
# vs = VideoStream(src=-1).start()


def mouse_drawing(event, x, y, flags, params):
    global point1, point2, drawing, Mouse_count

    # ----------Mouse 1-------
    if Mouse_count == False:
        if event == cv2.EVENT_LBUTTONDOWN:
            if drawing is False:
                drawing = True
                point1 = (x, y)
            # else:
                # drawing = False

        elif event == cv2.EVENT_MOUSEMOVE:
            if drawing is True:
                point2 = (x, y)
        elif event == cv2.EVENT_LBUTTONUP:
            drawing = False
            Mouse_count = True

# =================================


# -----membaca video----
cap = cv2.VideoCapture('cars.mp4')


cv2.namedWindow('Detection')
cv2.setMouseCallback('Detection', mouse_drawing)

jumlahMobil = 0

# saat program berjalan
while True:

    ret, frames = cap.read()
    cascadeCar = cv2.CascadeClassifier('cars.xml')
    # cascadeBike = cv2.CascadeClassifier('motor.xml')
    resize = cv2.resize(frames, (854, 480), interpolation=cv2.INTER_LINEAR)

    # ==========membuat ROI==========
    if point1 and point2:
        # membuat persegi
        r = cv2.rectangle(resize, point1, point2, (100, 50, 200), 3)
        frame_ROI = resize[point1[1]:point2[1], point1[0]:point2[0]]

        # --------Deteksi Cascade dalam ROI-------
        if drawing is False:
            # mengconvert video ke grayscale
            ROI_greyscale = cv2.cvtColor(frame_ROI, cv2.COLOR_BGR2GRAY)
            # deteksi objek dalam video
            cascade_ROI = cascadeCar.detectMultiScale(ROI_greyscale, 1.2, 2)

            # ------------
            line = cv2.line(frame_ROI, (0, 10), (900, 10), (255, 0, 0), 3)
            for(x, y, w, h) in cascade_ROI:
                a = cv2.rectangle(line, (x, y), (x+w, y+h), (0, 255, 0), 2)
                # membuat Text
                # jumlahMobil += cascade_ROI.shape[0]
                cv2.putText(frame_ROI, "Jumlah Objek: " + str(cascade_ROI.shape[0]), (
                            200, frame_ROI.shape[0] - 15), cv2.FONT_HERSHEY_TRIPLEX, 0.7, (0, 0, 255), 1)

            # -----------------------------------------
            # ======================================================
# -------------------------------------
            objek = [cascade_ROI]
            now = datetime.datetime.now()
            hitung = 0
            for n in objek:
                x = len(n)
                # arr.append(x)
                if x > 0:
                    hitung = x
                    print(hitung)
            # print(arr, end="")

            # print(now, ':', x)

# menghitung objek per 3 detik!
    cv2.imshow('Detection', resize)
    time.sleep(0.1)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
