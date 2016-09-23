__author__ = 'MrHowe'
# -*- coding: utf-8 -*-

'''
进阶练习，函数相关2

2016-9-4 晚
'''
'''
1.lambda总结


'''
d = lambda  x:x+1

'''
#练习1：定义一个方法get_num(num),num参数是列表类型，判断列表里面的元素为数字类型。其他类型则报错，并返回一个偶数列表。（注：列表里面的元素偶数）



'''

def get_num(num):
	'''
	返回一个偶数列表
	:param num:
	:return:lst
	'''
	lst = []
	for i in num :
		if isinstance(i,int) or isinstance(i,float):
			if i == 0:
				continue
			m = i % 2
			if m==0:
				lst.append(i)
		else:
			return
	return lst

