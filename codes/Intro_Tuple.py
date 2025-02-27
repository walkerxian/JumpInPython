# tuple是不可变对象，修改会生成新的字符串

#创建元组
tuple1 = ('Honda', 'Civic', 4, 2017)
print(tuple1)  # ('Honda', 'Civic', 4, 2017)

# 访问元素
print(tuple1[1])

# 遍历元组

for i in tuple1:
    print(i)

#元组是不可变对象，不能为其赋值
#tuple' object does not support item assignment
#tuple1[3] = 2018




