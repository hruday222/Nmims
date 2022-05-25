# Write a python function, nearest_palindrome() which accepts a number and returns the nearest 
# palindrome greater than the given number. 

# Sample Input      Expected Output
#    12300               12321
#    12331               12421

# def nearest_palindrome(number):
#     n = ''
#     m = ' '
#     while n != m:
#         n = str(number)
#         m = n[::-1]
#         number += 1
#     return number - 1

def nearest_palindrome(number):
    number = number + 1
    n = str(number)
    while n != n[::-1]:
        number += 1
        n = str(number)
        
    return number
    
number=99
print(nearest_palindrome(number))