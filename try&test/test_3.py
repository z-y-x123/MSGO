import json
with open("../scripts/data/pfas/heigh_pfas_0125_1/data.json","r") as f:
    infos=json.load(f)
print(len(infos["data"]["train"])+len(infos["data"]["val"])+len(infos["data"]["test"]))