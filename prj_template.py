import os
from pathlib import Path

curr_dir= os.getcwd()
poc_title= "text_to_speech"

dir_struct= [
    
    f"requirements.txt",
    "setup.py",
    "app.py",
    ".gitignore",
    "DockerFile",
    f"text_to_speech/artifacts/__init__.py",
    f"text_to_speech/artifacts/tts_audio",
    f"text_to_speech/artifacts/tts_text",

    f"text_to_speech/components/__init__.py",
    f"text_to_speech/components/get_accent.py",
    f"text_to_speech/components/TextToSpeech.py",

    f"text_to_speech/entity/__init__.py",
    f"text_to_speech/entity/config_entity.py",

    f"text_to_speech/exception/__init__.py",
    f"text_to_speech/logging/__init__.py",
    f"text_to_speech/constants.py",
    f"text_to_speech/__init__.py",
    f"templates/"
    ]


for file in dir_struct:
    filepath= Path(file)

    file_dir, file_name= os.path.split(filepath)
    if file_dir!="":
        os.makedirs(file_dir, exist_ok= True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open (filepath , 'w') as r:
            pass