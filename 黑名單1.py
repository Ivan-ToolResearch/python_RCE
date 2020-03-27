def check_secure(inp):
    block = [
            'exec',
            'open',
            'file',
            'execfile',
            'import',
            'eval',
            'input',
            'hacker'
            # 以上為黑名單字串
    ]
    for s in block:
        if s in inp:
            raise Exception("挨歐，'"+ s +"'是個非法字串喔！你想幹麻")

while True:
    try:
        inp = input('> ')
        check_secure(inp)
        ret = None
        exec("ret=" + inp)
        if ret != None:
            print(ret)
    except Exception as e:
        print (e)
        