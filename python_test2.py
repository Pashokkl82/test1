def f(iterator):
    i = 0
    while i < iterator:
        yield i**3
        i+= 1

if __name__ == '__main__':
    iterator = int(input("Введите вместимость итератора: "))
for i in f(iterator):
    print(i)