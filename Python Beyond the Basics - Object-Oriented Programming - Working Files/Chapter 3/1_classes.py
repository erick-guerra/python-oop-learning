
class MyClass(object):
    var = 10

this_obj = MyClass() # this_obj is a MyClass instance or MyClass Object
that_obj = MyClass() # created second instance to show different hex cod (memory address)

print(this_obj)
print(that_obj)
print(this_obj.var) # Instance access variable from the class; 10
print(that_obj.var)

class Joe(object):
    def callme(self):
        print('Calling "Call me" method instance: ')

thisjoe = Joe()
thisjoe.callme()
