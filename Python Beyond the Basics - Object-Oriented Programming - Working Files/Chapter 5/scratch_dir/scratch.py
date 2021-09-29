import os

class DictConfig(dict):

	def __init__(self, filename):
		self._file_name = filename
		if os.path.isfile(self._file_name):
			with open(self._file_name, 'a') as fh:
				fh.writelines("{key}={value}\n".format(key=key, value=value))




	def __setitem__(self, key, value):
		print("Set Item")
		dict.__setitem__(self, key, value)

	def __getitem__(self, item):
		print("Getting dictionary")
		with open('config_file.txt') as fh:
			for line in fh:
				line = line.split('=')
				self.dict[line[0]] = line[1]
		return dict.__getitem__(self, item)
	# def __getitem__(self, item):

a = DictConfig("config_text.txt")
print(a)
a['B'] = '3'
a['C'] = '1'
a['B']