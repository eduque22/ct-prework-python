###Question 1
##write a function to print "hello_USERNAME!"
##USERNAME is the input of the function

def hello_name(user_name):
    '''Displays a greeting to user.'''
    print('hello_' + user_name + '!')

hello_name('USERNAME')



print('\n')
###Question 2
##write a function, first_odds that prints the
##odd numbers from 1-100 and returns nothing

def first_odds():
    '''Prints odd numbers from 1-100 and 
    returns nothing.'''
    odds = list(range(1, 100, 2))
    print(odds)
    return None

print(first_odds())


print('\n')
###Question 3
##write a function that returns max number
##of a given list

def max_num_in_list(a_list):
    '''Function will print highest number 
    in a list.'''
    digits = a_list
    print(max(digits))

nums = [1, 34, 4, 3, 37, 20]
max_num_in_list(nums)



print('\n')
###Question 4
##write a function to return(boolean type) if the given
##year is a leap year. Leap year is divisible by 4,
##but not 100, unless it is also divisble by 400

def is_leap_year(a_year):
    '''Function will tell us if a given year is 
    a leap year.'''
    if a_year % 4 == 0 and a_year % 100 != 0:
        return True
    elif a_year % 400 == 0:
        return True
    else:
        return False

print(is_leap_year(2008))



print('\n')
###Question 5
##write a function to check if all numbers in list
##are consecutive. Return is boolean type

def is_consecutive(a_list):
    '''Will return True or False if a list of numbers 
    is consecutive.'''
    return sorted(a_list) == list(range(min(a_list), max(a_list) + 1))

a_list = [4, 5, 6, 7, 8]
print(is_consecutive(a_list))