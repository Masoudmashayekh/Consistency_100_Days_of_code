def life_in_weeks(age):
    total_weeks = 90 * 52
    weeks_pass = age * 52
    week_remains = total_weeks - weeks_pass
    print(f"You have {week_remains} weeks left.")
   
    
    
life_in_weeks(33)