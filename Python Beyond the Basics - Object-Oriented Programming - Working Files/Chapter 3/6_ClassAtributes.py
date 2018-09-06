
class YouClass(object):
    classy = 10

    def set_val(self):
        self.insty = 100

dd = YouClass()

dd.set_val()
print(dd.classy)
# Setting class variable trhough instance!
dd.classy = "Look, Set new value to class"
print(dd.classy)
del dd.classy
print(dd.classy)
print(dd.insty)