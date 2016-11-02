'''
author : Kennedy kolute
class  : Andela bootcamp 11
'''

def factorial(number):
    if number == 0:
        return 1
    else:
	# use recursion to generate the factorial
        return number * factorial( number -1)