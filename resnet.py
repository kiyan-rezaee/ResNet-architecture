from base64 import decode
import os
from matplotlib.pyplot import axis

from pytest import CaptureFixture
os.path.expanduser('~/.keras/models')
from tensorflow.keras.applications.resnet import ResNet152
from tensorflow.keras.applications.resnet import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np

model = ResNet152(weights='imagenet')

# print(model.summary())

# Evaluation

# for i in range(1, 4):
#     if i == 3:
#         img = image.load_img(f'{i}.jpeg', target_size=(224, 224))
#     else:    
#         img = image.load_img(f'{i}.jpg', target_size=(224, 224))

#     independent_variables = image.img_to_array(img)
#     independent_variables = np.expand_dims(independent_variables, axis=0)
#     # print(np.shape(independent_variables))

#     independent_variables = preprocess_input(independent_variables)

#     predictions = model.predict(independent_variables) # 1000 outputs

#     print(decode_predictions(predictions, top=3))

import cv2 

capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    frame = cv2.resize(frame, (224, 224))
    image = frame[..., ::-1] #BGR(opencv) to RGB(model)
    image = np.expand_dims(image, axis=0)
    image = preprocess_input(image)
    predicitons = model.predict(image)
    name = decode_predictions(predicitons, top=1)[0][0][1]
    cv2.putText(frame, name, (50,50), cv2.FONT_HERSHEY_PLAIN, 1.0, ((0, 0, 255)))
    cv2.imshow('webcam', frame)
    if cv2.waitKey(1) == 13: # press enter by user
        break
capture.release()
cv2.destroyAllWindows()