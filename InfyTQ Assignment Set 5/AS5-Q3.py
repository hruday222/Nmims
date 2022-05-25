# Write a python function, check_double(number) which accepts a whole number and returns 
# True if it satisfies the given conditions.
# The number and its double should have exactly the same number of digits.

# Both the numbers should have the same digits ,but in different order.
# Otherwise it should return False.

# Example: If the number is 125874 and its double, 251748, contain exactly the same digits, but in a different order.

def check_double(number):
    double = 2 * number
    dou = str(double)
    n = str(number)
    count = 0
    if len(dou) == len(n):
        for i in dou:
            if i in n:
                count += 1
        if count == len(n):
            return True
        else: 
            return False
    else:
        return False

        

#Provide different values for number and test your program
a = 125874
print(check_double(a))