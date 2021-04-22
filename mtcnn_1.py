# This code detects the face in real-time through your webcam and saves the face in '.jpg' 
from mtcnn import MTCNN
import cv2
import time

time_str = time.strftime("%Y%m%d-%H%M%S")
try:
    cam = cv2.VideoCapture(1)  # it can be 0 / 1
finally:
    cam = cv2.VideoCapture(0)
    
detector = MTCNN()

while True:
    ret, image = cam.read()
    faces = detector.detect_faces(image)
    if len(faces) != 0:
        print(faces)   # It returns the face dimensions JSON 
        bounding_box = faces[0]['box']
        keypoints = faces[0]['keypoints']
        
        # to draw rectangle in face
        
        cv2.rectangle(image,
                      (bounding_box[0], bounding_box[1]),
                      (bounding_box[0] + bounding_box[2], bounding_box[1] + bounding_box[3]),
                      (0, 155, 255),2)
        cv2.circle(image, (keypoints['left_eye']), 2, (0, 155, 255), 2)
        cv2.circle(image, (keypoints['right_eye']), 2, (0, 155, 255), 2)
        cv2.circle(image, (keypoints['nose']), 2, (0, 155, 255), 2)
        cv2.circle(image, (keypoints['mouth_left']), 2, (0, 155, 255), 2)
        cv2.circle(image, (keypoints['mouth_right']), 2, (0, 155, 255), 2)
        
        #adjusting the cropped face dimensions by +-50
        
        crop_img = image[bounding_box[1]-50:bounding_box[1] + bounding_box[3] + 50,
                   bounding_box[0]-20:bounding_box[0] + bounding_box[2] + 35]     
        crop_img = cv2.imwrite('./images/' + time_str + '_croppic.jpg', crop_img)    # saving the cropped face picture
        print("Cropped the face")
        cv2.imshow('image1', image)
        cv2.waitKey(1)
        break

cam.release()
cv2.destroyAllWindows()
