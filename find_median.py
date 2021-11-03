def find_median(lst):
    lst.sort()
    if(len(lst) %2 == 1):
        return lst[len(lst)//2]
    else:
        return (lst[len(lst) // 2-1] + lst[len(lst) // 2])/2

# Testing
print(find_median([4,2,5,1,3]))
print(find_median([2,5,1,3]))