# Enter your code here. Read input from STDIN. Print output to STDOUT 
# Enter your code here. Read input from STDIN. Print output to STDOUT 
num = int(input("no od stu : "))
count = 0
number_of_roll_numbers = int(input("Enter the number of roll numbers : "))
for i in range(number_of_roll_numbers+1):
    roll_no = i
french_sub = int(input("french sub : "))
enter_rool_no = input("roll no : ").split(" ")
enter_rool_no =map(int,enter_rool_no)
for j in (enter_rool_no):
  for k in range(french_sub):
    if j==k:
      count +=1
print(count)

num = int(input())
roll_numbers = set(map(int,input().split(" ")))

french_stu = int(input())
french_stu_r_n = set(map(int,input().split(" ")))

print(len(roll_numbers.union(french_stu_r_n)))
