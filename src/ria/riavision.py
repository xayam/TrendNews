import re


def template2html(data0, year, month, keywords, current, config):
    with open(f"riatemplate.html", mode="r", encoding="utf-8") as f:
        template = f.read()
    with open(f"fuse.js", mode="r", encoding="utf-8") as f:
        fuse = f.read()
    rep = re.compile("//__FUSE__")
    result = rep.sub(fuse, template)
    output = "points = ["
    ind = -1
    for data in data0:
        ind += 1
        for i in range(len(data)):
            xx = 'canvas.width - (' + str(i) + ' / ' + str(len(data) - 1) + ') * canvas.width'
            yy = '(' + str(ind) + ' / ' + str(len(data0) - 1) + ') * canvas.height'
            output += '{\nx: ' + xx + ', y: ' + yy + ', info: "&nbsp;&nbsp;&nbsp;' + \
                      data[i]["txt"].replace("\\", "&#92;"). \
                      replace('"', "'").replace("'", "&#8242;"). \
                      replace("\n", "<br/><br/>&nbsp;&nbsp;&nbsp;") + '"' + \
                      ', url: "' + data[i]["url"] + '", ' + \
                      'title: "' + data[i]["title"].replace('"', "'") + '", ' + \
                      'year: "' + data[i]["year"] + '", ' + \
                      'month: "' + data[i]["month"] + '", ' + \
                      'day: "' + data[i]["day"] + '", ' + \
                      '},\n'
    output = output[:-2] + '\n];\n'
    output += 'state["year"] = "' + year + '";\n'
    output += 'state["month"] = "' + month + '";\n'
    output += 'state["name"] = "' + config['name'] + '";\n'
    output += 'state["site"] = "' + config['site'] + '";\n'
    output += 'state["antitrend"] = "' + keywords[0] + '";\n'
    output += 'state["antitrendhref"] = "' + \
              data0[current[0]['r']][current[0]['s']]['url'] + '";\n'
    output += 'state["titleantitrend"] = "' + \
              data0[current[0]['r']][current[0]['s']]['title'].replace('"', "'") + '";\n'
    output += 'state["trend"] = "' + keywords[1] + '";\n'
    output += 'state["trendhref"] = "' + \
              data0[current[1]['r']][current[1]['s']]['url'] + '";\n'
    output += 'state["titletrend"] = "' + \
              data0[current[1]['r']][current[1]['s']]['title'].replace('"', "'") + '";\n'
    output += 'document.getElementById("year").value = "' + year + '";\n'
    output += 'document.getElementById("month").value = "' + month + '";\n'
    output += 'state["titledefault"] = "' + year + '.' + month + ' ' + \
              config['name'] + '";\n'
    output += 'preffix = "' + config["preffix"] + '";\n'
    rep = re.compile("//__POINTS__")
    result = rep.sub(output, result)
    with open(f"../{config['preffix']}{data0[-1][-1]['url'].split('/')[-2]}-" +
              f"{data0[0][0]['url'].split('/')[-2]}.html",
              mode="w", encoding="utf-8") as f:
        f.write(result)
