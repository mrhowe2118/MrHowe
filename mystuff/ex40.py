__author__ = 'MrHowe'
class TheThing(object):
	def __int__(self):
		self.number=0
	def some_function(self):
		print("I got called.")
	def add_me_up(self,more):
		self.number =more+self.number
		return self.number
a=TheThing()
b=TheThing()

a.some_function()
b.some_function()

print(a.add_me_up(20))
print(b.add_me_up(30))

print(a.number)
print(b.number)
class TheMultiplier(object):
	def __int__(self,base):
		self.base=base
	def do_it(self,m):
		return  m*self.base
x=TheMultiplier(a.number)
print(x.do_it(b.number))
