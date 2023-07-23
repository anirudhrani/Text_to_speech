import os
from dataclasses import dataclass
from text_to_speech.constants import *

@dataclass
class TTSConfig:
    app_name: str= APPLICATION_NAME
    artifact_dir:str= os.path.join(os.getcwd(), app_name, ARTIFACT_DIR)
    audio_dir: str= os.path.join(artifact_dir, AUDIO_DIR)
    text_dir: str= os.path.join(artifact_dir, TEXT_DIR)