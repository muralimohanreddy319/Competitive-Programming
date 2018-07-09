import random


def rand7():
    return random.randint(1, 7)


def rand5():

    # Implement rand5() using rand7()
    
    val = ((rand7()*7)%5)+1
    return val


print 'Rolling 5-sided die...'
print rand5()