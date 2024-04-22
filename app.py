from flask import Flask, jsonify,request,send_file
from flask_cors import CORS

from get_emotions import get_prediction
from convert_img import connvert_image

app = Flask(__name__)
CORS(app)

@app.route("/upload",methods = ['POST'])
def predict():
    image = request
    connvert_image(image)
    emotion = get_prediction()

    return {"emotion":emotion}

if  __name__ == "__main__":
    app.run(host='localhost',port=5010,debug=True)