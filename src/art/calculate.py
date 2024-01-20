import os

from config import *


for ft in folderTxt:
    news_texts = []
    names = []
    fl = os.listdir(ft)
    for fn in fl:
        with open(ft + fn, mode="r", encoding="utf-8") as f:
            text1 = f.read().strip()
        names.append(ft + fn)
        news_texts.append(text1)
    k = []
    top = 15
    for i in range(len(news_texts)):
        # k = []
        progress(f"{i + 1}/{len(news_texts)}")
        keywords = get_keyword2(text=split_text2(news_texts[i]), top=top)
        keywords = keywords[:top]
        k += keywords
    print("")
    k = list(set(k))
    if k:
        keywords = get_keyword2(text=k, top=30)
        keywords = keywords[:]
        pp.pprint(keywords)
