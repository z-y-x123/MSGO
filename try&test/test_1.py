import json
with open("PFAS_infos.json","r") as f:
    infos=json.load(f)
infos_key=[k for k,v in infos.items()]
print(infos_key)
print(infos["data"].keys())
print(infos["data"]["test"])
