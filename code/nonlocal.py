def parent():
    a = 5
    def child():
        nonlocal a
        a += 1
        print(a)
    child()
parent()