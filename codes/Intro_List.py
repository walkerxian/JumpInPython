#****************列表是可变对象，可以存储多个数据*************

#创建
list1 = [11,22,33]
print(list1)

# 访问

print(list1[1])

#遍历
for i in list1:
    print(i)
    
#修改可变对象  list
list1[1] = 100
print(list1)


#为可变对象  添加元素
list1.append(44)
print(list1)

# 删除元素
list1.pop(2)
#list1.remove(33)
print(list1)

#列表合并
#list1.extend([4,5,6])
list1.append([4,5,6])
print(list1)

#列表压缩 Zipping
list1 = [1,2,3]
list2 = [4,5,6]
for x,y in zip(list1,list2):
    print(x,y)

# 需要并行遍历多个列表时候，zip()可以简化代码
list1 = ["Alice", "Bob", "Charlie"]
list2 = [25, 30, 22]

for name, age in zip(list1, list2):
    print(f"{name} is {age} years old.")





