# 深浅拷贝
# 赋值:会随着原变量一起变化
# li = [1,2,3,4]
# print(li)
# li2 = li
# print('li',li)
# print('li2',li2)
# # 给li列表新增元素
# li.append(5)
# print('li',li)
# print('li2',li2)
# 赋值，等同于完全共享资源，一个值的改变会完全被另一个值共享

# 浅拷贝  (数据半共享)
# 会创建新的对象，拷贝第一层的数据、嵌套层会指向原来的内存地址
# import copy  # 导入copy模块
# li = [1,2,3,[4,5,6]]  # 定义一个嵌套列表
# li2 = copy.copy(li)
# # print('li',li)
# # print('li2',li2)
# # 查看内存地址 id()
# print("li内存地址：",id(li))
# print("li2内存地址：",id(li2))   # 内存地址不一样说明不是同一个对象
# li.append(8)
# print('li',li)
# print('li2',li2)
# # 往嵌套列表添加元素
# print(li[3])
# li[3].append(7)
# print(li)
# 外层的内存地址不同，但是内层的内存地址相同
# 拷贝速度快，占用空间少，拷贝效率高


# 深拷贝  （数据完全不共享）
# 外层的对象和内部的元素都拷贝了一遍
# import copy
# li = [1,2,3,[4,5,6]]
# li2 = copy.deepcopy(li)  # 深拷贝
# # print('li',li,id(li))
# # print('li2',li2,id(li2))
# li.append(8)
# print(li)
# print(li2)
# # 在嵌套列表添加
# li[3].append(7)
# print(li)
# print(li2)
# 深拷贝数据变化只影响自己本身，跟原来的对象没有关联


# 可变类型
# 含义：变量对应的值可以修改，但是内存地址不会发生改变
# 常见的可变类型：list、dict、set
li = [1,2,3,4]
print('li的原内存地址：',id(li))
li.append(5)
print(li)
print('li的现内存地址',id(li))
dic = {'name':'bingbing','age':18}
print(dic,id(dic))
dic['name'] = 'susu'
print(dic,id(dic))

set = {1,2,3,4,5}
print(set,id(set))
set.remove(3)  # 删除元素
print(set,id(set))


# 不可变对象：变量对应的值不能被修改，如果修改的话会生成一个新的值从而分配新的内存空间
n = 10   # 整形
print(n,id(n))
n = 15
print(n,id(n))   # 内存地址发生改变

st = 'hello'
print(st,id(st))
st = 'bingbing'
print(st,id(st))
# 元组：
tua = (1,2,3)
print(tua,id(tua))
tua = ('a','b','c')
print(tua,id(tua))
# 注意：前面所说深浅拷贝只针对可变对象，不可变对象没有拷贝的说法
