import os, sys
from flask import Flask, request, render_template
from text_to_speech.constants import *
from text_to_speech.logging import logger
from text_to_speech.exception import tts_exception
from text_to_speech.entity.config_entity import TTSConfig
from text_to_speech.components.TextToSpeech import TTS_Application
from text_to_speech.components.get_accent import get_accent_message, get_accent_tld


app= Flask(__name__)
#CORS(app)

@app.route('/', methods= ['GET'])
#@cross_origin
def home():
    try:
        accent_list= get_accent_message()
        return render_template('index.html', accent_list= accent_list)
    except Exception as e:
        raise tts_exception(e, sys)

@app.route("/predict", methods= ['POST','GET'])
#@cross_origin()
def predict():
    try:
        if request.method== 'POST':
            text_data= request.json['data']
            accent_input= request.json['accent']
            accent= get_accent_tld(accent_input)
            
            result= TTS_Application().text2speech(text_data, accent= accent)
            return {"data": result.decode("utf8")}
    except Exception as e:
        print(e)
        raise tts_exception(e, sys)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug= False)