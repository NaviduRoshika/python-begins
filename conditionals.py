a, b = 1, 1
if a < b:
    print('this is true')
elif a == b:
    print('a equals b')
else:
    print('this is false')

# SWITCH

choices = dict(
    one='first',
    two='second',
    three='third'
)

v = 'one'
print(choices[v])  

v = 'seven'
print(choices.get(v, 'other'))

v = 'this is true' if a < b else 'this is false'
print(v)
