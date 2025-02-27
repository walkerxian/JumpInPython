#字符串操作： 不可变对象，修改会生成新的字符串

#大小写转换
word = "Hello"
print(word.lower())
print(word.upper())
print(word)

#字符串拼接
print('1' + '2')
print('Hi' + ' there.')

#字符串重复
print("12" *3)

#去掉空格或者指定字符
s = ' Extras \n'
print(s.strip())

s = '*********10*****'
print(s.strip('*'))

# 字符串拆分
s = "Let's splt the words"
print(s.split(' '))
s = 'Jane,Doe,Cars,5'
print(s.split(','))

#字符串切片 相当于[)左闭区间，右开区间
word = "Hello"
print(word[1:3])

print('el' in word)
print(word.find('el'))

#格式化这个有点新意
statement = 'We love {} {}.'
print(statement.format('data','analysis'))





