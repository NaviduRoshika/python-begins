# WHILE LOOP
a, b = 0, 1
while b < 50:
    print(b, end=' ')
    a, b = b, a + b

print()

# FOR
for ch in 'string':
    print(ch, end=' ')

print()
# FOR WITH INDEX
for index, ch in enumerate('string'):
    print(index, ch, end='\n')
else:
    print('ALl are printed')

