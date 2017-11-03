
def test_var_args(f_arg, *argv):
    print "first normal arg:", f_arg
    for arg in argv:
        print "list arg", arg

test_var_args('yasoob','python','eggs','test')

