from config import *

folder = "original/youtube.com/"
txt_files = [folder + f + ".txt" for f in folders]

for name_path in txt_files:
    with open(name_path, mode="r", encoding="utf-8") as f:
        title_watch = f.readlines()
    channel = name_path.split("/")[-1][:-4]
    txt_links = ""
    for tw in title_watch:
        split1 = tw.strip().split("https://www.youtube.com/watch?v=")
        title = split1[0].strip()
        watch = split1[1].strip().split("&")[0]
        txt_links += f"watch?v={watch}\n"
        with open(folder + channel + "/title/" + watch + ".txt",
                  mode="w", encoding="utf-8") as f:
            f.write(title)
    with open(folder + channel + "/links.txt", mode="w", encoding="utf-8") as f:
        f.write(txt_links.strip())
