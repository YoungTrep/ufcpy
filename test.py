from ufcpy import find_fighter_by_fullname

for name in ["Jon Jones", "Nariman Abbassov" , "Holly Holm"]:
    figher = find_fighter_by_fullname(name)
    print(figher.wins_by_dec_percentage)