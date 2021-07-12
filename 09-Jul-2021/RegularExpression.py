import re

stg = "The rain in Spain"

#Special Sequences

A = re.findall("\AThe", stg)
print(A)
if A:
  print("Sucess Match")
else:
  print("No match")

txt = " hai 1234"

d = re.findall("\d", txt)

print(d)

if d:
  print("Digits Found")
else:
  print("No match")


s = re.findall("\s", txt)

print(s)

if s:
  print("Sucess ")
else:
  print("No match")

S = re.findall("\S", txt)

print(S)

if S:
  print("Sucess ")
else:
  print("No match")







