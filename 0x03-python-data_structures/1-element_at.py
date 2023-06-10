#!/usr/bin/python3
def element_at(my_list, idx):
    le = len(my_list) - 1
    if (idx < 0) or (idx > le):
        return (None)
    return (my_list[idx])
