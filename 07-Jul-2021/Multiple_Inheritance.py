class Add:
    @staticmethod
    def add(a,b):
        c=a+b
        print(a+b)

class Sub:
    @staticmethod
    def sub(a,b):
        c=a-b
        print(c)

class Mul:
    @staticmethod
    def mul(a,b):
        c=a*b
        print(c)

class Div:
    @staticmethod
    def div(a,b):
        c=a/b
        print(c)


class Calculator(Add,Sub):
    @staticmethod
    def calci():
        keys = [1,2,3,4]
        operator = ["Addition","Subraction","Multiplication","Division"]

        operation = dict(zip(keys,operator))

        print(operation)

        action = int(input("Enter key that you want perform operation : "))

        a = int(input("Enter first value : ")) 
        b = int(input("Enter second value : ")) 
    
        if action == 1:
            Add.add(a,b)
        elif action == 2:
            Sub.sub(a,b)
        elif action == 3:
            Mul.mul(a,b)
        elif action == 4:
            Div.div(a,b)
        else :
            print("Enter the Valid Key to perform Operation")

cal = Calculator()
#cal.calci()

