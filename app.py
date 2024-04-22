from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import cv2

model = load_model('edm.keras')  
img_path = 'angry.jpeg'  
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (64, 64))

img_array = cv2.merge([img, img, img])


img_array = np.expand_dims(img_array, axis=0)


img_array = img_array.astype('float32') / 255.0

print(img_array)
predictions = model.predict(img_array)

# Interpret the results
emotion_labels = ['Angry', 'Contempt', 'Disgust','Fear', 'Happy', 'Sadness', 'Surprise']
predicted_class = np.argmax(predictions)
predicted_emotion = emotion_labels[predicted_class]

print("Predicted Emotion:", predicted_emotion)
print("Predicted Probabilities:", predictions)
