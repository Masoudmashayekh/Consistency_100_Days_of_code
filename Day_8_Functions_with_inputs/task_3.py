def calculate_love_score(name1, name2):
    list_name1 = list(name1.lower())
    list_name2 = list(name2.lower())
    list_true = list("true")
    list_love = list("love")
    total1 = 0
    total2 = 0
    for i1 in list_name1:
        if i1 in list_true:
            total1 += 1
    for i2 in list_name2:
        if i2 in list_true:
            total1 += 1
    for i in list_name1:
        if i in list_love:
            total2 += 1
    for ii in list_name2:
        if ii in list_love:
            total2 += 1
            
            
    print(f"{total1}{total2}")
    
    
    
calculate_love_score("Kanye West", "Kim Kardashian")