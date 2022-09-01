import math
# 1num => SyntaxError

num = 0.77
num2 = 888
name = 'Mike'
s = "Hello " + name
is_ok = True
num, num2 = num2, num
num = str(num)

print("Hello world", name+num, s[:], s[5:10], type(is_ok))
print('1', '2', '3', sep='\n')
print("Hello world", name+num, s[:], s[5:10], type(is_ok), sep=', ')
# print(help(math))
print(math.log2(10))
print('C:\nam\name')
print(r'C:\name\name')
print("########")
print("""
Hello
world
""")
print("########")
print("########")
print("""\
Hello
world\
""")
print("########")
print("Hello world " * 3)
s1 = ('abcdefg'
     'hijklmn')
s2 = 'abcdefg'\
     'hijklmn'
print("s1 = "+s1[-7], "s2 = "+s2[-6], sep=',')
print(s1[2:8])
idx = 3
print(len(s2[:idx]))
s = 'Hi my name is hiroaki. I was born in Yokohama. I\'m living in Yokohama.'
print(s.startswith('Hi'), s.find('in'), s.rfind('Yokohama'), s.count('Yokohama'), sep=',')
print(s.capitalize(), '\n', s.title())
print('a is {}'.format('a'))
print('a is {2} {1} {0}'.format(1, 2, 3))
s = 'I\'m {1} {0}. {1} is first name.'
print(s.format('Makino', 'Hiroaki'))
