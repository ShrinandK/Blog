# Importing the OpenCV package
import cv2

# This is the raw image taken
rawImg = cv2.imread('image_to_read_path.jpg')

# Resizing of the image
 is required if it is too large. Here I have just given how you can do # this
# resizeImg = 
# cv2.resize(rawImg, (int(rawImg.shape[1]/6),int(rawImg.shape[0]/6)),interpolation = 
# cv2.INTER_AREA)

resizeImg = rawImg

# As OpenCv takes form in BGR we convert to RGB for similarity across all
properImg = cv2.cvtColor(resizeImg, cv2.COLOR_BGR2GRAY)

# Load Haar Cascade for frontal face
haarCasFace = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Get the co ordinates where frontal face is there
facesRect = haarCasFace.detectMultiScale(properImg,scaleFactor = 1.3,minNeighbors = 2,minSize=(30,30))
print('Faces found: ', len(facesRect))

# Rectangle plotting on image for frontal face
for (x,y,w,h) in facesRect:
     cv2.rectangle(resizeImg, (x, y), (x+w, y+h), (0, 255, 0), 2)
     
     
# View image in a window and close when exc is pressed
while True:
    cv2.imshow('Correct Image',resizeImg)
    
# will close the windpw only when Esc key is pressed
    if cv2.waitKey(1) & 0xFF == 27:
        break
    
cv2.destroyAllWindows()