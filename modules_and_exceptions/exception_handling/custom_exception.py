def own_exception(a):
    if a == 4:
        raise Exception("This is my own Exception")
    else:
        print("Input is ok")
try:
    own_exception(5)
    own_exception(4)
except Exception as e:
    print(e)