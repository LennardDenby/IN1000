def tell_grader(fag, bsc, msc):
    antalLike = 0
    if fag == bsc:
        antalLike += 1
    if fag == msc:
        antalLike += 1  
    return antalLike

assert tell_grader("informatikk", "informatikk", "informatikk") == 2
assert tell_grader("historie", "informatikk", "informatikk") == 0
assert tell_grader("historie", "informatikk", "historie") == 1