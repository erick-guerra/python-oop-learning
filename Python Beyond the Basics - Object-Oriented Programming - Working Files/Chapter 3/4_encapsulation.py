class MyClass(object):
    def set_val(self, val):
        self.value = val

    def get_val(self):
        return self.value

class MyInterger(object):
    """ set_val method is verifying that the argument passed to it is an interger, if not then return nothing
    and does not set value, if value is interger, then it does set value(val)"""
    def set_val(self, val):
        try:
            val = int(val)
        except ValueError:
            return
        self.val = val

    def get_val(self):
        return self.val

    def increment_val(self):
        self.val = self.val + 1

a = MyClass()
b = MyClass()
i = MyInterger()

a.set_val(10)
b.set_val(100)
i.set_val(9)

print(a.get_val())
print(b.get_val())
print(i.get_val())
i.set_val("Hi!")
print(i.get_val())