a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
c = int(input("Введіть третє число: "))


operation = input("Введіть 'max', 'min', или 'average': ")
if operation == 'max':

    result = max(a, b, c)
    print("Максималье:", result)
elif operation == 'min':

    result = min(a, b, c)
    print("Минімальне количество:", result)
elif operation == 'average':

    result = (a + b + c) /3
    print("Среднє число дорівнює:", result)