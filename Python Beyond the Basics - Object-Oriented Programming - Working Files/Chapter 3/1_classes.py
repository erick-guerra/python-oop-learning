
class MyClass(object):
    var = 10

# this_obj is a MyClass instance or MyClass Object
this_obj = MyClass()
# created second instance to show different hex cod (memory address)
that_obj = MyClass()

print(this_obj)
print(that_obj)
print(this_obj.var) # Instance access variable from the class; 10
print(that_obj.var)

class Joe(object):
    def callme(self):
        print('Calling "Call me" method instance: ')

thisjoe = Joe()
thisjoe.callme()
