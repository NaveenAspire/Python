from functools import reduce

ls =["Apple","Orange","Ant","Mouse"]

map_ex = list(map(lambda n : n[0] == "A", ls))

print(map_ex)


filter_ex  = list(filter(lambda n : n[0] == "A", ls))

print(filter_ex)

numls = [1,2,3,4]


reduce_ex = reduce(lambda x,y :x+y , numls)

print(reduce_ex)