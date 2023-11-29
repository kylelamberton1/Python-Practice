# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this 
#my mistakes / differences
#sum = (student_heights[0]+student_heights[1]+student_heights[2])
total_height = 0
for height in student_heights:
  total_height += height
print (f"total height = {total_height}")
#number = (n + 1)
number = 0
for student in student_heights:
  number += 1 
print (f"number of students = {number}")

average = round(total_height / number)
print (f"average height = {average}")



  
      
