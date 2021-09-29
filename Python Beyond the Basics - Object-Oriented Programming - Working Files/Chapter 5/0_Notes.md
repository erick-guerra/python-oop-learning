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