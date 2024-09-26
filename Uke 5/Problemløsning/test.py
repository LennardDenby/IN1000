def fjern_utsolgte(handleliste, utsolgte):
    nyliste = []
    for vare in handleliste:
        if vare not in utsolgte:
            nyliste.append(vare)
        else:
            print
    
    return nyliste

print(fjern_utsolgte(["melk", "brus", "pasta"], ["kanel","brus"]))