student_scores = [150, 142, 120, 160, 120, 40, 54, 180, 94, 130, 200]

sum_scores = 0
for score in student_scores:
    sum_scores += score
    
print(sum_scores)

max = 0
for score in student_scores:
    if max <= score:
        max = score
   
print(max)