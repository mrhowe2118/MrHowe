__author__ = 'MrHowe'
def person(name, age, **kw):
	if 'city' in kw:
		kw['city']='Shanghai'
    print('name:', name, 'age:', age, 'other:', kw)


person('Bob', 35, city='Beijing')

def fun(a,b,*,c,*f):
	print(a,b,c,f)
