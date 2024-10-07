liste = [10, 20, 30, 40, 50]

for i, tall in enumerate(liste):
    print(f"indeks {i} har verdi {tall}")

print("------------------------")

for i in range(len(liste)):
    print(f"indeks {i} har verdi {liste[i]}")

print("------------------------")

ordbok = {
    1: "en",
    2: "to",
    3: "tre"
}

print("------------------------")

for nokkel, verdi in ordbok.items():
    print(f"nøkkel: {nokkel}, verdi: {verdi}")

print("------------------------")

for nokkel in ordbok:
    print(f"nøkkel: {nokkel}, verdi: {ordbok[nokkel]}")