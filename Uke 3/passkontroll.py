personer = [
    [0, "Ole", "Osloveien 1", "41329938", "Spania"],
    [1, "Kari", "Bergveien 2", "48290012", "Italia"],
    [2, "Per", "Solbakken 3", "47231122", "Frankrike"],
    [3, "Anna", "Fjellveien 4", "45981123", "Tyskland"],
    [4, "Lars", "Sjøveien 5", "45872034", "Hellas"]
]

output = f"{personer[0][1]} med id {personer[0][0]} fra {personer[0][2]} har telefonnummer: {personer[0][3]} og skal til {personer[0][4]}"

print(output)
print("Navn: ", personer[0][1])