class MaxSizeList(object):

    def __init__(self, max):
        self.max_size = max
        self.innerlist = []

    def push(self, obj):
        self.innerlist.append(obj)
        # Does the max/limit logic here, with out the wonky reverse reversal solution I implemented (duh!)
        if len(self.innerlist) > self.max_size:
            self.innerlist.pop(0)

    def get_list(self):
        return self.innerlist

#  My solution
# class MaxSizeList(object):
#
#     def __init__(self, limit):
#         try:
#             self.limit = int(limit)
#         except ValueError:
#             return
#         self.limit = int(limit)
#         self.myList = []
#
#     def push(self, word):
#         self.myList.append(word)
#
#     def get_list(self):
#         new_list = list(reversed(self.myList))[:self.limit]
#         new_list = list(reversed(new_list))
#         print(new_list)

a = MaxSizeList(2)
b = MaxSizeList(1)
a.push("hey")
a.push("hi")
a.push("let's")
a.push("go")
a.push("more")
a.push("data")
b.push("hey")
b.push("hi")
b.push("let's")
b.push("go")

print(a.get_list())
print(b.get_list())