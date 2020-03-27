def make_secure():
    kill = __builtins__.__dict__.keys()
    kill.remove('open')
    kill.remove('print')
    for x in kill:
        del __builtins__.__dict__[x]
    


make_secure()


while True:
    try:
        inp = input('> ')
        ret = None
        exec("ret=" + inp)
        if ret != None:
            print(ret)
    except Exception as e:
        print (e)
