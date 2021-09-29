import os

class ConfigDict(dict):

	def __init__(self, filename):
		self._file_name = filename
		if os.path.isfile(self._file_name):
			with open(self._file_name) as fh:
				for line in fh:
					key, value = line.rstrip().split("=")
					dict.__setitem__(self, key, value)

	def __setitem__(self, key, value):
		print("Set Item")
		dict.__setitem__(self, key, value)
		with open(self._file_name, "w") as fh:
			for key, val in self.items():
				fh.write('{0}={1}\n'.format(key, val))


	def __getitem__(self, item):
		print("Getting dictionary")
		return dict.__getitem__(self, item)


a = ConfigDict("config_file.txt")
a['Boom'] = 'BANG'

print(a)
# print(a.__dict__)
# a['E'] = '15'
# a['A'] = '57'
# a['B'] = '18'
# a['C'] = '96'
