# Write a python function find_duplicates(), which accepts a list of numbers and returns another 
# list containing all the duplicate values in the input list and the order should be same as in 
# the input list. If there are no duplicate values, it should return an empty list.

def find_duplicates(list_of_numbers):
    new_lst = []
    for i in range(0, len(list_of_numbers)):
        for j in range(i + 1, len(list_of_numbers)):
            if list_of_numbers[j] == list_of_numbers[i]:
                new_lst.append(list_of_numbers[i])
    
    return list(set(new_lst))

list_of_numbers=[1,2,2,3,3,3,4,4,4,4]
list_of_duplicates=find_duplicates(list_of_numbers)
print(list_of_duplicates)

# def find_duplicates(list_of_numbers):
#     l=[]
#     for i in list_of_numbers:
#         x=list_of_numbers.count(i)
#         if x>=2:
#             l.append(i)
#             l=set(l)
#             l=list(l)
#     return l