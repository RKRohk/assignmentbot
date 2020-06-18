from pathlib import Path
import re

def checkAssignments():
    total = list(range(1806453,1806528))
    notinsection = [1806474,1806515]
    for roll in notinsection:
        total.remove(roll)
    
    p = Path('./assignments')

    for x in p.iterdir():
        print(x)
        lol = re.findall(r'[0-9]{7}',str(x))
        if len(lol) > 0:
            total.remove(int(str(lol[0])))

    print(str(total))
    return total

checkAssignments()