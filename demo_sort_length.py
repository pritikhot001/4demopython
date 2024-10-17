#python sort list according to the length of the element
def sort_length(lst):
    return sorted(lst, key=len)
my_list = ["apple","banana","kiwi","mango","cherry","pinapple","fruit"]
sorted_lst = sort_length(my_list)
print(sorted_lst)
