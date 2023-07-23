import os, sys
import base64
from text_to_speech.constants import *
from text_to_speech.exception import tts_exception
from text_to_speech.logging import logger
from text_to_speech.entity.config_entity import TTSConfig
from gtts import gTTS

class TTS_Application():
    def __init__(self, app_config= TTSConfig()) -> None:
        try:
            self.app_config= app_config
            self.artifact_dir= app_config.artifact_dir
            self.audio_dir= app_config.audio_dir
            self.text_dir= app_config.text_dir
        except Exception as e:
            raise tts_exception(e, sys)
    
    def text2speech(self, text, accent):
        try:
            # Take user input and push that to a text file.
            text_file_name= TEXT_FILE_NAME
            text_file_path= os.path.join(self.text_dir, text_file_name)
            os.makedirs(self.text_dir,  exist_ok= True)
            with open(text_file_path, "a+") as file:
                file.write(f'\n{text}')

            # GTTS input
            tts= gTTS(text= text, lang= 'en', tld= accent, slow= False)
            audio_file_name= f"converted_file{CURR_TIME}.mp3"
            os.makedirs(self.audio_dir, exist_ok= True)
            # Saving audio file
            audio_file_path= os.path.join(self.audio_dir, audio_file_name)
            tts.save(audio_file_path)
            
            # Giving Audio in content
            with open(audio_file_path,"rb" ) as file:
                my_string= base64.b64encode(file.read())

            return my_string
        except Exception as e:
            raise tts_exception(e, sys)