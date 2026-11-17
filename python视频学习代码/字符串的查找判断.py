# 1.字符串常见操作
# 1.1查找
# find:检测某个子字符串是否包含在字符串中，如果在就返回这个字符串开始位置的下标，否则就返回—1
# find(子字符串，开始位置下标，结束位置下标)
# 注意开始位置和结束位置下标可以省略，表示在整个字符串中查找
# 遵循包前不包后规则
# name = 'zzh在练习代码'
# print(name.find('h'))   # h的下标为2，输出结果也为2
# print(name.find('zzh代码'))  # 查找不到所以返回-1
# print(name.find('在',2))    # 3
# print(name.find('在',5))    #从下标5开始查找不到所以返回-1

# 1.2 index()
# 作用与find一致
# 区别：find找不到返回-1、index找不到会报错
# 语法：index(子字符串，开始位置下标，结束位置下标)
# 遵循包前不包后规则
# name1 = ('我命由我不由天')
# print(name1.index('命'))   # 返回1
# print(name1.index('命',2))  # 报错，从下标2开始没有找到
# print(name1.index('命',1,3))   # 1

# 1.3 count():返回某个子字符串在整个字符串中出现的次数，没有就返回0
# 语法：count(子字符串，开始位置下标，结束位置下标)
# 注意开始位置和结束位置下标可以省略，表示在整个字符串中查找
# 遵循包前不包后规则
name2 = 'bingbing'
print(name2.count('b'))   # 2
print(name2.count('a'))   # 0
print(name2.count('b',1))  # 1
print(name2.count('b',1,3))  # 返回0，因为在1到3这个位置里面查找不到
print(name2.count('b',1,4))   #返回0，遵循包前不包后原则


# 2 判断
# 2.1 startswith()：判断是否以某个子字符串开头，是的话就返回True，不是返回false，如果设置了范围，它就在指定范围内查找
# 语法：startswith(子字符串，开始位置下标，结束位置下标)
st = 'sixstar'
print(st.startswith('s'))  # True
print(st.startswith('s',0,1))  # True
print(st.startswith('s',3,6))  # True
print(st.startswith('s',2,6))  # False
# 2.2 endswith(),与startswith()基本相同不赘述
# 2.3 isupper():检测字符串中所有的字符是否都为大写，是返回True，不是返回False
# 2.3 islower():检测字符串中所有的字符是否都为小写，是返回True，不是返回False

# 3 修改元素
# 3.1 replace()替换
# 语法 ：replace(旧内容，新内容，替换次数)
# 注意替换次数可以省略，默认全部替换
name3 = '好好学习天天向上'
print(name3.replace('天','时',1))  # 好好学习天时向上
print(name3.replace('天','时',))   # 好好学习时时向上


# 4 split():指定分隔符来切字符串
st1 = 'helllo，python'
print(st1.split('，'))   # 以列表形式返回['hello','python']
# 如果字符串中不包含分割内容，就不进行分割，会作为一个整体
print(st.split('a'))    # 不分割


# 5 capitalize():将第一个字符大写，其他都小写
st2 = 'aingaing'
print(st2.capitalize())

# 6 lower():大写字母全部转为小写
st3 = 'cINGcIng'
print(st3.lower())

# 7 upper():小写字母全部转换为大写与lower()同理
