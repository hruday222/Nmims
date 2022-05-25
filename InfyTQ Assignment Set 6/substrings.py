# A 10-substring of a number is a substring of its digits that sum up to 10.
# For example, the 10-substrings of the number 3523014 are:
# 3523014, 3523014, 3523014, 3523014

# Write a python function, find_ten_substring(num_str) which accepts a string and returns the list of 
# 10-substrings of that string.
# Handle the possible errors in the code written inside the function.

# Sample Input              Expected Output
#  '3523014'         ['5230', '23014', '523', '352']


def find_ten_substring(num_str):
    str1 = ""
    result_list = []
    sum = 0

    for n in range(0, len(num_str)):
        sum = 0
        str1 = ""
        for i in range(n, len(num_str)):
            sum = sum + int(num_str[i])
            str1 += str(num_str[i])
            if(sum == 10):
                result_list.append(str1)

    return result_list

num_str="3523014"
result_list=find_ten_substring(num_str)
print(result_list)