
class MyNum(object):
    def __init__(self, value):
        print("Calling __init__")
        try:
            value = int(value)
        except ValueError:
            value = 0
        self.val = value

    def increment(self):
        self.val = self.val + 1

dd = MyNum("hello")
dd.increment()
dd.increment()
print(dd.val)