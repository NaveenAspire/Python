add = lambda a,b : a+b

print(add(2,3))

# Work with Map

ls = [1,2,3,4,5,6,7,8,9,10]

ls1 = list(map(lambda x: x*2 ,ls))

print(ls1)

# Work with Filter

ls2 = list(filter(lambda n:(n%2==0),ls))
print("\nEven Position :")
print(ls2)

