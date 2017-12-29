def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming {}...'.format(n))
        r = '200 0K'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing {}...'.format(n))
        r = c.send(n)
        print('[PRODUCER] Consumer return: {}'.format(r))
    c.close()

# c = consumer()
# produce(c)





# receive = yield value
# 1.向函数外抛出value
# 2.函数暂停执行，等待next()或send()恢复
# 3.赋值receive = MockGetValue(). 这个MockGetValue()是假想函数，用来接收send()发送进来的值
def countdown(n):
    print('Counting down from', n)
    while n >= 0:
        print('=================')
        s = yield n
        print('*****************')
        print('s : ', s)
        print('n : ', n)
        if s is not None:
            n = s
        else:
            n -= 1


c = countdown(5) # 5
print(c)
for x in c: # x = c.next()
    print('x : ', x)
    if x == 5:
        print('-----------------')
        c.send(3) # c.send()
        print('-----------------')
        c.send(2) # c.send()
        print('-----------------')

'''
c.next() == c.send(5)   n = 5
c.send(3)               n = 3
c.send(2)               n = 2

c.next() == c.send(None)n = 1

c.next() == c.send(None)n = 0

'''

'''
x :  5

s :  3
n :  5 

s :  2
n :  3 

s :  None
n :  2

x :  1

s :  None
n :  1

x :  0

s :  None
n :  0

'''
