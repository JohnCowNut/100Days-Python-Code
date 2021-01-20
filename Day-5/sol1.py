# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])  # convert to numbers
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
result = 0
count = 0
for studentHeigh in student_heights:
    result += studentHeigh
    count += 1
print(round(result/count))
