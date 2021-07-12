class Methods:
    a = 10
    def mulIns(self,a,b):
        print("\nInstance Method")
        #print(self.a)
        a =self.a
        ans = a*b
        print(ans)

    @staticmethod
    def mulSta(c,b):
        print("\nStatic Method")
        Methods.a =10
        c= Methods.a
        ans  = c*b
        print(ans)

    @classmethod
    def mulCls(cls,a,b):
        print("\nClass Method :")
        a = Methods.a
        ans = a*b
        print(ans)



obj = Methods()

Methods.mulSta(11,2)



Methods.mulCls(12,2)

obj.mulIns(11,2)