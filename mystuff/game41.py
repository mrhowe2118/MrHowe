__author__ = 'MrHowe'
class Animal(object):
	pass
class Dog(Animal):
	def __int__(self,name):
		self.name=name
class Cat(Animal):
	def __int__(self,name):
		self.name=name
class Person(object):
	def __int__(self,name):
		self.name=name
		self.pet=None
class Employee(Person):
	def __int__(self,name,salary):
		super(Employee,self).__int__(name)
		self.salary=salary
class Fish(object):
	pass
class Salmon(Fish):
	pass
class Halibut(Fish):
	pass
rover=Dog('Rover')
satan=Cat('Satan')
print(rover)
print(satan)
