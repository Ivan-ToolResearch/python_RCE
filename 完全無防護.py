while True:
    try:
        print('請輸入：')
        inp = input()
        ret = None
        exec("ret=" + inp)
        if ret != None:
            print(ret)
    except Exception as e:
        print (e)