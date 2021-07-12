def display(add):
    def call():
        avg = add()
        return avg
    return call

def average(getls):
    def get():
        ls = getls()
        n = len(ls)
        total = sum(ls)
        avg = total/n
        return avg
    return get

@display
@average
def getls():
    ls  =[1,2,3,4,5,6]
    n = len(ls)
    return ls

print(getls())