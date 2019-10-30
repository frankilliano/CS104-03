#Python Richter Scale Calculation 
#Frank Illiano 
#s1288616

Gameover = False 
while not Gameover: 
    Richter = float(input("Enter the Richter scale value or -99 to end: "))

    if Richter == -99: 
        Gameover = False
        break
    if Richter <= 0:
        print("Value must be greater than 0")
    elif Richter >= 8.0:
        print("Most structures fall")
    elif Richter >= 7.0: 
        print("Many buildings destroyed")
    elif Richter >= 6.0:
        print("Many buildings considerably damaged, some collapse")
    elif Richter >= 4.5: 
        print("Damage to poorly constructed buildings")
    else: 
        print("No destruction of buildings")
