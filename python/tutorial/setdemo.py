set_color = {'red', 'green', 'blue', 'yellow', 'white'}
print(set_color)

print(len(set_color))

set_color.discard('green')
print(set_color)

set_color.update(['purple', 'pink'])
print(set_color)


set_num = {'one', 'two', 'three'}
print(set_num)
set_three = set_color.union(set_num)
print(set_three)

