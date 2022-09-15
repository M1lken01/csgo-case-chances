import json
import random
import time
import colored
from os import system

data = {"tries": 0, "blue": 0, "purple": 0, "pink": 0, "red": 0, "gold": 0}
cfg = {"no-save": False, "cases": 9999, "delay": 0.05, "auto": False , "reset": False, "gold-stop": False, "auto-limit": 1}
colors = {"blue": 18, "purple": 54, "pink": 161, "red": 124, "gold": 136}
dark = colored.fg(232)
light = colored.fg(231)
stop = False
limit = 0

def main():
    system("title CSGO case odds simulator")
    global data, cfg
    with open("cfg.json", "r") as db:
        d = json.load(db)
        db.close()
    cfg = d
    print(colored.bg(234) + str(cfg).replace(', ', '\n').replace('{', '').replace('}', ''))
    print(f'| count   | quality | quality |' + colored.bg(0))
    caseLoop()


def caseLoop():
    if cfg["reset"]:
        global data
        data = {"tries": 0, "blue": 0, "purple": 0, "pink": 0, "red": 0, "gold": 0}
    global stop, limit
    limit += 1
    m = 0
    c = colored.bg(235)
    while m < cfg["cases"] and stop == False:
        n = random.randint(0, 9999999)
        m += 1
        t = "none"
        data["tries"] += 1
        if n <= 25575:
            data["gold"] += 1
            t = "Gold"
            c = colored.bg(colors["gold"]) + dark
            if cfg["gold-stop"]:
                stop = True
        elif n <= 89514:
            data["red"] += 1
            t = "Red"
            c = colored.bg(colors["red"])
        elif n <= 409207:
            data["pink"] += 1
            t = "Pink"
            c = colored.bg(colors["pink"])
        elif n <= 2007672:
            data["purple"] += 1
            t = "Purple"
            c = colored.bg(colors["purple"])
        elif n <= 9999999:
            data["blue"] += 1
            t = "Blue"
            c = colored.bg(colors["blue"])
        print(c + f'| {m:07} | {n:07} | {t:7} |' + colored.bg(0) + light)
        time.sleep(cfg["delay"])
    saveToDb()


def saveToDb():
    with open("db.json", "r") as db:
        d = json.load(db)
        db.close()
    
    d.append(data)
    getData = d
    if not cfg["no-save"]:
        with open("db.json", "w") as db:
            json.dump(d, db)
            db.close()
    info(getData[-1])


def info(db):
    print(f"""---------------------------------{colored.bg(234)}
Values:
{colored.bg(colors["blue"])} Blues   : {db["blue"]:07}{colored.bg(234)}
{colored.bg(colors["purple"])} Purples : {db["purple"]:07}{colored.bg(234)}
{colored.bg(colors["pink"])} Pinks   : {db["pink"]:07}{colored.bg(234)}
{colored.bg(colors["red"])} Reds    : {db["red"]:07}{colored.bg(234)}
{colored.bg(colors["gold"])}{dark} Golds   : {db["gold"]:07}{colored.bg(234)}{light}
Info:
 Cases   : {db["tries"]:07}{colored.bg(0)}
---------------------------------""")
    global stop, limit
    if stop or cfg["auto"] == False or limit == cfg["auto-limit"]:
        limit = 0
        stop = False
        input('Enter to continue.\n')
    caseLoop()


if __name__ == '__main__':
    main()
