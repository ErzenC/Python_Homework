#Bonus 1 
# Create a decorator that logs function input and output.

def logger(func):
    def wrapper(a, b):
        print("Input:", a, b)
        result = func(a, b)
        print("Output:", result)
        return result
    return wrapper

@logger
def multiply(x, y):
    return x * y

multiply(4, 5)

#OUTPUT:
#Input: 4 5
#Output: 20


#BONUS 2 
#Implement a generator that yields numbers divisible by 4 up to N
def numbers_divisible_by_4(n):
    for i in range(1, n + 1):
        if i % 4 == 0:
            yield i

x = int(input("Shkruaj nje numer: "))
for num in numbers_divisible_by_4(x):
    print(num)

#BONUS 4:
#Use map() to convert numeric values into strings
numbers = [1, 2, 3, 4, 5]

result = list(map(str, numbers))

print(result)