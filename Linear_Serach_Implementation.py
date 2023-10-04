def linear_search (input_list, target):
    """This function is used to check if target number is in the input list."""
    variable_index = -1

    for iterate in input_list:
        if iterate == target:
            variable_index = iterate
            break

    return variable_index


my_list = [1, 3, 5, 7, 9, 11]
target = 19

result = linear_search(my_list, target)

if result != -1:
    print(f"The target element {target} is at index {result}.")
else:
    print(f"The target element {target} was not found in the list.")

help(linear_search)