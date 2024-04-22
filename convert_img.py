from PIL import Image
import io

from PIL import Image
import io
import base64

def connvert_image(base64_data):
    base64_data = base64_data.split(',')[1]
    
    binary_data = base64.b64decode(base64_data)

    image_stream = io.BytesIO(binary_data)
    
    image = Image.open(image_stream)
    
    image.save("output.png", format="PNG")