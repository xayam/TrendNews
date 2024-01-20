import os
import audio
from config import *


for fm4a in folderM4a:
    lists = os.listdir(fm4a)
    audio_list = [fm4a + a for a in lists if a[-4:] == ".m4a"]
    convert = audio.AudioClass(audio_list)
    convert.create_wav()
