for i in range(1, 51):
    if i % 3== 0 and i % 5 == 0:
        print("Divisible by both")
    elif i % 3 == 0:
        print("Divisibl by three")
    elif i % 5== 0:
        print("Divisble by five")
    else:
        print(i)
