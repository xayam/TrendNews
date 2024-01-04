import re


def template2html(data, cluster, colors, txt, name, data1):
    with open(f"{data1}../src/template.html", mode="r", encoding="utf-8") as f:
        template = f.read()
    output = "points = ["

    for i in range(len(data)):
        xx = '(' + str(data[i]["index"]) + ' / ' + str(len(data)) + ') * canvasWidth'
        yy = 'canvasHeight - (' + str(data[i]["value"]) + ' + 0.5) * canvasHeight'
        output += ('{x: ' + xx + ', y: ' + yy + ', info: "' +
                   txt[i].replace('"', "'").replace("\n", "<br/><br/>") + '", color: "' +
                   colors[cluster[data[i]["index"]]] + '"},\n')
    output = output[:-2] + '\n];\n'
    output += 'for (var i = 0; i < points.length; i++) { \n    ' + \
              'ctx.fillStyle = points[i]["color"];\n    ' + \
              'ctx.fillRect(points[i]["x"], points[i]["y"], 2, 2); }\n'
    rep = re.compile("//__POINTS__")
    result = rep.sub(output, template)
    with open(f"{data1}../news-trends-{name}.html", mode="w", encoding="utf-8") as f:
        f.write(result)