def heie(tabellplass_ordbok):
    if tabellplass_ordbok["Brann"] <= 3:
        return "Brann"
    for lag in tabellplass_ordbok:
        if tabellplass_ordbok[lag] == 1:
            return lag

print(heie({"Rosenborg":4, "Odd": 1, "Molde": 3, "Brann":2}))
print(heie({"Rosenborg":2, "Odd": 1, "Molde":3, "Brann": 4}))