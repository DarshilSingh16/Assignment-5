#Task 1 
students = {
    "Alice": 85,
    "Ayush": 78,
    "Pushkar": 92,
    "Piyush": 88
}

name = input("Enter the student's name: ")
if name in students:
    print("Marks of", name, "are:", students[name])
else:
    print("Student not found in the records.")

#Task 2
numbers = list(range(1, 11))


first_five = numbers[:5]

reversed_list = first_five[::-1]

print("Extracted list (first five elements):", first_five)
print("Reversed extracted list:", reversed_list)

