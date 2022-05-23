def divisible_by_Left(number):
    new_list = []
    num = str(number)
    for i in range(0, len(num)):
        if len(num) == 1:
            return False
        elif int(num[i]) % int(num[i-1]) == 0:
            new_list.append("True")
        else:
            new_list.append("False")

    return new_list
        
print(divisible_by_Left(73312))