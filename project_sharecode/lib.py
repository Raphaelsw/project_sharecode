def try_me():
    n = int(input("Enter trapezoid size "))
    for i in range(n):
        print(" "*(n-i) + "*"*i, end='')
        for j in range(i+n):
            print("*", end='')
        print('')

    if n < 0:
        print("Error! %d is not a positive number." % n)
