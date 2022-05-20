def Carry(n1, n2):
    count = 0
    carry = 0
    while n1!=0 or n2!=0:
        if (n1 % 10)+(n2 % 10) + carry > 9:
            carry = 1
            count += 1
        else:
            carry = 0
        n1 = n1/10
        n2 = n2/10
    return count

print(Carry(1111,3333))