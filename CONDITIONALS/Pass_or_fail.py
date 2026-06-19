marks={}
a = float(input("Enter Your English Marks: "))
marks.update({"English":a})
a = float(input("Enter Your Maths Marks: "))
marks.update({"Maths":a})
a = float(input("Enter Your Physics Marks: "))
marks.update({"Physics":a})
print(marks)

#Check for total percentage
total_percentage = round((sum(marks.values()) / 300)*100, 2)
print(f"Total Percentage: {total_percentage}")

# Check for passing or failing
if(total_percentage >=40 and marks["English"]>=33 and marks["Maths"]>=33 and marks["Physics"]>=33):
    print("You passed!!")
else:
    print("You Failed!!")