for n in range(2, 2001):
    eh_primo = True 
    for i in range(2, n):
        if n % i == 0:
            eh_primo = False 
            break

    if eh_primo:
        print(n)