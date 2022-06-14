# this is a comment
# numbers
a = 2
b = 4
c = a + b
print(4 % 2)
# should be 20
print(50 - 5*6)

# classic divistion return float
print(17 / 3)

# pow
print(2 ** 10)

# strings
s1 = 'this is a string'
s2 = "this is a string"
s3 = "I don't know" # using ' inside a string
s4 = 'this is a "quote"' # using " inside a string
print(f"{a} + {b} = {a + b}")
print("this is a \"string\"")
print('this is a \'string\'')
# string multiple lines
print("""this is a
    multiple line \"string\"
""")
# string concatenation
print("Hello " + "world!")
print("Hello " "World!")
print(  "multi\n"
        "line\n"
        "string\n")

# slicing
word = 'Python'
print(word[0] + " == 'P'")
print(word[0:2] + " == 'Py'")
print(word[-2:] + " == 'on'")
print(word[:3] + " == 'Pyt'")

alphabet = "abcdefghijklmnopqrstuvwxyz"
print(len(alphabet))

# string is inmutable
try:
    str = "text"
    str[0] = 'T' # raise a TypeError because Strings are inmutable
except TypeError:
    print("string is inmutable!")

# list
squares = [1, 4, 9, 16, 25]
print(squares)
print(squares + [36, 49, 64])

# list are mutable
cubes = [1, 8, 27, 65, 125]
cubes[3] = 64
print(cubes)

print('-' * 40)