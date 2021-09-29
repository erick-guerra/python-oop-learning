# Recommended use of with; Handle opening and closing (clean-up) of files
with open("scratch_dir/with_context_file.txt") as fh:
	for line in fh:
		line = line.rstrip()
		print(line)

class MyClass(object):
	def __enter__(self):
		print("We have entered the 'with'.")
		return self

	def __exit__(self, type, value, traceback):
		print("We are leaving the 'with'.")
		print(f'Error type: {type}')
		print(f'Error Value: {value}')
		print(f'Error Traceback: {traceback}')

	def say_hi(self):
		print(f'Hi! instance {id(self)}')


with MyClass() as oj:
	oj.say_hi()
	5/0

print('After the with block')