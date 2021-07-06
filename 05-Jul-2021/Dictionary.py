student = {"name":"Ironman","Roll_NO":30,"Mark":90}
print(student)

del student["Mark"]
print(student)

student["Mark"] = 95
print(student)

print("Avoid Key Err : ",student.get("age"))


# user Input for Dictionary

n = int(input("Enter number of values in dictionary : "))
user_dict = {}

for i in range(0,n):
    key = input("Enter the key : ")
    value = input("Enter value : ")
    user_dict[key]  = value

print(user_dict)

