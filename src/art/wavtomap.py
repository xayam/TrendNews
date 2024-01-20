import os
import recognizer
from config import *


recognize = recognizer.RecognizerClass()

for fw in folderWav:
    lists = os.listdir(fw)
    audio_list = [fw + a for a in lists if a[-4:] == ".wav"]
    for w in audio_list:
        recognize.create_map(w)
