# decorator function


def fun_decorator(fun):
    def wrapper_fun(x):
        print('before fun ')
        fun(x)
        print('after the fun')
    return wrapper_fun


@fun_decorator
def foo(x):
    print('now i am in foo fun')
foo(20)    