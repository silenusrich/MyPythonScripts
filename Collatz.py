def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2

    else:
        print(3*number + 1)
        return 3*number + 1


print('Enter number:')
i = int(input())
while collatz(i) != 1:
    i=collatz(i)

  
    
    
    
