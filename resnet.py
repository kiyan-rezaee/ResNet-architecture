import os
os.path.expanduser('~/.keras/models')
from tensorflow.keras.applications.resnet import ResNet152
from tensorflow.keras.applications.resnet import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np

model = ResNet152(weights='imagenet')

# print(model.summary())

# Evaluation

for i in range(1, 4):
    if i == 3:
        img = image.load_img(f'{i}.jpeg', target_size=(224, 224))
    else:    
        img = image.load_img(f'{i}.jpg', target_size=(224, 224))

    independent_variables = image.img_to_array(img)
    independent_variables = np.expand_dims(independent_variables, axis=0)
    # print(np.shape(independent_variables))

    independent_variables = preprocess_input(independent_variables)

    predictions = model.predict(independent_variables) # 1000 outputs

    print(decode_predictions(predictions, top=3))