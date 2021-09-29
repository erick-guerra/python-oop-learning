import datetime
import abc


'''
		Chapter 4 Assignment | PBB - OOP
	The purpose of the script is to create a logging utility
	which writes a single string into a .txt file or list in
	CSV format
'''

# Parent class initialized with filename.
class WriteFile(object):

	__metaclass__ = abc.ABCMeta
	# Abstract method 'contract'
	@abc.abstractmethod
	def write(self, text):
		return

	def __init__(self, filename):
		self.filename = filename

	# Handles file objet opening, writing, and closing.
	def write_lines(self, text):
		fh = open(self.filename, 'a')
		fh.write(text + '\n')
		fh.close()

# Child class used for CSV formatting of text
class DelimFile(WriteFile):
	def __init__(self, filename, delim):
		# Could have just used 'self.filename = filename' but used super
		# constructor for practice; good practice.
		#self.filename = filename
		super(DelimFile, self).__init__(filename)
		self.delim = delim

	def write(self, this_list):
		#joins items in a list and passed through 'write_lines'
		line = self.delim.join(this_list)
		self.write_lines(line)

class LogFile(WriteFile):
	def write(self, this_line):
		dt = datetime.datetime.now()
		date_str = dt.strftime("%D | %H:%M")
		self.write_lines("{date} | {text}".format(date=date_str, text=this_line))

