# len() 求长度
# dic = {'name':'bingbing','age':18,'tel':'18308572371'}
# print(len(dic))
# li = [1,2,3,4]
# print(len(li))
# st = 'hello'
# print(len(st))


# keys(): 返回字典里面的所有键名
# dic = {'name':'bingbing','age':18,'tel':'18308572371'}
# print(dic.keys())
# # 循环取出键名
# for i in dic.keys():   # 代表只取出键名
#     print(i)

# values(): 返回字典里面包含的所有值
dic = {'name':'bingbing','age':18,'tel':'18308572371'}
print(dic.values())
for i in dic.values():
    print(i)


# item():返回字典里面包含的所有键值对,并以字典的形式返回输出
dic = {'name':'bingbing','age':18,'tel':'18308572371'}
print(dic.items())
for i in dic.items():
    print(i)


# 字典应用场景
# 使用键值对，存储描述一个物体的相关信息

# 集合
# 格式： 集合名 = {元素1,元素2,元素3...}
# s1 = {1,2,3,4}
# s1 = {}   # 定义空字典
# s1 = set()   # 定义空集合
# 集合具有无序性
# s1 = {'a','b','c','d','e','f','g','h'}
# print(s1)   # 每次运行结果都不同
# # 无序性不能修改集合中的值
# # 集合具有唯一性，可以自动去重
# s2 = {1,2,3,4,5,4,3}
# print(s2)

# 集合的常见操作
# 添加元素
# add() 添加的是一个整体
# 因为集合的唯一性，所以如果添加的元素在原集合中已经存在，就不进行任何操作
# s3 = {1,2,3,4}
# print(s3)
# s3.add(5)   # 一次只能添加一个元素
# print(s3)

# update 把传入的元素拆分，一个个拿进集合中
# s4 = {6,7,8,9,10}
# s4.update([5,6,7])   # 添加元素必须是能被for循环取值的可迭代对象
# print(s4)

# 删除元素
# remove :选择删除的元素，如果集合中有就删除，没有就会报错
s2 = {1,2,3,4}
s2.remove(3)
print(s2)

# pop  对集合进行无序排列，然后将左边的第一个元素删除
# 默认删除根据hash表排序后的第一个元素
s2 = {1,2,3,4}
s2.pop()
print(s2)

# discard ：选择要删除的元素，没有不会进行任何操作
s2 = {1,2,3,4}
s2.discard(4)
print(s2)




# 交集和并集
# 交集
# & 符号表示
a = {1,2,3,4}
b = {3,4,5,6}
print(a & b)   # 如果每日有共同的交集，就会返回输出set()表示一个空集合

# 并集
# | 表示
a={1,2,3,4}
b = {3,4,5,6}
print(a|b)    # 重复的部分不会输出






































