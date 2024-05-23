#!/usr/bin/python3
"""
Replace an element in a list at a specific position without
modifying the original list
"""
def new_in_list(my_list, idx, element):
    # Make a copy of the original list
    new_list = my_list[:]
    
    # Check if the index is within the valid range
    if 0 <= idx < len(my_list):
        # Replace the element at the specified index
        new_list[idx] = element
    
    # Return the new list
    return new_list
