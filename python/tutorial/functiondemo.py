def remove_head_tail(my_list):
    my_list.pop(-1)
    my_list.pop(0)
    return my_list

my_list = [1, 2, 3, 4, 5]
print(my_list)

updated_list = remove_head_tail(my_list)
print(updated_list)

def function_test(*arg):
    print(arg)

function_test(1, 2, 3)
function_test([1, 2, 3])

