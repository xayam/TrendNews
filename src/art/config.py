import os
import pprint
import re
import sys
from typing import List

import pymorphy2
import numpy as np
import yake
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

import cross

np.random.seed(42)

f = os.getcwd().replace("\\", "/") + "/"

folders = ["dnevikdezainera", "shelnat", "zemscov"]

folderM4a = [f + f"original/youtube.com/{folder}/m4a/" for folder in folders]
folderWav = [f + f"original/youtube.com/{folder}/wav/" for folder in folders]
folderMap = [f + f"original/youtube.com/{folder}/map/" for folder in folders]
folderTxt = [f + f"original/youtube.com/{folder}/txt/" for folder in folders]

all_stop = [
    "первое", "второе", "третье",
    "нуль", "ноль", "один", "два", "три", "четыре", "пять",
    "шесть", "семь", "восемь", "девять", "десять", "двадцать",
    "нулевой", "первый", "второй", "третий", "четвертый", "четвёртый", "пятый",
    "шестой", "седьмой", "восьмой", "девятый", "десятый",
    "одиннадцатый", "двенадцатый", "тринадцатый", "четырнадцатый",
    "пятнадцатый", "шестнадцатый", "семнадцатый", "восемнадцатый", "девятнадцатый", "двадцатый",
    "сто", "тысяча", "миллион", "миллиард", "триллион",
    "январь", "февраль", "март", "апрель", "май", "июнь",
    "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь",
    "рубль", "евро", "доллар", "юань",
    "день", "неделя", "месяц", "год", "полгода", "век",
    "миллиметр", "сантиметр", "метр",
    "миллиграмм", "грамм", "килограмм", "тонна",
    "секунда", "минута", "час", "сутки", "день", "ночь",
    "миллилитр", "литр", "галон",
    "михаил", "алексей", "владимир", "анатолий", "александр", "сергей", "андрей", "антон",
    "серёга", "рудольф", "дмитрий", "архип", "адам", "юра", "юрий", "ваня", "иван", "игорь",
    "чжон", "алекс", "макс", "максим", "саша", "серёжа",
    "ольга", "елена", "марина", "татьяна", "оксана", "наталья", "анастасия", "алла",
    "жанна", "маргарита",
    "алексеев", "иванович", "алексеевич", "валериевич", "иванов", "вадимович",
    "абрамович", "введенский", "владимирович", "рогов", "власович", "донский",
    "москва", "россия",
    "весь", "самый", "наш", "название", "сам", "эн", "теор", "уркварта", "ургул", "атан",
    "такой", "какой", "тот", "этот", "раз", "ютуба",
]


def r_map(data):
    r_start = []
    r_end = []
    r_word = []
    for i in data["fragments"]:
        try:
            for k in i["result"]:
                r_start.append(k["start"])
                r_end.append(k["end"])
                r_word.append(k["word"].lower().replace("ё", "е"))
        except KeyError:
            pass
    return r_start, r_end, r_word


def split_text2(text):
    result = re.findall(r"\b[йёцукенгшщзхъфывапролджэячсмитьбю]+\b", text)
    return result


def progress(message):
    sys.stdout.write("\r" + message)
    sys.stdout.flush()


vectorizer = TfidfVectorizer(norm=None, use_idf=False, smooth_idf=False)
morph = pymorphy2.MorphAnalyzer()
pp = pprint.PrettyPrinter(width=80, compact=True)


def get_keyword(text):
    news = [text] + list(set(cross.split_text2(text)))
    tfidf = vectorizer.fit_transform(news)
    similarities1 = linear_kernel(tfidf[0:1], tfidf).flatten()
    indices1 = similarities1.argsort()[::-1]
    # pp.pprint(similarities1[indices1])
    keys = []
    for k1 in range(1, len(indices1)):
        if similarities1[indices1][k1] == 0.0:
            continue
        p = morph.parse(news[indices1[k1]])[0]
        if (p.tag.POS in ['NOUN', 'ADJF']) and \
                (str(p.normal_form) not in all_stop):
            keys.append(str(p.normal_form))
    return keys


def get_keyword2(text: List[str], top: int) -> List[str]:
    extractor = yake.KeywordExtractor(lan="ru", n=1, dedupLim=0.3, top=top)
    words = []
    for w in text:
        p = morph.parse(w)[0]
        if (p.tag.POS in ['NOUN', 'ADJF']) and \
                (str(p.normal_form) not in all_stop):
            words.append(str(p.normal_form))
    extract = extractor.extract_keywords(" ".join(words))
    return [e[0] for e in extract]
