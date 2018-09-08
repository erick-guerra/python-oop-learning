import abc
import datetime

class WriteFile(object):

    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def write(self, text):
        return

    def __init__(self, filename):
        self.filename = filename

    def write_line(self, text):
        fh = open(self.filename, 'a')
        fh.write(text + '\n')
        fh.close()

class DelimFile(WriteFile):
    def __init__(self, filename, delim):
        super(DelimFile, self).__init__(filename)
        self.delim = delim

    def write(self, this_list):
        line = self.delim.join(this_list)
        self.write_line(line)

class LogFile(WriteFile):
    def write(self, this_line):
        dt = datetime.datetime.now()
        date_str = dt.strftime("%Y-%m-%d %H:%M")
        self.write_line("{date} | {line}".format(date=date_str, line=this_line))

# x = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
# print(x)