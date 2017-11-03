def func():
    print('func()')
    def func1():
        print('func1')
        def func2():
            print('func2')
        #func2()
    func1()

func()
