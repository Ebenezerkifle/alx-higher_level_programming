#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx >= 0 or idx < len(my_list):
        temp = my_list[0 : idx]
        temp2 =  my_list[idx + 1:]
        my_list = temp + temp2
       # my_list.append(temp2)
    return my_list

my_list = [1, 2, 3, 2, 5]
idx = 3
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)