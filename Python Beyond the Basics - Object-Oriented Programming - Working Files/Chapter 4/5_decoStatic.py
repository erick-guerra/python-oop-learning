class InstanceCounter(object):
	count = 0

	def __init__(self, val):
		self.val = self.filterint(val) # Calling filterint() as gate check
		InstanceCounter.count += 1

	def set_val(self, newval):
		self.val = newval

	def get_val(self):
		return self.val

	# Static method works neither on Instance or class but simply just a utility type class that does something useful,
	# it belngs in with the class code but still, is neither an instance or class method
	@staticmethod
	def filterint(value):
		if not isinstance(value, int):
			return 0
		else:
			return value
	# Some methods are designed to use class data, and not use instance data, we have class methods. Its done for code
	# clarity and readability
	@classmethod
	def get_count(cls):
		return cls.count

a = InstanceCounter("boom")
b = InstanceCounter(55)
c = InstanceCounter("BAM")

for obj in (a, b, c):
    print("Val of object: {}".format(obj.get_val()))
    print("Count: {}".format(obj.get_count()))
# We can always use the class itself to call the class method
print("Class method being called here: {}".format(InstanceCounter.get_count()))