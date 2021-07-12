import os

f = open("sample.txt","w")
f.write("This file created as sample.txt")
f.close()

f=open("sample.txt","r")
print(f.read())

f = open("sample.txt","a")
f.write("  Contet from append -> Now the file sample.txt is has more content by append method")
f.close()

f=open("sample.txt","r")
print(f.read())

f = open("sample.txt","w")
f.write("contet changed ->Now the file sample.txt lost the contents because used w method to open up a exisiting file")
f.close()

f=open("sample.txt","r")
print(f.read())

#f = open("sample.txt","x")

print("\n Readline Used\n")

f = open("created.txt","r")
print(f.readline())
f.close()

print("\n For loop with Read Line\n")

f = open("created.txt","r")
for x in f :
    print(x)
f.close()

#deleting File



if os.path.exists("sample.txt"):
  os.remove("sample.txt")
  print("\n File deleted")
else:
  print("The file does not exist")




