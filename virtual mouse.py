import cv2 #pip install opencv
import mediapipe #pip install mediapipe
import pyautogui #pip install pyautogui
capture_hands=mediapipe.solutions.hands.Hands()
drawing_options=mediapipe.solutions.drawing_utils
screen_width,screen_height=pyautogui.size()
camera=cv2.VideoCapture(0)   #It handles camera of our system
x1=y1=x2=y2=0
while True: # When camera is avaliable it starts raeding
  _,image=camera.read()
  image=cv2.flip(image,1)
  image_height,image_width,_=image.shape  
  rgb_image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
  output_hands=capture_hands.process(rgb_image)
  all_hands=output_hands.multi_hand_landmarks
  if all_hands:
    for hand in all_hands:
      drawing_options.draw_landmarks(image,hand)
      one_hand_landmarks=hand.landmark
      for id,lm in enumerate(one_hand_landmarks):
        x=int(lm.x*image_width)
        y=int(lm.y*image_height)
        #print(x,y)
        if id==8:
          mouse_x=int(screen_width/image_width *x)
          mouse_y=int(screen_height/image_height *y)
          cv2.circle(image,(x,y),10,(0,255,255))
          pyautogui.moveTo(mouse_x,mouse_y)
          x1=x
          y1=y
        if id==4:
          cv2.circle(image,(x,y),10,(0,255,255))
          x2=x
          y2=y
    dist=y2-y1  # difference between the fingers
    print(dist)  
    if(dist<30):
      pyautogui.click() 
    elif(dist>100 and dist<150):
      pyautogui.rightClick()
  cv2.imshow("Hand movement with  mouse gestures",image) #title of the frame 
  key=cv2.waitKey(100)
  if key == 27: # 27 is the esacpe key number
    break
camera.release()
camera.destroyAllWindows() 