import cv2
import numpy as np
img=np.zeros([600,900,3],dtype=np.uint8)#heigh =600     ,  width=900
#backgroung
img=cv2.rectangle(img,(0,0),(900,500),(255,255,85),-1)
img=cv2.rectangle(img,(0,500),(900,600),(0,102,51),-1)
#sun
img=cv2.circle(img,(150,100),60,(0,255,255),-1)
img=cv2.circle(img,(150,100),70,(0,255,255),5)
#tree
img=cv2.line(img,(710,500),(710,420),(30,65,155),15)
#tree leafs
tringle =np.array([[640,420],[780,420],[710,250]],dtype=np.int32)
cv2.fillPoly(img,[tringle],(65,180,70))
#write text
font=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
img=cv2.putText(img,"i love python",(120,550),font,1.5,(255,255,255),2)
cv2.imwrite("graphic_tree_with_python.png",img)
img=cv2.imshow("graphic",img)
img=cv2.waitKey(0)
cv2.destroyAllWindows()

