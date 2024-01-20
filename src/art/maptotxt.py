import json
import os
from config import *


for mp in folderMap:
    lists = os.listdir(mp)
    map_list = [mp + a for a in lists if a[-5:] == ".json"]
    for m in map_list:
        with open(m, mode="r", encoding="utf-8") as map_json:
            R_start, R_end, R_word = r_map(json.load(map_json))
        text = ""
        for w in R_word:
            text += w + " "
        split1 = m.split("/")
        name = split1[-1][:-5] + ".txt"
        output = "/".join(split1[:-2]) + "/txt/" + name
        with open(output, mode="w", encoding="utf-8") as f:
            f.write(text.strip())
        print(output)
