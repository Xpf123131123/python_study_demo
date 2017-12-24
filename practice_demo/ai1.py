
import random
from time import sleep

count = 0
ai = 0
gsp = 0

def gogogo(p=0.5, limit=500, result=10):
    global ai, gsp, count, gsp
    # gsp = abs(result - ai)
    if ai == result or count == limit:
        print('p : ', p)
        return

    gsp = abs(result - ai)
    gress = random.random()
    if gress > p:
        ai += 1
    else:
        ai -= 1

    gsp1 = abs(result - ai)
    if gsp < gsp1:
        p -= 0.01
    else:
        p += 0.01
    count += 1
    print('count : {}, p : {}, ai : {}'.format(count, p, ai))
    sleep(0.1)
    gogogo(p)
    pass

gogogo()


