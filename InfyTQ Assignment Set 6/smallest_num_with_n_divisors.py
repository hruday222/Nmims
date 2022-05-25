# Write a python function find_smallest_number() which accepts a number n and returns the 
# smallest number having n divisors.
# Handle the possible errors in the code written inside the function.

# Sample Input          Expected Output
#      16                     120

def find_divisors(num):
    count = 0
    for i in range(1, (num//2) + 1):
        if num % i == 0:
             count += 1
    return count + 1

def find_smallest_number(num):
    a = 0
    n = 0
    while a != num:
        a = find_divisors(n)
        n += 1
    return n - 1

num = 8
# print("The number of divisors :",num)
result=find_smallest_number(num)
print("The smallest number having", num ,"divisors is",result)

