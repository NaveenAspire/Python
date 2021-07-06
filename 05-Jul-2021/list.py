a = [1,2,3,4,5,6]
print(a)
a.append(7)
print('After Append :',a)

a=[1,2,3,4,5,5,5]
print(a.count(5))
print(a.index(2))

# Second Index
val = int(input("Enter value for index : "))
index = []
for i in range (len(a)):
    if(a[i] == val):
        index.append(i)
print("Indexes are : ",index)

str = ["hai","hello","how"]
hai = str[:1]
hello = str[1:2]
how = str[2:3]
print(hai,hello,how)
print(str[:])
print(str.pop(1))
