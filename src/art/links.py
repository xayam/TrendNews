import os
import re

folder = "original/youtube.com/"
filenames = os.listdir(folder)

for name in filenames:
    with open(folder + name, mode="r", encoding="utf-8") as f:
        html = f.read()
    result = re.findall(r"watch\?v=[a-zA-Z\-_0-9]+", html)
    if result:
        text = ""
        result = set(result)
        for r in result:
            text += r + "\n"
        with open(folder + name[:-4] + "_.txt", mode="w", encoding="utf-8") as f:
            f.write(text.strip())
