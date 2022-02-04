from glrlm import GLRLM
import cv2

IMG_PATH = 'assets/eiproject-logo.jpg'

img = cv2.imread(IMG_PATH)
app = GLRLM()
glrlm = app.get_features(img, 8)
print(glrlm.Features)