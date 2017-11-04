
print("helloWorld!")

print("{0:_^10} is a dog".format('hahaha'))

i = 5

number = 23


# if guess == number:
#     print("哈哈哈")
# elif guess > number:
#     print("项目名称")
# else:
#     print("qwqewqewqe")
#     pass

running = False

while running:
    guess = int(input('Enter an integer : '))
    if guess == number:
        print("good!")
        running = False
        break #跳出循环
    elif guess > number:
        print("big than number")
    else:
        print("small than number")
else:
    print("done")

print(list(range(1, 5)))

for i in range(-1, 5):
    print(i)

def say_hello():
    print("helloWorld")
    global number
    number = 72
    pass

say_hello()

def pay(message, times = 5):
    print(message * times)
    pass

pay("hello ")

def total(a, b = 5, c = 10):
    print("a is : {} , b is : {}, c is : {}".format(a, b, c))
    pass

total(9)
total(10, 11, 12)
total(c = 15, b = 13, a = 1)

def total1(a = 5, *numbers, **phonebook):
    '''随便玩玩.

    :param a: 玩玩
    :param numbers: 数组
    :param phonebook: 字典
    :return:
    '''
    print("a : {}".format(a))
    for number in numbers:
        print("number {}, index ".format(number))

    for key, word in phonebook.items():
        print("key : {}, word : {}".format(key, word))

    pass

total1(10, 1, 2, 3, 4, 5, l=1, m=2,n=3)
print(total1.__doc__)



































