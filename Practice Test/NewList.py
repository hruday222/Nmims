#Q1
def unique(list1):
    new_list = []
    for i in list1:
        if list1.count(i) == 1:
            new_list.append(i)
    print(new_list[0])

list1 = [3,3,3,3,7,3,3]
unique(list1)

#Q2

def century(year):
    cent = (year - 1) // 100
    cent += 1

    return cent

print(century(2005))
print(century(1950))
print(century(1900))