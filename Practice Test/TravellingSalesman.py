def paths(n):
    fact = 1
    for i in range(1,n + 1):
        fact = fact * i

    return "No of paths taken = ", fact

print(paths(4))