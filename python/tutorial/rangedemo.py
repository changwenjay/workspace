#my_list = [1, 2, 3, 4, 5, 6, 7, 8]
my_list = []
for x in range(1, 9):
    my_list.append(x)

for x in my_list:
    if x == 3 or x == 7:
        continue
    print(x)

print(my_list)
print()

x = 5
while x >= 0:
    if x == 0:
        print('GO')
    else:
        print(x)

    x -= 1
print()

for n in range(1, 51):
    if n % 3 == 0 and n % 5 == 0:
        print('FizzBuzz')
    elif n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
        print('Buzz')
    else:
        print(n)

