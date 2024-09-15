introverte = ["Oscar", "Oda", "Martin", "Kari"]
ekstroverte = ["Caroline", "Sara", "Audun", "Karl"]
bordPlassering = []

for i in range(len(introverte)):
    bordPlassering.append(introverte[i])
    bordPlassering.append(ekstroverte[i])

for i in range(len(bordPlassering)-1):
    print(f"Par: {bordPlassering[i]} og {bordPlassering[i+1]}")