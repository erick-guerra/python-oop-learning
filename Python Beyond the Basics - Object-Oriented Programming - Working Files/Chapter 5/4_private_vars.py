class GetSet(object):
	instance_count = 0
	__mangled_name = 'No privacy!'
	def __init__(self, value):
		self._attrval = value
		GetSet.instance_count += 1

	@property
	def var(self):
		print("Getting a value")
		return self._attrval

	@var.setter
	def var(self, value):
		print("Setting a value")
		self._attrval = value

	@var.deleter
	def var(self):
		print("Deleting var attribute")
		self._attrval = None

me = GetSet(5)
print("The value after first init of inst is {}".format(me.var))
me.var = 1000
print("Value added, now is {}".format(me.var))
del me.var
print("Value removed, now is {}".format(me.var))