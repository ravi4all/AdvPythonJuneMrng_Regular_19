Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Emp():
	id = 101
	name = "Ram"
	age = 45
	sal = 45000

	
>>> Emp()
<__main__.Emp object at 0x000001FBE5C18320>
>>> emp = Emp()
>>> emp
<__main__.Emp object at 0x000001FBE5C33898>
>>> emp.age
45
>>> emp.name
'Ram'
>>> emp.name = "Raman"
>>> emp.__dict__
{'name': 'Raman'}
>>> emp.dept = "IT"
>>> emp
<__main__.Emp object at 0x000001FBE5C33898>
>>> emp.__dict__
{'name': 'Raman', 'dept': 'IT'}
>>> class Emp():
	id = None
	name = None
	age = None
	sal = None

	
>>> emp_1 = Emp()
>>> emp_1id
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    emp_1id
NameError: name 'emp_1id' is not defined
>>> emp_1.id
>>> emp_1.id = 101
>>> emp_1.name = 'Ram'
>>> emp_1.age = 40
>>> emp_1.sal = 45000
>>> emp_1.__dict__
{'id': 101, 'name': 'Ram', 'age': 40, 'sal': 45000}
>>> type(12)
<class 'int'>
>>> isinstance(12,int)
True
>>> isinstance(emp_1, Emp)
True
>>> emp_2 = Emp()
>>> emp_2.id = 102
>>> emp_2.name = 'Shyam'
>>> emp_2.age = 29
>>> emp_2.sal = 35000
>>> emp_2.__dict__
{'id': 102, 'name': 'Shyam', 'age': 29, 'sal': 35000}
>>> emp_2.__dir__
<built-in method __dir__ of Emp object at 0x000001FBE5C87A90>
>>> emp_2.__dir__()
['id', 'name', 'age', 'sal', '__module__', '__dict__', '__weakref__', '__doc__', '__repr__', '__hash__', '__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__init__', '__new__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']
>>> 
