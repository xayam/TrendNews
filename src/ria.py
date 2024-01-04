import os.path
import re
import requests
from datetime import date, timedelta

count_day = 30
domain = "https://ria.ru/sitemap_article.xml?"

headers = {
    "User-Agent":
        r"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) " +
        "GoogleBot Gecko/20100101 Firefox/96.0",
    "Content-type": "application/x-www-form-urlencoded"
}


def get_news_text(html):
    r = ""
    result = re.findall('<div class="article__title">(.*?)</div>', html)
    if result:
        for res in result:
            r += res + "\n"
    result = re.findall('<div class="article__text">(.*?)</div>', html)
    if result:
        for res in result:
            r += res + "\n"
    clean = re.compile('<.*?>')
    return re.sub(clean, '', r)


if os.path.exists("../data/"):
    data1 = "../data/"
elif os.path.exists("data/"):
    data1 = "data/"
else:
    raise "Error. Not found data folder"

for day in range(0, count_day + 1):
    yesterday = str(date.today() - timedelta(days=day)).replace("-", "")
    path = data1 + yesterday
    print(path)
    if not os.path.exists(path):
        os.mkdir(path)
    try:
        direct_link = f"{domain}date_start={yesterday}&date_end={yesterday}"
        resp = requests.get(direct_link, timeout=3, verify=False, headers=headers)
        if resp.status_code == 200:
            result = re.findall("<loc>(.*?)</loc>", str(resp.content))
            if result:
                for r in result:
                    newspath = path + "/" + r.split("/")[-1]
                    if os.path.exists(newspath):
                        continue
                    resp = requests.get(r, timeout=3,
                                        verify=False, headers=headers)
                    if resp.status_code == 200:
                        with open(newspath,
                                  mode="w", encoding="utf-8") as f:
                            f.write(get_news_text(str(resp.content, "utf-8")))
                    else:
                        raise Exception(f"1) resp.StatusCode={resp.status_code}")
        else:
            raise Exception(f"2) resp.StatusCode={resp.status_code}")
    except Exception as e:
        print("ERROR: " + e.__str__())
