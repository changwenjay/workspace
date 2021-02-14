vehicle = {
        'model': 'cefiro',
        'make': 'nissan',
        'year': 2003,
        'mileage': 109545
        }
print(vehicle)
print(vehicle['year'])

vehicle_2 = vehicle.copy()
vehicle_2['tires'] = 4

vehicle['year'] = 2021
print(vehicle['year'])

vehicle['type'] = 'sedan'
print(vehicle)

# del vehicle['make']
vehicle.pop('make')
print(vehicle)
print()

for x, y in vehicle.items():
    print (x, y)
print()

for x, y in vehicle_2.items():
    print (x, y)

string = 'I am so happy to learn Python' \
        'which makes my wife happy' \
        'and interested in Python' \
        'Python Python Python'
print(string)

count = {}
for x in string.split():
    if x in count:
        count[x] += 1
    else:
        count[x] = 1
print(count)

count_2 = {}
for each in string.split(' '):
    count_2[each] = count_2.get(each, 0) + 1
print(count_2)

