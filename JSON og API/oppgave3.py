import json 
from pathlib import Path
filsti = Path(__file__).parent / "musikk.json"

with open(filsti, encoding="utf-8") as fil:
    data = json.load(fil)

print(data["artister"][0]["navn"]);
print(data["artister"][1]["navn"]);
print(data["artister"][2]["navn"]);
print("land = " + data["artister"][2]["land"])
