print('read file old way:')
f = open('input.txt', mode='r', encoding='utf-8')
for line in f:
    print(line, end='')
f.close()
print('-'*40)

print('read file with "with":')
with  open('input.txt', mode='r', encoding='utf-8') as f:
    for line in f:
        print(line, end='')
