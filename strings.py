s = "This is a \nstring"
print(s)
s = r"This is a \nstring"
print(s)
s = "This is a formated {} string".format(43)
print(s)
s = "This is a formatted %s string" % 42  # OLD WAY
print(s)
s = '''
 This is 
a multi line string'''
print(s)
s = '''\
This is 
a multi line string'''
print(s)

s = "string"
print(s[2])
print(s[2:4])

for i in s:
    print(i) 


