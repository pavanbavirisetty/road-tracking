import cv2

img_file = 'images/car1.jpg'
video = cv2.VideoCapture('road.mp4')

car_tracker = cv2.CascadeClassifier('cars.xml')
ped_tracker = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')

while True:

 # img = cv2.imread(img_file)
   read_successful , frame = video.read()   

   bnw = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

   car = car_tracker.detectMultiScale(bnw)
   ped = ped_tracker.detectMultiScale(bnw)

   print(car)
   print(ped)

   for (x,y,w,h) in car: 

      cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
    
   for (x,y,w,h) in ped:

     cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)

   cv2.imshow('car detector',frame) 

   key = cv2.waitKey(1)

   if key == 32:
       break

video.release()


print('code completed')