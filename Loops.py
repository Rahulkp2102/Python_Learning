
# while loops works with 3 steps: initialization, condition, increment/decrement

# While Loop (nested) - Cube Pattern
i = 0
while i <5:
    print("#", end=' ')
    i +=1
    j = 0
    while j <5:
        print("#", end=' ')
        j +=1
    print()

i = 0
n = 5
# While Loop - Pyramid Pattern 
while i < 5:
    print(('#'*(2*i+1)).center(2*n-1))
    i += 1
    

# While Loops - Pyramid
i = 0
n = 5;
while i < 5:
    space = ' ' * (n - i - 1)
    print(space + '#' * (2 * i + 1))
    i += 1

## for loop

for i in range(0,100):
    n = i ** 0.5
    if n * n == i:
        print(i, 'is a perfect square')
    else:
        print(i, 'is not a perfect square')


## prime or not 

num = int(input("enter the number: "))

for i in range(2, num):
    if num % i == 0:
        print(num, "not prime")
        break
else:
    print(num, "is prime")


# ## prime number 

# is_prime = True
# num = int(input("Enter a number: "))

