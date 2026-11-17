# # 列表
# # 基本格式：
# # 列表名 = [元素1，元素2，元素3....]
# # 所有元素放在中括号内，元素与元素之间用逗号隔开，元素之间的数据类型可以各不相同
# # 能够进行切片操作
# # 列表也是可迭代对象，可以for循环遍历取值
# li = [1,2,3,4]
# print(type(li))
# print(li[2])
# for i in li:
#     print(i)
#
#
# # 列表的常见操作
# # 添加元素
# # append()  extend()  insert()
# li1 = ['one','two','three']
# # li1.append('four')    #append整体添加
# # print((li1))
# # li1.extend('four')      # 分散添加，将另一个类型中的元素逐一添加
# # print(li1)
# li1.insert(3,'four')      # 在指定位置插入元素
# li1.insert(0,'five')      # 如果指定位置存在元素，原有元素会像后移动，如果不指定元素，就会报错
#
# # 修改元素
# # 直接通过下标就可以进行修改
# li2 = [1,2,3]
# li2[1] = 'a'
# print(li2)
#
# # 查找元素
# # in : 判断指定元素是否存在列表中，存在返回true，不存在返回false
# # not in ：与in相反
# li3 = ['a','b','c','d']
# print('b'in li3)
#
# while True:
# # 用户输入昵称，昵称重复不能使用
# # 定义一个列表，保存已经存在的昵称
#     name_list = ['bingbing','susu','ziyi']
#     name = input("请输入您的昵称：")
#     # 判断昵称是否已经存在
#     if name in name_list:
#         print(f"该昵称已经存在{name}")
#     else :
#         print(f'昵称{name}已成功注册')
#         name_list.append(name)
#         break


# 删除元素
# del
# li4 = ['a','b,','c,','d']
# del li4    # 删除列表
# del li4[2]   # 根据下标删除
# print(li4)

# pop: 删除指定下标的数据，python3版本默认删除最后一个元素
# li4 = ['a','b,','c,','d']
# li4.pop()    # 默认删除d
# li4.pop(2)   # 指定下标删除，超出范围报错
# print(li4)


# remove :根据元素的值进行删除
# li4 = ['a','b,','c,','d','b']
# li4.remove('f')    # 如果列表中没有这个元素时报错
# li4.remove('b')    # 如果有两个相同元素，默认删除第一个
# print(li4)


# 排序
# sort：将列表按指定顺序重新排列，默认从大到小
# li = [1,4,45,6,7,34]
# # li.sort()
# # reverse :倒序，将列表反过来,并不按照从大到小，而是顺序倒置，sort与reverse一起用能实现从大到小
# li.sort()
# li.reverse()
# print(li)


# 列表推导式
# 格式一；[表达式 for 变量 in 列表]    注意in后面不仅可以放列表还可以放range（）、可迭代对象
# li = [1,2,3,4,5,6,7]
# [print(i) for i in li]   # 前面的i是表达式
li = []
# for i in range(1,7):
#     li.append(i)
# print(li)
[li.append(i) for i in range(1,8)]
print(li)


# 格式二：[表达式 for 变量 in 列表 if 条件]
# 把奇数放到列表
li6 = []
[li6.append(i) for i in range(1,10) if i%2==1]
print(li6)


# 列表嵌套
li = [1,2,3[4,5,6]]    # [4,5,6]是里面的内存列表
print(li[3])   # 会输出456，代表下标3就是[456]这个列表
print(li[3][0])  #取出4