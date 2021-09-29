from writerFunc import DelimFile, LogFile

d = DelimFile("test.csv", ",")
l = LogFile('file.txt')

d.write(['3', '5', 'this line'])
l.write("Log this one")
l.write("Log this twice")
l.write("Log this thrice")