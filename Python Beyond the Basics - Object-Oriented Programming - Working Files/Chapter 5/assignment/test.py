from main import ConfigDict

oc = ConfigDict('config_file.txt')
print(oc['A'])
print(oc['B'])

oc["this"] = "other"

print(oc)