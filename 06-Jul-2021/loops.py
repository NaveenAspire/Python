sentence = ["hai","hello","how","are","you"]

word = "String Print By Loop"

print("lsit are print by for loop")

for n in sentence :
    print(n,end=" ")
print()
print()
print("String print by For loop")
for n in word :
    print(n,end=" ")
print()

print("-"*(4)+"While Loop"+"-"*(4))

i=0
while i < len(sentence):
    print(sentence[i])
    i+=1