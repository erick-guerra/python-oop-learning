class depth_A(object):
    def dothis(self):
        print("doing this in A class")

class depth_B(depth_A):
    pass

class depth_C(object):
    def dothis(self):
        print("Doing this in C class")

class depth_D(depth_B, depth_C):
    pass

d = depth_D()
print(depth_D.mro())

class diamond_A(object):
    def dothis(self):
        print("doing this in A class")

class diamond_B(diamond_A):
    pass

class diamond_C(diamond_A):
    def dothis(self):
        print("Doing this in C class")

class diamond_D(diamond_B, diamond_C):
    pass

d = diamond_D()
print(diamond_D.mro())
