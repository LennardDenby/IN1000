ord = "heisann"

#dette er 1 løsning:
unikeBokstaver = set(ord)
print(f"Ordet {ord} har {len(unikeBokstaver)} ulike bokstaver")

#løsning nummer 2:
bokstaver = []
for bokstav in ord:
    if bokstav not in bokstaver:
        bokstaver.append(bokstav)

print(f"Ordet {ord} har {len(bokstaver)} ulike bokstaver")