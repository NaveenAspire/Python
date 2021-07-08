import builtins
import InstanceMethod
import ClassMethod as cl
import StaticMethod

cl.ClassMeth.Emp("Class",3443)

StaticMethod.StaicMeth.Emp("Static",1221)

InstanceMethod.obj.Emp("Instance",2332)

print("Dir of ClassMethod")

print(dir(cl))

print("Dir of SaticMethod")

print(dir(StaticMethod))

print("Dir of InstanceMethod")

print(dir(StaticMethod))



print("Builtin Dir : ")
print(dir(builtins))
