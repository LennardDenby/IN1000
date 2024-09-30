def legg_til_bokstav(ordliste, bokstav):
    for i in range(len(ordliste)):
        ordliste[i] += bokstav
    return ordliste


def hovedprogram():
    ordliste = ["Je", "de", "se"]
    ordliste = legg_til_bokstav(ordliste, "g")
    print(ordliste)


hovedprogram()