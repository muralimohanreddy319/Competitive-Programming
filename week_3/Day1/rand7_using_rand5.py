import random


def rand5():
    return random.randint(1, 5)


def rand7():

    # Implement rand7() using rand5()
    val = ((rand5()-1) * 5 + (rand5()-1) + 1)%7+1

    return val


print 'Rolling 7-sided die...'
print rand7()