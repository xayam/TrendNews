
# for riacalculate.py
version = "v2.4"
site = "ria.ru"
name = "TrendNews"
preffix = f"{name}-{version}-{site}-"
domain = f"https://{site}/"

years = [str(a) for a in range(2023, 2013, -1)]
months = [str(b).rjust(2, '0') for b in range(12, 0, -1)]
days = [str(c).rjust(2, '0') for c in range(31, 29, -1)]

# this words will exclude from keywords
all_months = ["январь", "февраль", "март", "апрель", "май", "июнь",
              "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]
all_days = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
all_stop = ["россия", "сми", "ростёха"]

# for riadownload.py
count_day = 366 * 10 + 10  # last count days, which will download
domain_download = f"{domain}sitemap_article.xml?"
