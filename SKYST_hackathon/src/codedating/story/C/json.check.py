import json

with open('plot.json', 'r', encoding="UTF-8") as f:
    plot = json.load(f)

id_dic = {}

for i in range(len(plot)):
    if plot[i]['type'] == 0:
        id_dic[plot[i]['id']] = plot[i]['next']
    elif plot[i]['type'] == 1:
        id_dic[plot[i]['id']] = plot[i]['next']
    elif plot[i]['type'] == 2:
        id_dic[plot[i]['id']] = plot[i]['next'][1]
    else:
         id_dic[plot[i]['id']] = 100

for key,val in id_dic.items():
        print(id_dic[id_dic[key]])
