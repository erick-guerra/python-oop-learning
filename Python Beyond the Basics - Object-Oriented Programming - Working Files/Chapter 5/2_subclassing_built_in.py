# Inheriting from buil-in classes
class MyDict(dict):
	cnt = 0

	def __setitem__(self, key, value):
		print("setting key and value!")
		dict.__setitem__(self, key, value)


dd = MyDict()
dd[1] = "A"
dd[2] = "B"

for key in dd.keys():
	print("{key} = {value}".format(key=key, value=dd[key]))


class MyList(list):  # inherits from list

	def __getitem__(self, index):
		if index == 0: raise IndexError
		if index == 0: raise IndexError
		if index > 0: index = index - 1  # list read method behavior edit
		return list.__getitem__(self, index)

	def __setitem__(self, index, value):
		if index == 0: raise IndexError
		if index == 0: raise IndexError
		if index > 0: index = index - 1  # list writte methods behavior edit
		list.__setitem__(self, index, value)

# __init__() is inherited from built-in list class
x = MyList(['one', 'two', 'three', 'four'])
# __repr__() is inherited from built-in list class
print(x)

x.append('five')  # append is inherited from built-in list class
print(x[5])
