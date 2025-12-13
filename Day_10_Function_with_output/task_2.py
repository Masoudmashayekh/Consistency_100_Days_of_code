def is_leap_year(year):
    # Write your code here. 
    # Don't change the function name.
    if year % 4 != 0:
        return False
    elif  year % 4 == 0 and year % 100 != 0:
        return True
    elif  year % 100 == 0 and year % 400 != 0:
        return False
    elif year % 400 == 0:
        return True
    


print(is_leap_year(2000))



# Simple checklist
# If not divisible by 4 → ❌ not a leap year
# If divisible by 4 but not by 100 → ✅ leap year
# If divisible by 100 but not by 400 → ❌ not a leap year
# If divisible by 400 → ✅ leap year