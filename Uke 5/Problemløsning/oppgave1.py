def badminton(per_vil, espen_vil, palle_vil):
    sum_vil = per_vil + espen_vil + palle_vil
    
    return sum_vil == 2
        

print(badminton(True, True, False))
print(badminton(True, True, True))
print(badminton(True, False, False))