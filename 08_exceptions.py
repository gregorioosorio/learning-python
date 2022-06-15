while True:
    try:
        n = int(input('Please enter a number: '))
        if n == 0:
            break
    except ValueError as e:
        print('That was not a valid number', e)

class A(Exception):
    pass

class B(A):
    pass

class C(B):
    pass

for cls in [A, B, C]:
    try:
        raise cls()
    except C:
        print('C')
    except B:
        print('B')
    except A:
        print('A')