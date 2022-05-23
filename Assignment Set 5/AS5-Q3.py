#lex_auth_01269441810970214471

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