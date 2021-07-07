class Exception1 :
    @staticmethod
    def built_in() :
        result = ""
        try:
            a = int(input("Enter a : "))
            if a<4:
                b=a/(3-a)
            print(b)
        except ZeroDivisionError :
            print("a is try to dived by zero")
            result = "Exception Hnadled"
        except NameError :
            print("You can not print the undefined variable")
            result = "Exception Hnadled"
        else : 
            result = "No Exception Handled"
        finally:
            print(result)


#obj.error()


#User Defined Exception

class UserInvalidErr(Exception):
    
    def __init__(self,msg) :
        self.msg  = msg

class NetworkErr(UserInvalidErr):
    def __init__(self, msg):
        self.msg = msg

class Create :
    @staticmethod
    def usererr():
        try:
            raise (UserInvalidErr("Not a Valid user"))
        except UserInvalidErr as ue :
            print(ue.msg)
    
    @staticmethod
    def net_err():
        try:
            raise (NetworkErr("Network error detected"))
        except NetworkErr as ne:
            print(ne.msg)

user = Create()

obj = Exception1()
