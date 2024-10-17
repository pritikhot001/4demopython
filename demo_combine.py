#combining two sorted listts
def combine_sortlist(l1,l2):
    return sorted(l1+l2)
list1 = [5,6,9,7,5]
list2 = [1,2,3,4,8]
comb_list =combine_sortlist(list1,list2)
print(comb_list)
