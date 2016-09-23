__author__ = 'MrHowe'
# -*- coding: utf-8 -*-

'''
进阶练习，函数相关1

2016-9-4
'''

'''
1、基本概念

define 定义

定义一个空函数
def func_name():
	pass
	return

EX:
def func_1():
	print(232323)
	#return None  #默认返回None，养成有显性返回的习惯
print(func_1())
结果：
232323
None
---------------------------------------
'''
'''
2、函数的参数和抽象的概念

参数分为可选参数和必须参数
抽象是设定可复用的代码块

需求一：任意两个数的求和
def add(num1, num2): #按照需求设定两个必须参数,可选参数可以设定默认值
	return num1+num2
print(add(1, 99))

需求二：任意多个数的求和
def add(*num):  #按照需求设定一个可选参数tuple，一个*，两个**就是字典dict
	print(type(num))
	d = 0
	for i in num :
		d+=i
	return d
print(r'add(1,2,5,6)=',add(1,2,5,6))

---------------------------------------------------------------------------
'''
'''
3.程序的健壮性

3.1你永远知道你的方法会返回什么
	-输入的误操作的过滤
	-参数的条件的识别
	-异常的判断
3.2返回你想要的结果
	-duanyan测试

#需求一：任意两个数的求和
def add(num1, num2): #按照需求设定两个必须参数,可选参数可以设定默认值
	if isinstance(num1,int) and isinstance(num2,int):
		return num1+num2
	else:
		return 'add（）函数输入参数错误，请输入两个整数'
print(add(1.3, 99))

assert add(1,3) == 3 #断言测试

----------------------------------------------------------------
'''
'''
4.函数命名方法

	下划线命名法  xia_hua_xian()
	驼峰命名法   xiaHuaXian()
'''
'''
5.函数使用心得

	a.别管多复杂，先直接把功能先实现
	b.把可复用的抽象成函数：命名规范，伪代码，参数默认值
	c.将函数写的更加健壮，让他可以跑很多地方
	d.完善的测试
		assert
		对函数返回进行一个值与类型的测试
		单元测试
'''
'''
#练习1：定义一个方法，该方法可以引入任意多的整形参数，结果返回其中的最大值和最小值

def IntMaxMin1(*num):
	#通过遍历参数过滤参数错误
	for i in num:
		if not isinstance(i, int):
			return '参数报错，请输入正整数'
	#通过内置函数输出最大值最小值,也可以用a=list(num).sort()
	return max(num),min(num)
print(IntMaxMin1(44,55,22,'ss'))
'''
'''
#练习2：定义一个方法，该方法可以引入任意多的字符串，结果返回其中的长度最长的字符串

def LongStr(*str):
	#通过遍历参数过滤参数错误
	for i in str:
		if not isinstance(i, str):
			return '参数报错，请全部输入字符串'
	#定义一个变量用来存放最大长度
	long=0
	#考虑到可能会有多个字符串长度都是最大，先得出最大字符串的长度再去元组中匹配
	#也可以用a= sorted(str, key=lambda k:len(k)),通过安装字符串长度进行元组排序的形式得到最大长度，但是只会有一个
	for i in str:
		if len(i)>long:
			long=len(i)
	strlong=[]
	for i in str:
		if len(i)==long:
			strlong.append(i)
	return strlong
print(LongStr('aaa','ss','ssdad','sdadd'))
'''
'''
#练习3:定义一个方法get_doc(module),module参数为该脚本中导入的或者定义的模块对象，该函数返回module的帮助文档

import urllib
def get_doc(module):
	return help(module)
print(get_doc(urllib))

def get_doc(module):
	return help(module)
print(get_doc(urllib))
'''
'''
#练习4：定义一个方法get_text(f),f参数为任意一个文件的磁盘路径，该函数返回f文件的内容

import os
def get_text ( f ):
	# os.path.exists(f)判断文件是否存在
	# os.path.isflie(f)判断路径是文件还是文件夹
	if os.path.exists(f):
		text=open(f,'r') #打开文件
		text_r=text.read()
		text.close() #记得关闭文件，节省内存
		return text_r
	else:
		return '你输入的路径不存在，请重新输入'
print(get_text('stest.txt')) #注意相对路径和绝对路径，以及linux和windows的路径写法的差异
'''
'''
#练习5：定义一个方法get_dir(folder),folder参数为任意文件夹，该函数返回folder文件夹的文件列表。

import glob #这是查找符合特定规则的文件路径名
def get_dir(folder):
	return glob.glob(folder+'*') #参数为特定的相对路径或者绝对路径

print(get_dir(''))
'''
