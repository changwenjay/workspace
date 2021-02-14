import random

length = 5
def myrand(randseed = 1, length = length):
    random.seed(randseed)
    for x in range(length):
        r = yield random.random()

r = myrand()
for x in r:
    print(x, end = ' ')
print()

s = myrand()
for i in range(length):
    print(next(s), end = ' ')
    # s.send('asc')
print()

def myrand2(randseed = 1, length = length):
    # random.seed(randseed)
    for x in range(length):
        r = yield random.randrange(0, 10)

t = myrand2()
for i in range(length):
    print(next(t), end = ' ')
print()

if __name__ == '__main__':
    random.seed(1)

    x = random.random()
    y = random.random()

    # print(x)
    # print(y)

