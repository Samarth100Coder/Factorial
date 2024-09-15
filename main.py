def fact(x):
    if x==1 or x==0:
        return 1
    else:
        return x*fact(x-1)

n=int(input('Enter a number: '))

if n<0:
    print('Factorial does not exist')
else:
    print('Factorial is',fact(n))