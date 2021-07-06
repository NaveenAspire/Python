def student():
    name = input("Enter Name : ")
    roll_no = input("Enter RollNo : ")
    mark = int(input("Enter Mark : "))
    print(name,"RollNo is ",roll_no+" and Mark is ",mark)

student()

def liked(item,*args,**key):
    """
    This is the doc string in function
    """

    print("Item : ",item)
    print("available :")

    for arg in args :
        print(arg)
    
    print()
    print("Items liked and unliked : ")
    for k in key :
        print(k," : ", key[k])

print(liked.__doc__)    

liked("fruits","Apple","Orange",liked = "Apple",Unliked = "Orange")

