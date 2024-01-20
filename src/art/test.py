import os
import pprint
import pymorphy2
import cross
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

pp = pprint.PrettyPrinter(width=80, compact=True)
vectorizer = TfidfVectorizer()
morph = pymorphy2.MorphAnalyzer()

news_texts = ["наука техника искусственный интеллект"]
folder = "../ria/data/"
fnlist = os.listdir(folder)
count = 0
for i in range(len(fnlist)):
    count += 1
    print(count)
    if count == 365:
        break
    fnlist2 = os.listdir(folder + fnlist[i])
    for j in range(len(fnlist2)):
        news_texts.append(' '.join(
            cross.split_text2(
                cross.get_news_text(f"{folder}{fnlist[i]}/{fnlist2[j]}").replace("&nbsp;", " "))))


def get_keyword(text):
    news = [text] + list(set(cross.split_text2(text)))
    tfidf = vectorizer.fit_transform(news)
    similarities1 = linear_kernel(tfidf[0:1], tfidf).flatten()
    indices1 = similarities1.argsort()[::-1]
    pp.pprint(similarities1[indices1])
    for k in range(1, len(indices1)):
        p = morph.parse(news[indices1[k]])[0]
        if p.tag.POS == 'NOUN':
            return str(p.normal_form)


tfidf_matrix = vectorizer.fit_transform(news_texts)
similarities = linear_kernel(tfidf_matrix[0:1], tfidf_matrix).flatten()

indices = similarities.argsort()[::-1]
pp.pprint(news_texts[indices[1]])
pp.pprint(similarities[indices])

print(get_keyword(news_texts[indices[1]]))
