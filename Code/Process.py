from statistics import mean
from skimage.feature import blob_log
import glob
from skimage.io import imread
import numpy as np
example_file = glob.glob("file.jpg")[0]

im = imread(example_file, as_gray=True)

blobs_log = blob_log(im,max_sigma=50,min_sigma=10,threshold=0.2)
numrows = len(blobs_log)
print(numrows)


arr = np.array(numrows)
for i in range(0,10):
    if(arr[i]==numrows):
        d = i


road_width = {
    "A":3,
    "B":4,
    "C":5,
    "D":6
}

ratio = arr[d]/road_width[d]

if(ratio <1):
    cars_in_route = 2
    print("no traffic problem .... U can move")
    import cv2
    import numpy as np
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

    cap = cv2.VideoCapture(0)
    count2 = 0

    i = 1

    while 1:
        ret, img = cap.read()
        gray = cv2.cvtColor(img , COLOR_BGB2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y), (x+w,y+h),(255,0,0), 2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            eye = eye_cascade.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color, (ex,ey) , (ex+ew, ey+eh), (0,255,0) , 2)
        cv2.imshow('img', img)
        v = cv2.waitKey(30)
        if(k=27):
            break
    cap.release()
    cv2.destroyAllWindows()
    count2 = len(faces)


    if(cars_in_route>1):
        input_var = input("enter the the type of vehicle...if car press 1 and bus press 2.....")
        if(input_var == 1):
            total_seats = 4
            x1 = total_seats - count2
            print(x1)
        if(input_var == 2):
            total_seats = 10
            X2 = total_seats - count2
            print(x2)

if(ratio>1):

    a = input("if you want to use alternative way press 1:")
    if(a == 1):
        dict = {
            4:"route_A",
            2:"route_B",
            2:"route_C",
            3:"route_D"
        }
        l = []
        m = []
        m = sorted(dict.keys())
        l = sorted(dict.items())

        counter = 0
        for i in range(0,3):
            j = i+1
            for j in range(0,2):
                if(dict[i]==dict[j]):
                    valuess = dict[i]


        if(valuess == m[0]):
            turnings_road = {
                4:"route_A",
                3:"route_B",
                5:"route_C",
                2:"route_D"
            }
            new_turnings = []
            new_turnings = sorted(turnings_road.items())
            variable = new_turnings[0]
            print(variable)

else:

    from statistics import mean
    print("traffic problem is there.....")
    xs = np.array([2,4,6,5,7,9], dtype=np.float64)
    ys = np.array([7,4,9,1,3,2], dtype=np.float64)

    m = (((mean(xs)*mean(ys)) - mean(xs*ys)) / ((mean(xs)*mean(xs)) - mean(xs*xs)))
    b = (mean(ys) - m * mean(xs))
    predict_y =(m*(numrows)+b)
    current_dist = 15
    speed_predict_required = current_dist/predict_y
















