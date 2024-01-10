import math
import os
import pprint
import gensim
import yake
import numpy as np
from datetime import datetime, timedelta
import pymorphy2

from riaconfig import *
import riacross as cross
import riavision as vision

extractor1 = yake.KeywordExtractor(lan="ru", n=1, dedupLim=0.3, top=1)
extractor10 = yake.KeywordExtractor(lan="ru", n=1, dedupLim=0.3, top=10)
morph = pymorphy2.MorphAnalyzer()
pp = pprint.PrettyPrinter(width=80, compact=True)

all_index = []
if os.path.exists("data/"):
    data1 = "data/"
else:
    raise "ERROR. Not found data folder"

for year in years:
    for month in months:
        result = []
        input_dt = datetime(int(year), int(month), 13)
        next_month = input_dt.replace(day=28) + timedelta(days=4)
        res = next_month - timedelta(days=next_month.day)
        last = str(res.date())[-2:]
        html_name = f"../{preffix}{year}{month}01-{year}{month}{last}" + ".html"
        if os.path.exists(html_name):
            print(f"WARNING. File '{html_name}' exists. Continue...")
            continue
        for day in days:
            folder = year + month + day
            print(folder)
            if not os.path.exists(data1 + folder):
                print("WARNING. '" + data1 + folder + "' folder not exists")
                continue
            fn = os.listdir(data1 + folder)
            sums = []
            title = []
            txt = []
            url = []
            for filename in fn:
                reading = cross.get_news_text(f"{data1}{folder}/{filename}")
                title.append(reading.split("\n")[0])
                txt.append(reading)
                url.append(f"{domain}{folder}/{filename}")
            cr = cross.embed_text(txt)
            sim = np.asarray(cross.get_sim(cr), dtype=np.float32)
            cr = np.asarray(cr, dtype=np.float32)
            for i in range(len(sim)):
                summa = 0.
                for j in range(len(sim[i])):
                    if math.isnan(sim[i][j]):
                        sim[i][j] = 1.
                    summa += sim[i][j]
                sums.append(summa)
            sums = np.asarray(sums, dtype=np.float32)
            sums = sums / len(sim)
            sums = (sums - sums.mean()) / (sums.max() - sums.min())
            sums = [{'value': x,
                     'index': i,
                     'title': title[i],
                     'txt': txt[i],
                     'url': url[i],
                     'year': year,
                     'month': month,
                     'day': day,
                     } for i, x in enumerate(sums)]
            sums.sort(key=lambda x: x["value"], reverse=True)
            result.append(sums)
        keywords = []
        current = []
        for s in [-1, 0]:
            txt0 = []
            all_words = {}
            for r in range(len(result) - 1, -1, -1):
                txt1 = []
                text = result[r][s]['title'].lower()
                ws = cross.split_text(text=text)
                wss = []
                for w in ws:
                    if '-' not in w:
                        wss.append(w)
                        all_words[w] = {'r': r, 's': s}
                txt0.append(' '.join(wss))
            extract = extractor10.extract_keywords(" ".join(txt0))
            words = [e[0] for e in extract]
            words = [i for i in words if words.count(i) == 1]
            nouns = []
            nouns_ = []
            for w in words:
                p = morph.parse(w)[0]
                if (p.tag.POS == 'NOUN') and \
                        (str(p.normal_form) not in all_months + all_days + all_stop):
                    nouns.append(str(p.normal_form))
                    nouns_.append(w)
            for n in range(len(nouns)):
                nouns = ' '.join(nouns).replace(nouns[n], 'а', ' '.
                                                join(nouns).count(nouns[n]) - 1).split(' ')
            print(len(nouns), len(nouns_))
            pp.pprint(nouns)
            pp.pprint(nouns_)
            keyword = gensim.summarization.keywords(' '.join(nouns),
                                                    ratio=None, words=1, split=True,
                                                    scores=False, pos_filter=None,
                                                    lemmatize=False, deacc=False)
            word = keyword[0]
            curr = {}
            print(word)
            for w in range(len(nouns_)):
                p = morph.parse(nouns_[w])[0]
                if str(p.normal_form) == word:
                    curr = all_words[nouns_[w]]
                    print(curr)
                    break
            keywords.append(str(word).capitalize())
            current.append(curr)
        params = {
            'data0': result,
            'year': year,
            'month': month,
            'keywords': keywords,
            'current': current,
            'preffix': preffix
        }
        vision.template2html(**params)
        all_index.append(params)
