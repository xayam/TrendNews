import re
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pprint
from bs4 import BeautifulSoup


pp = pprint.PrettyPrinter(width=80, compact=True)


def get_sim(embeddings_1, embeddings_2=None):
    # sim = [[0 for _ in range(len(labels_1))] for _ in range(len(labels_1))]
    # embeddings_1 = embed_text(labels_1)
    sim = 1 - np.arccos(cosine_similarity(embeddings_1, embeddings_2)) / np.pi
    return sim


def split_text(text):
    result = re.findall(r"\b[\-цукенгшщзхъфывапролджэячсмитьбю]+\b", text)
    return result


def split_text2(text):
    result = re.findall(r"\b[йёцукенгшщзхъфывапролджэячсмитьбю]+\b", text)
    return result


def get_news_text(filepath):
    with open(filepath, mode="r", encoding="utf-8") as f:
        text = f.read()
    soup = BeautifulSoup(text, 'lxml')
    for data in soup(['style', 'script', 'img', 'noindex']):
        data.decompose()
    for data in soup.find_all("div", {'class': 'article__meta'}):
        data.decompose()
    for data in soup.find_all("div", {'class': 'article__announce'}):
        data.decompose()
    for data in soup.find_all("div", {'class': 'article__aggr'}):
        data.decompose()
    for data in soup.find_all("div", {'class': 'article__article'}):
        data.decompose()
    for _ in soup.find_all('a'):
        soup.a.unwrap()
    quote = soup.find_all('div', class_='layout-article__600-align')
    if len(quote) > 0:
        quote = quote[0]
    else:
        print("WARNING. Not found 'div', class_='layout-article__600-align'")
        return ""
    rep = re.compile('<.*?>')
    quote = rep.sub("\n", str(quote)).strip()
    quote = quote.replace("«\n", "\n")
    quote = quote.replace(" \n", "\n")
    rep = re.compile('\n+')
    quote = rep.sub("\n", str(quote))

    return quote.replace("\xa0", "&nbsp;").lower()
