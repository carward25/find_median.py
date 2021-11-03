#name: Cassidy Ward
#date: 11/3/2021
#description: this program takes as a parameter a list of numbers.
#The function should return the statistical median of those numbers, which will require it to sort the list

def find_median(lst):
    lst.sort()
    if(len(lst) %2 == 1):
        return lst[len(lst)//2]
    else:
        return (lst[len(lst) // 2-1] + lst[len(lst) // 2])/2

#Testing
print(find_median([4,2,5,1,3]))
print(find_median([2,5,1,3]))
