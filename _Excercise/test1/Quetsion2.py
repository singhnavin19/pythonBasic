inputStr=input("please enter string")
for i in inputStr:
    if i in 'aeiouuAEIOU':
        print('vowel',i)
    else:
        print('not vowel',i)