'''
author : Kennedy kolute
class  : Andela bootcamp 11
'''
def find_max_min (numbers):
# return only length when all numbers in the list are the same
    if min(numbers)== max(numbers):
        return [len(numbers)]
		# else return list with minimum number and maximum number 
    return [min(numbers),max(numbers)]