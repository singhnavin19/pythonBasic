inputNumber=int(input('please enter number'))
isPimerNumber=0
for i in range(2,inputNumber):
    if inputNumber%i==0 :
        isPimerNumber=1
        break
if isPimerNumber==1 or inputNumber<=1:
    print('Not prime number')
else:
    print('Prime Number')
    