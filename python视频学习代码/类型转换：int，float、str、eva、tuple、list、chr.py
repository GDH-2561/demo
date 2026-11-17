# 类型转换
# int() ；转换为一个整数，只能转换纯数组成的字符串
a = 1.23
print(int(a))
print(int(1.8))  # 输出也是整形
st = '1234'
print(int(st))
# print(int('bingbing'))    会报错
# 如果字符串中有数字和正负号(-+)以外的字符，就会报错。正负号也只能在前面不能在后面

# # 用户从控制台输入，判断年龄
# age = int(input('请输入你的年龄：'))
# if age >=18:
#     print("已成年")
# else:
#     print('未成年')

# float(): 转化为一个小数
print(float(11))
print(float('-11.456'))

# str():转换为字符串类型，在任何类型都可以转化成字符串型
a = 100
b = str(a)
print(type(b))
st = str(1.80)
print(st)    # 浮点型的转换为字符串会取出末位为0的小数部分

# # eval()：
# print(10+10)
# print('10'+'10')
# print(eval('10+10'))
# 还可以实现list、dict、tuple、str之间的转换
# str-->list
st1 = '[[1,2],[3,4],[5,6]]'
li = eval(st1)
print(type(li))

# str-->dict
st2="{'name':'bingbing','age':18}"
dic = eval(st2)
print(type(dic))

#eval()非常强大，但是不够安全，容易被恶意修改数据，不建议使用


# list()：将可迭代对象转换成列表
# 支持转换为list的类型：str、tuple、dict、set
# str-->list
print(list('abcdefg'))

# tuple-->list
print(list((1,2,3,4)))

# dict-->list
print(list({'name':'bingbing','age':18}))
# 字典转换成列表，会取键名作为列表的值

# set-->list
print(list({'a','b','c','d','e'}))






















