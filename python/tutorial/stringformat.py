#!/usr/bin/python3

# 3 way to concat string

item_one = 'Bike'
item_two = 'Cellure phone'

#1
birthday_phrase = f'1 My birthday gifs are {item_one} and {item_two}.'
print(birthday_phrase)

#1-2
birthday_phrase = f'1-2 My birthday gifs are {item_one}'\
                  f' and {item_two}.'
print(birthday_phrase)

#2
birthday_phrase = '2 My birthday gifs are {} and {}.'.format(item_one, item_two);
print(birthday_phrase)

#3
birthday_phrase = '3 My birthday gifs are {first} and {second}.'\
                .format(first=item_one, second=item_two);
print(birthday_phrase.upper())


