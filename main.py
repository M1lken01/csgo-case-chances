import json
import random
import time
import colored
from os import system

data = {"tries": 0, "blue": 0, "purple": 0, "pink": 0, "red": 0, "gold": 0}
cfg = {"no-save": False, "cases": 9999, "delay": 0.05, "auto": False , "reset": False, "gold-stop": False}
dark = colored.fg(232)
light = colored.fg(231)
stop = False

def main():
    system("title csgo-case-chances")
    global data, cfg
    if not cfg["reset"]:
        with open("db.json", "r") as db:
            d = json.load(db)
            db.close()
        data = d
    with open("cfg.json", "r") as db:
        d = json.load(db)
        db.close()
    cfg = d
    print(colored.bg(234) + str(cfg))
    print(f'| count   | quality | quality |' + colored.bg(0))
    caseLoop()


def caseLoop():
    if cfg["reset"]:
        global data
        data = {"tries": 0, "blue": 0, "purple": 0, "pink": 0, "red": 0, "gold": 0}
    global stop
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
            c = colored.bg(136) + dark
            if cfg["gold-stop"]:
                stop = True
        elif n <= 89514:
            data["red"] += 1
            t = "Red"
            c = colored.bg(124)
        elif n <= 409207:
            data["pink"] += 1
            t = "Pink"
            c = colored.bg(161)
        elif n <= 2007672:
            data["purple"] += 1
            t = "Purple"
            c = colored.bg(54)
        elif n <= 9999999:
            data["blue"] += 1
            t = "Blue"
            c = colored.bg(18)
        print(c + f'| {m:07} | {n:07} | {t:7} |' + colored.bg(0) + light)
        time.sleep(cfg["delay"])
    saveToDb()


def saveToDb():
    with open("db.json", "r") as db:
        d = json.load(db)
        db.close()
    d = data
    getData = d
    if cfg["no-save"]:
        info(getData)
        return
    with open("db.json", "w") as db:
        json.dump(d, db)
        db.close()
    info(getData)


def info(db):
    print(f"""---------------------------------{colored.bg(234)}
Values:
{colored.bg(18)} Blues   : {db["blue"]:07}{colored.bg(234)}
{colored.bg(54)} Purples : {db["purple"]:07}{colored.bg(234)}
{colored.bg(161)} Pinks   : {db["pink"]:07}{colored.bg(234)}
{colored.bg(124)} Reds    : {db["red"]:07}{colored.bg(234)}
{colored.bg(136)}{dark} Golds   : {db["gold"]:07}{colored.bg(234)}{light}
Info:
 Cases   : {db["tries"]:07}{colored.bg(0)}
---------------------------------""")
    if not cfg["auto"]:
        input('Enter to continue.\n')
    if stop:
        input("Enter to exit.")
    else:
        caseLoop()


if __name__ == '__main__':
    main()
