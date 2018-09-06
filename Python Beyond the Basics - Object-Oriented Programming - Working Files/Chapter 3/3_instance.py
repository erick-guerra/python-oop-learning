import random

class MyClass(object):
    var = 10
    def dothis(self):
        self.rand_val = random.randint(1,10)

this_obj = MyClass()
that_obj = MyClass()

print("##"*20)
print("this_obj MyClass memmory allocation hex code: {}".format(this_obj))
print("that_obj MyClass memmory allocation hey code: {}".format(that_obj))
print("this_obj var from class: {}".format(this_obj.var))
print("that_obj var from class: {}".format(that_obj.var))
print("##"*20)
myinst = MyClass()
myinst.dothis()
print(myinst.rand_val)
print("")
print("")