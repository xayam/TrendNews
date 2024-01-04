import pandas as pd
from sklearn.cluster import Birch
import numpy as np
import os
import cross
import matplotlib.pyplot as plt
import vision

counts = [1, 7, 14]
count_day = counts[-1]
n_clusters = 4
colors = ['black', 'blue', 'green', 'red',  'yellow', 'orange', 'gray'][:n_clusters]
count = count_day
txt = []

if os.path.exists("../data/"):
    data1 = "../data/"
elif os.path.exists("data/"):
    data1 = "data/"
else:
    raise "Error. Not found data folder"

fl = os.listdir(data1)
fl.sort(reverse=True)
days_begin = []
days_end = []
index0 = 0
index1 = 0
index = 0
indexs = []
for folder in range(len(fl)):
    fn = os.listdir(data1 + fl[folder])
    for filename in fn:
        with open(f"{data1}{fl[folder]}/{filename}", mode="r", encoding="utf-8") as f:
            txt.append(f.read())
            index += 1
    index1 += 1
    if index1 == counts[index0]:
        days_end.append(fl[0])
        days_begin.append(fl[folder])
        indexs.append(index)
        index0 += 1
    count -= 1
    if count == 0:
        break
cr = cross.embed_text(txt)
sim = np.asarray(cross.get_sim(cr), dtype=np.float32)
cr = np.asarray(cr, dtype=np.float32)
sums = []
for i in range(len(sim)):
    summa = 0.0
    for j in range(len(sim[i])):
        if i == j:
            sim[i][j] = 1.0
        summa += sim[i][j]
    sums.append(summa)
sums = np.asarray(sums, dtype=np.float32)
sums = sums / len(sums)
sums = (sums - sums.mean()) / (sums.max() - sums.min())
# print(sums)
sums = [{'value': x, 'index': i} for i, x in enumerate(sums)]

red_wine_df = pd.DataFrame(data=cr)
brc = Birch(n_clusters=n_clusters)
brc.fit(red_wine_df)
cluster = brc.predict(red_wine_df)

# for i in range(len(sums)):
#    plt.scatter(x=(sums[i]["index"] / len(sums) - 0.5) * 2.,
#                y=sums[i]["value"],
#                color=colors[cluster[sums[i]["index"]]])
# plt.show()

for i in range(len(counts)):
    vision.template2html(data=sums[: indexs[i]],
                         cluster=cluster[: indexs[i]],
                         colors=colors,
                         txt=txt[: indexs[i]],
                         name=days_begin[i] + '-' + days_end[i],
                         data1=data1)


