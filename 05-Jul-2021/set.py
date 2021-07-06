setA = {"one","two","one","two","three","three"}
print(setA)

print("one" in setA)
print("four" in setA)

setB = {"one","two","one","two","four","four"}

print("letters in setA but not in setB : ",setA-setB)

print("letters in setA or setB or both : ",setA|setB)

print("letters in setA and setB : ",setA&setB)

print("letters in setA or setB : ",setA^setB)

