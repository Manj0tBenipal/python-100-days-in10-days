def calculateFactorial(a):
    if(a==1):
        return 1;
    else:
        return a * calculateFactorial(a-1)

print(calculateFactorial(5))