def ProgCetakAngka(n):
    i = 0
    for i in range (n):
        if i % 3 == 2 and i % 5 == 4:
            print("Python UMS")
        elif i % 3 == 2:
            print("Python")
        elif i % 5 == 4:
            print("UMS")
        else:
            print(i + 1)
