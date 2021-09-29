# Old Style
class OldClass():
	pass

# New style inherit eventually from object
class NewClass(object):
	pass

oc = OldClass()
nc = NewClass()
print(type(nc))
print(type(oc))
# print(f'Type:\nOC instance is {oc}\nNC instance is {nc}')
# print(f'Type:\nOC instance is {oc.__class__}\nNC instance is {nc.__class__}')