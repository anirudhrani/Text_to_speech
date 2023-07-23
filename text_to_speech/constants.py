from datetime import datetime
APPLICATION_NAME= "text_to_speech"
ARTIFACT_DIR= "artifact"
AUDIO_DIR= "tts_audio"
TEXT_DIR= "tts_text"
TEXT_FILE_NAME= "userinput.txt"

dt_format= "%Y-%m-%d_%H%M%S" # avoid this to get rid of file storage issues due to naming convention"%m-%Y-%d :: %H:%M:%S"
CURR_TIME= f"{datetime.now().strftime(dt_format)}"