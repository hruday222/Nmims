# Write a python function, check_anagram() which accepts two strings and returns True, if one 
# string is a special anagram of another string. Otherwise returns False.

# The two strings are considered to be a special anagram if they contain repeating characters 
# but none of the characters repeat at the same position. 
# The length of the strings should be the same.
# Note: Perform case insensitive comparison wherever applicable.

def check_anagram(data1,data2):
    count = 0
    data1 = data1.lower()
    data2 = data2.lower()
    if len(data1) != len(data2):
        return False
    else:
        for i in range(len(data1)):
            if (data1[i] in data2 and data2[i] in data1) and data1[i] != data2[i]:
                count += 1
        if count == len(data1):
            return True
        else:
            return False

print(check_anagram("Schoolmaster", "Theclassroom"))