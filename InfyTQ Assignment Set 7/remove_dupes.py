# Write a python function, remove_duplicates() which accepts a string and removes all 
# duplicate characters from the given string and return it.

def remove_duplicates(value):
    str1 = ""
    for i in value:
        if i not in str1:
            str1 = str1 + i
    return str1

print(remove_duplicates("222233435657uwqtqasda!"))