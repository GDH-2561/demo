# 字符串编码
# 本质上就是二进制数据与语言文字的一一对应关系
# Unicode：所有字符都是两个字节，
# 好处：字符与数字之间的转换速度更块
# 坏处：占用空间大
# UTF-8：精准，对不同字符用不同的长度表示
# 优点：节省空间
# 缺点：转换速度慢


#   字符串编码转换
# a = 'hello'
# print(a,type(a))       #str：字符串
# a1 = a.encode()      #编码
# print('编码后：',a1)
# print(type(a1))     #bytes,以字节为单位进行处理
# a2=a1.decode()     #解码
# print(a2)
# print(type(a2))


# st='这里是zzh练习的代码'
# st1=st.encode("UTF-8")
# print(st1,type(st1))
# st2=st1.decode("UTF-8")
# print(st2,type(st2))


# 字符串常见操作
# + 字符串拼接
print(10+10)   # 结果等于20，这里属于算术运算符
print("10"+"10")   # 结果等于1010，这里属于字符串拼接


# * 重复输出
print('好好学习天天向上\n'*10)


# 成员运算符
# 作用：检查字符串中是否包含某个字符串（既某个或多个字符串）
# in : 如果包含返回true，不包含返回false
# not in : 如果不包含返回true，包含返回false
name = "渣渣灰"
print("灰"in name)    # 结果返回true
print("辉"in name)    # 结果返回false
print("灰"not in name)    # 结果返回false
print("辉"not in name)    # 结果返回true


# 下标
# python中下标从零开始
# 作用：通过下标能快速找到对应数据
# 格式：字符串名[下标值]
name = 'zzh在练习代码'
print(name[0])
print(name[1])
print(name[5])
# 从右往左数，下标从—1开始
print(name[-1])
print(name[-2])

# 切片：指对操作对象截取其中一部分的操作
# 语法：[开始位置：结束位置：步长]
# 注意包前不包后：即从起始位置开始到结束位置的前一位结束（不包含结束位置本身）
w1 = 'abcdefgh'
print(w1[0:3])  #结果为abc
print(w1[3:])   #后面不写则截取后面全部
# 步长表示选取间隔，不写步长则默认是一，步长绝对值决定切取的间隔，正负号决定切取的方向
print(w1[0:7:2])
print(w1[-1:-5:-1])