# 1num => SyntaxError

num = 0.77
num2 = 888
name = 'Mike'
s = "Hello " + name
is_ok = True
num, num2 = num2, num
num = str(num)

print("Hello world", name+num, s[:], s[5:10], type(is_ok))
