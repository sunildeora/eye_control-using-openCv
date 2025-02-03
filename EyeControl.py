import cv2
import mediapipe as mp
import pyautogui # mouse and keyboard programmatically

cam = cv2.VideoCapture(0)

face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)#add it will give 478 dots(landmarks)
screen_w,screen_h=pyautogui.size()

while True:
    _,frame = cam.read() 
    frame=cv2.flip(frame,1)# flip the vertically
    rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
   # print(landmark_points)
    frame_h,frame_w,_=frame.shape # h = height, w = width
    if landmark_points:
       landmarks = landmark_points[0].landmark
       for id, landmark in enumerate(landmarks[474:478]): # this is left eye points
         x= int(landmark.x*frame_w)
         y= int(landmark.y*frame_h)
         print(x,y)
         cv2.circle(frame,(x,y),3,(0,255,255))
         if id ==1: # id = 1 it means it select the landmark
             screen_x=screen_w*landmark.x # x scale size
             screen_y=screen_h*landmark.y
             pyautogui.moveTo(screen_x,screen_y)#access the mouse by eye
       left=[landmarks[145],landmarks[159]]#landmark on left eye
       for landmark in left:
           x=int(landmark.x*frame_w)
           y=int(landmark.y*frame_h)
           cv2.circle(frame,(x,y),3,(0,255,255)) 
       if(left[0].y-left[1].y)<0.01:# upper and lower point 
          pyautogui.click()
          pyautogui.sleep(1)
    cv2.imshow('Eye Controlled Mouse',frame)
    cv2.waitKey(10)# wait to run in milliseconds