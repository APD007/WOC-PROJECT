

def get_user_input(message, valid_choices=None):
    user_input = input(message)
    
    if valid_choices is not None:
        while user_input not in valid_choices:
            print(f"Invalid choice. Please enter one of {valid_choices}.")
            user_input = input(message)

    return user_input

def display_output(output):
    print(output)

def get_tuple_input(prompt):
    input_str = input(prompt)
    elements = ''.join(char for char in input_str if char.isdigit() or char == ',').split(',')
    try:
        return tuple(map(int, elements))
    except ValueError:
        raise ValueError("Invalid input format. Please enter a valid tuple of integers.")
    
def get_int_list_input(prompt):
    input_str = input(prompt)
    try:
        elements = [int(element.strip()) for element in input_str.replace('[', '').replace(']', '').split(',')]
        return elements
    except ValueError:
        raise ValueError("Invalid input format. Please enter a valid list of integers separated by commas.")

def get_dict_input(prompt):
    entry = input(prompt)
    try:
        mapping = eval(entry)
        if isinstance(mapping, dict):
            return mapping
        else:
            print("Invalid input. Please enter a valid mapping.")
            return {}
    except Exception as e:
        print(f"Error: {e}. Please enter a valid mapping.")
        return {}

import numpy as np

def get_matrix_input(size):
    try:
        size = int(size)
        if size <= 0:
            raise ValueError("Size must be a positive integer.")
        matrix = np.zeros((size, size), dtype=int)
        print(f"Enter the {size}x{size} matrix:")
        for i in range(size):
            for j in range(size):
                matrix[i, j] = int(input(f"Enter element at position ({i + 1}, {j + 1}): "))
        return matrix
    except ValueError as e:
        print(f"Error: {e}")
        return None
