import os, sys
from text_to_speech.constants import *
from text_to_speech.exception import tts_exception
from text_to_speech.logging import logger


def get_accent_message():
        try:
            accent= ["Australian", "South Africa", "British", "Indian", "Canadian", "Irish", "Spanish"]
            return accent
        except Exception as e:
            raise tts_exception(e, sys)


# TLD -> Top Level Domain
def get_accent_tld(user_input):
        try:
            accent_input= {"Australian": "com.au",
                           "South Africa": "co.za", 
                           "British": "co.uk", 
                           "Indian": "co.in", 
                           "Canadian": "ca", 
                           "Irish": "ie",
                           "Spanish": "es"}
            tld= accent_input[user_input]
            return tld
        except Exception as e:
            raise tts_exception(e, sys)
