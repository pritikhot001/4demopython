
#interchange first and last element using temporay value
def swap(list):
    if len(list) > 1:
        temp = list[0]
        list[0] = list[-1]
        list[-1] = temp
        return list
my_list = [5,6,9,3,7,8]
swapped_list = swap(my_list)
print(swapped_list)
