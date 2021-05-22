import face_recognition
import os
import cv2

# preprocessing images
def preProcessImage(image_path):
    
    # This is the raw image taken
    rawImg = cv2.imread(image_path)
    
    # returning the image in RGB format
    return cv2.cvtColor(rawImg, cv2.COLOR_BGR2RGB) 

# encoding images
def faceRecogTrain(path):
    
    # checking all the images in folder
    image_paths = [os.path.join(path, f) for f in os.listdir(path)]
    
    # encoded images will contains face images
    knownEncoding = []
    
    # labels will contains the label that is assigned to the image
    knownName = []
    
    for image_path in image_paths:
        
        # preprocessing image
        properImg = preProcessImage(image_path)
        
        # face recognition with cnn
        boxes = face_recognition.face_locations(properImg)
        
        # encoding faces for prediction
        encodings = face_recognition.face_encodings(properImg, boxes)
        print('Faces found: ', len(encodings))
        
        for encoding in encodings:
            # saving the encodings
            knownEncoding.append(encoding)
            knownName.append('BradleyCooper')               
    
    return knownEncoding, knownName

# face recognition
def predictImages(path,priorEncoded,priorLabels):
    
    # This is the raw image taken
    rawImg = cv2.imread(path)
    
    properImg = preProcessImage(path)
    
    # face recognition with cnn
    boxes = face_recognition.face_locations(properImg)
        
    # encoding faces for prediction
    encodings = face_recognition.face_encodings(properImg,boxes)
    
    names = []
        
    print('Faces found: ', len(encodings))
    
    for encoding in encodings:
        
        # comparing the faces with saved face data
        matches = face_recognition.compare_faces(priorEncoded,encoding)
        name = 'Unknown'
        print(matches)
        if True in matches:
            matchedIdxs = [i for (i, b) in enumerate(matches) if b]
            counts = {}
            print(matchedIdxs)
            for i in matchedIdxs:
                name = priorLabels[i]
                counts[name] = counts.get(name, 0) + 1
                
            name = max(counts, key=counts.get)
        names.append(name)
        
    # drawing the rectangle and labelling the faces
    for ((top, right, bottom, left), name) in zip(boxes, names):
        
    	# draw the predicted face name on the image
    	cv2.rectangle(rawImg, (left, top), (right, bottom), (0, 255, 0), 2)
    	y = top - 15 if top - 15 > 15 else top + 15
    	cv2.putText(rawImg, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,0.75, (0, 255, 0), 2)
        
    # show the output image
    cv2.imshow("Image",rawImg)
    cv2.waitKey(0)

images, labels = faceRecogTrain("folder_path_of_image")
predictImages("path_of_image.jpg",images,labels)