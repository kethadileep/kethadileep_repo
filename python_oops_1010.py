
# decorator

def smart_devide2(func):
    def nested(c,d):
        print('nested 2')
        result = func(c,d)
        print('nested 2')
        return result
    return nested

def smart_devide1(func):
    def nested(a,b):
        print('nested 1')
        result = func(a,b)
        print('nested 1')
        return result
    return nested

@smart_devide2
@smart_devide1
def devide(a,b):
    print (a/b)

devide(10,2)
