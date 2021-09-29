class Erick(object):
    greeting = 'Hello, Erick'

    def callme(self):
        print("Calling the 'call me' method with instance: ")
        print("This is the instance obj memory allocated: {} ".format(self))

this_erick = Erick()
print(this_erick)

this_erick.callme()

print(this_erick.greeting)