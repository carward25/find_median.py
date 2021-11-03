#name: Cassidy Ward
#date: 11/3/2021
#description: this program takes as a parameter a list of numbers.
#The function should return the statistical median of those numbers, which will require it to sort the list

def find_median(numbers):
    numbers.sort()
    if len(numbers) % 2 == 1:
        return numbers[len(numbers) // 2]
    else:
        return (numbers[len(numbers) // 2] + numbers[(len(numbers) - 1) // 2]) / 2

