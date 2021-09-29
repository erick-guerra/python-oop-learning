# Implementing Python's Core Syntax

* Our Classes can respond to core syntax features.
  * Operators like **'+ , - , \* , /'**.
  * Operator like **'in'**
  * Built-in functions like **len()** and **str()**
  * Looping
  * Subscripts and slices
* Core syntact features translate to ***"magic"*** method calls

> **Syntactic sugar referce to a short-hand that resolves some other call inorder to make code morrre legible and quicked to express** 

| Syntax       	| Core Syntax resolution  	|
|--------------	|-------------------------	|
| 'abc' in var 	| var.\_\_contains\_\_('abc') 	|
| var == 'abc' 	| var.\_\_eq\_\_('abc')       	|
| var[1]       	| var.\_\_getitem\_\_(1)      	|
| var[1:3]     	| var.\_\_getslice\_\_(1, 3)  	|
| len(var)     	| var.\_\_len\_\_()           	|
| print(var)   	| var.\_\_repr\_\_()          	|


# Inheriting from built-ins
- Python lets our classes inherit from built-in classes
- An inheriting (child) class of a buil-in shares all the same attributes, including methods, of the built-in.
- We can take advantage of core built-in functionality, but customize selected operations
- Built-in behavior is familiar to all Python developers - this can make use of our inheriting class easy to learn.

---
# Attribute Encapsulation 
- Instance attributes can be changed anywhere, to any value, breaking encapsulation.
- Getter and Setter methods are encouraged encapsulation, but are clunkier
- User are expected to do the 'right thing'
- Trusing the user is Pythonic

# **@property**
> ***@property*** - is a decorator that designates an instance attributes as encapsulate-able through methods

* Getting, setting, and deleting methods can be defined, called automatically when a user accesses the attribute. 
* The names are linked to the attribute name- the methods including setter and deleter methods, must use it. 
* **@property** offerss sine control, but don't try to force the user into  certain behaviours - it's not Pythonic.
* **@property** should not encapsulate expensive operations, because attribute setting looks cheap.
*  **@property** controls attriobutes that are expected, but can't controll attributes that are unexpected.
*  **\_\_slots\_\_** can define allowable attributes
    *  Saves memory by defining attributes ahead of time
    *  Should not be used to limit attributes - un-Pythonic!
---
# Private Variables Names 


> **PEP8**  stands for *'Python Enhancement Proposal'* and it's a series of documents that are shared among the Python community to discuss proposed changes to the language. The standard for clean Python code. 

### Varbiable Naming: **PEP8**
* Module names: **all\_lower\_case**
* Class banes and exception names: **CamelCase**
* Globals and locals: **all\_lower\_case**
* Functions and methods: **all\_lower\_case**
* Constants: **ALL_CAPS**

### Varbiable Naming: **"Public"** *and* **"Private"**
* "Public" attributes or variables (intended to be used by the importer of this module or user of this class): **regular_lower_case**
* "Private" attributes or variables (internnal use by the module or class): 
&nbsp;**_single_leading_underscore**
* "Private" attributes that shouldn't be subclassed:
&nbsp; **__double_leading_underscore**
* "Magic" attributes *(Use them, doon't create them)*:
&nbsp; **\_\_double_underscore__**
&nbsp;
---

# *\_\_With\_\_* Context
* Some object need to 'clean up' when done
    * File object needs to close()
    * A network connection may need to close
    * A data-intensive operation may need to **del** the data
* \_\_with\_\_ provides a block that 'cleans up' when exited
* Can handle exceptions that occur within the block
* Can also execute code when entered

---
# New Style Classes
* Inherit from "object"
* Can be constructed with default attributes from "metaclass" constructors.
* Allow subclassing of built-ins
* Allow the use of "slots" to define instance attributes
* use the "C3" MRO (Method resolution order)
* Support "descriptors"
* Are the only style of class in Python3