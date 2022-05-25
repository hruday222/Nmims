# The number, 197, is called a circular prime because all rotations of the digits: 
# 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# Write a python program to find and display the number of circular primes less than the given limit.

def check_prime(number):
    #if the number is prime return true, else return false
    if number == 2 or number == 1: 
        return True
    else:
        for i in range(2, number):
            if number % i == 0:
                return False
        else:
            return True

def rotations(num):
    #It should return the list of different combinations of digits of the given number.
	#Rotation should be done in clockwise direction. 
    #For example, if the given number is 197, the list returned should be [197, 971, 719]
    rotated_lst = []
    rotated_lst.append(num)
    temp = str(num)
    for i in range(1, len(temp)):
        temp = temp[1:] + temp[0]
        rotated_lst.append(int(temp))
    return rotated_lst

def get_circular_prime_count(limit):
    #It should return the count of circular prime numbers below the given limit.
    prime_count = 0
    for i in range(2, limit):
        a = rotations(i)
        count = 0
        for j in a:
            if check_prime(j) == True:
                count += 1
        if count == len(a):
            prime_count += 1
    
    return prime_count

#Provide different values for limit and test your program
print(get_circular_prime_count(100))