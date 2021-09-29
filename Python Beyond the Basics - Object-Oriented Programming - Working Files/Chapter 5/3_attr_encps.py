# Example of breaking encapsulation
class MyClass(object):
	pass

x = MyClass()
print(x)

x.one = 1 # here's the break
x.two = 2 # and here
x.word = "String'o text!" # here 2

print(x.one)

class GetSet(object):
	def __init__(self, value):
		self.attrval = value

	@property
	def var(self):
		print("Getting a value")
		return self.attrval

	@var.setter
	def var(self, value):
		print("Setting a value")
		self.attrval = value

	@var.deleter
	def var(self):
		print("Deleting var attribute")
		self.attrval = None

me = GetSet(5)
print("The value after first init of inst is {}".format(me.var))
me.var = 1000
print("Value added, now is {}".format(me.var))
del me.var
print("Value removed, now is {}".format(me.var))
