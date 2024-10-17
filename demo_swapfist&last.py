#write a python program to swap the first and last  element of thw list using python

def swap(list):
    if len(list) > 1:
        list[0],list[-1] = list[-1],list[0]
        return list
my_list = [5,6,9,5,7,8]
swapped_list = swap(my_list)
print(swapped_list)
