# if statements
from multiprocessing.sharedctypes import Value


n = 2
if(n % 2 == 0):
    print(f"{n} is even!")
else:
    print(f"{n} is odd")

# for statement
for i in range(10):
    print(i, end=' ')
print()

# print first 10 odd numbers
for i in range(1,10*2,2):
    print(i, end=" ")
print()

# print the cube of even numbers only, and only less than 100
for i in range(200):
    if(i % 2 != 0):
        continue
    elif i >= 100:
        break
    print(i ** 3, end=' ')
print()

# function definition
def fibonacci(n):
    """Fibonacci function"""
    a,b = 0,1
    while a < n:
        print(a, end=' ')
        a,b = b, a+b

    print()

fibonacci(100)

# default values
def say_hello(name = 'world'):
    print('Hello ' + name + '!')

say_hello()
say_hello('Gregorio')

# return list
def fibonacci_list(n):
    """Returning a fibonacci list up to n"""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

print(fibonacci_list(100))

def ask_ok(prompt, retries=2, reminder="Please try again!"):
    while True:
        ok = input(prompt)
        if ok in ("yes", "y"):
            return True
        elif ok in("No", "n"):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError("invalid user response")
        print(reminder)

ask_ok("Do you want to exit? ")

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")