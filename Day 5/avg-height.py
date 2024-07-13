# Input a Python list of student heights
sum=0
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  sum+=student_heights[n]

print(sum)
avg_height=sum/len(student_heights)
print(avg_height)

