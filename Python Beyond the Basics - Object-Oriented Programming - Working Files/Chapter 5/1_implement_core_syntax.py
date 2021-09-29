# Syntactic Sugar: A shorthand that python takes give an operator
var1 = "Hello"
var2 = " World!"
var3 = 1
var4 = 5
var5 = ['a', 'b']
var6 = ['c', 'd']
# When use the '+' sign like this (concatenation)...
ex1 = var1 + var2
ex2 = var3 + var4
ex3 = var5 + var6

print(ex1)
print(ex2)
print(ex3)
''' What python is actually doing is resolving to a method call.
  In this example, the add attribute is used on strings, ints, and list.
  Double underscore of an attribute is known as magic attribute'''

ex1_magic = var1.__add__(var2)
ex2_magic = var3.__add__(var4)
ex3_magic = var5.__add__(var6)

print(ex1_magic)
print(ex2_magic)
print(ex3_magic)

# We can edit the native behavior of built-in syntax, this example changes the '+'
# or __add__ behavior
class SumList(object):
	def __init__(self, this_list):
		self.mylist = this_list

	# Will go through the lists between two instances by index value,
	# add the numbers and return the new list.
	def __add__(self, other):
		new_list = [x + y for x, y in zip(self.mylist, other.mylist)]
		return SumList(new_list)

	#repr method is used to display the object as a string, default, it would
	#just return the object.
	def __repr__(self):
		return str(self.mylist)


aa = SumList([1, 5, 10, 20, 40])
bb = SumList([10, 50, 100, 300, 400])
cc = SumList(['Word ', 'Big ', 'Much '])
dd = SumList(['up', 'boss', 'wow'])

int_add = aa + bb
list_add = cc + dd
print(int_add)
print(list_add)