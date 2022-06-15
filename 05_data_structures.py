# manual
numbers = []
for i in range(10):
    numbers.append(i+1)
print(numbers)

# list comprenhension
numbers2 = [i + 1 for i in range(10)]
print(numbers2)

print([(x, y) for x in [1,2,3] for y in [1,2,3] if x != y])

ret = []
for x in [1,2,3]:
    for y in [1,2,3]:
        if x != y:
            ret.append((x,y))

print(ret)