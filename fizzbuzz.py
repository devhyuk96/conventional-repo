# i -> print('hello') -> exc -> :wq + enter
for i in range(1,16+1):
    if i%3==0 and i%5==0:
        print('fizzbuzz')
    else:    
        if i%3==0:
            print('fizz')
        elif i%5==0:
            print('buzz')
        else:
            print(i)
