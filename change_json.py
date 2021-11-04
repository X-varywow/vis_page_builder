import json
import os

def change_json(df):
    os.system("cls")
    #print(type(df))
    #print(df)

    with open("vis.json", "r") as f:
        d = json.load(f)

    for title in df:
        if title not in d or d[title] != 1:
            os.system("cls")
            print(title)
            try:
                key = int(input("输入1表示看过，输入0表示没看过，输入2表示不清楚：\n"))
                d[title] = key
            except:
                pass
        
    with open("vis.json","w") as f:
        f.write(json.dumps(d))
