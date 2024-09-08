brukere = {
    "hanjo": "Hanne Johnsen",
    "karsi": "Kari Sirisen",
    "olha": "Ole Hansen"
}

brukere["karsi"] = "Kari Marie Sirisen"
brukere["Lennarrd"] = "Lennard Denby"

print(brukere["hanjo"])

brukere.pop("karsi")
print(brukere)
