# OBJECT-ORIENTED PROGRAMMING (OOP)

### BRIEF HISTORY

>Developed in the 1960's (Simula67, smalltalk)

> A paradigm for code organization and design.
    - Organize data into objects and functionality into methods
    - Defines object specification (data, methods) in classes

> Promote collaboration, conde extension and maintenance.

> The primary paradigm of software design worldwide.

>Procedural VS Object Paradigm

# Procedural Paradigm (NON-OOP)

```python

def increment():
    arg = arg + 1
    return arg

this = 0
this = increment(0)
this = increment(0)
print(this) #2
```

# Object Paradigm
```python

class myCustomInt(object):
    def __init__(self):
        self.val = 0
    def increment(self):
        self.val = self.val + 1
    def __repr(self):
        return str(self.val)

this = myCustomInt()
this.increment()
this.increment()
print(this) #2
```


# OOP: WHY?

> * ###OOP: Three Pillars
> + Encapsulation
> + Inheritance
> + Polymorphism

### OOP Python
>What is an object?<br>  
An object is a unit of data (having one or more attributes), of
a particular class or type, with associated functionality (methods)

