# -*- coding: utf-8 -*-
print("\n[EX-1-3]计算与运算")
print("***计算实例-今年是不是闰年***") #你好全世界~~~~~~~~~~
try: #一个容错识别
	year = int(input("请输入年份（如2008）: ")) #year为年份变量
except:
	print("请输入正确的年份")
	exit()

is_leap = False #是否闰年
if year%100 == 0 and year%400 ==0:#整百年能被400整除的是闰年
	is_leap=True
elif year%100 != 0 and year%4 ==0:# 非整百年能被4整除的为闰年
	is_leap=True
if is_leap:
	print("{0}年份是闰年".format(year))
else:
	print("{0}年份不是闰年".format(year))

print("\n加分练习-平方根!")
num = float(input('请输入一个数字： '))
num_sqrt = num ** 0.5
print(' %0.3f 的平方根为 %0.3f'%(num ,num_sqrt))
# 注释叔叔欢乐~~！！！
