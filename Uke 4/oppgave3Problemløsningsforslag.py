varer = [
    "melk",
    "brød",
    "egg",
    "smør",
    "melk",
    "ost",
    "brød",
    "appelsinjuice",
    "søtpaprika",
    "egg",
    "banan",
    "potet",
    "kaffe",
    "smør",
    "te",
    "banan",
    "melk"
]

varerMap = {}

for vare in varer:
    if vare not in varerMap:
        varerMap[vare] = 1
    else:
        varerMap[vare] += 1

unikeVarer = list(set(varer))
unikeVarer.sort()

for vare in unikeVarer:
    print(f"Varen: {vare} har {varerMap[vare]} ijen")