from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np


def get_prediction():
    model = load_model('edm_v2.keras')  
    
    img_path = 'output.png'  
    img = image.load_img(img_path, target_size=(64, 64))  
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  
    img_array /= 255.0  
    
    predictions = model.predict(img_array)
    
    
    emotion_labels = ['Angry',  'Happy',  'Neutral', 'Sad', 'Surprise']
    predicted_class = np.argmax(predictions)
    predicted_emotion = emotion_labels[predicted_class]
    
    return predicted_emotion

