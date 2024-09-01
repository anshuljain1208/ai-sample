def find_max(array):
    max_number = array[0]
    for number in array:
        if number > max_number:
            max_number = number
    return max_number