item_list = {
        'book': 20,
        'pen': 4,
        'eraser': 2,
        'tape': 15
}

def find_input():
    money_input = 0
    while True:
        str_input = input('Enter your money: ').strip()
        if str_input.isdigit():
            money_input = int(str_input)
            return money_input
        else:
            print('Input digits please')
            continue

def find_items():
    shop_list = []
    while True:
        input_str = input('Enter the item you shop: ').strip()
        if input_str in item_list:
            shop_list.append(input_str)
            print('There is {} items in cart.'.format(len(shop_list)))
        else:
            print('The item entered is NOT in the shop')

        input_yn = input('Want to continue to shop? (y/n)').strip().lower()
        if input_yn == 'y':
            continue
        else:
            return shop_list

def calc_shopping_sum(input_items):
    sum_of_shopping = 0
    for x in input_items:
        sum_of_shopping += item_list.get(x, 0)
    return sum_of_shopping


input_money = find_input()
# print(input_money)

input_items = find_items()
# mprint(input_items)

sum_of_shopping = calc_shopping_sum(input_items)
# print(sum_of_shopping)

if sum_of_shopping <= input_money:
    print('You remain: {}'.format(input_money - sum_of_shopping))
else:
    print('Not affordable')






