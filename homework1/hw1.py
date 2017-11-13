import pickle

class userInfo(object):

    def __init__(self, name, age, mobile, emial):
        self.name = name
        self.age = age
        self.mobile = mobile
        self.emial = emial

    def __doc__(self):
        """xpfxpf"""

    def description(self):
        print('name : {}, age : {}, mobile : {}, emial : {}'
              .format(self.name, self.age, self.mobile, self.emial))


# dict = {}

path = 'userInfo.plist'



def add_userInfo_to_pickle(user):
    try:
        f = open(path, 'rb')
        dict = pickle.load(f)
        print(dict)
    except EOFError:
        dict = {}
    finally:
        dict[user.name] = user
        f1 = open(path, 'wb')
        pickle.dump(dict, f1)
        print(dict)

def search_userInfo_with_name(name):
    try:
        with open(path, 'rb') as f:
            dict = pickle.load(f)
            if not dict[name]:
                print('未查找到相关信息,请检查您的输入内容是否有误')
            else:
                print(dict[name].description())
    except EOFError:
        print('未查找到相关信息,请检查您的输入内容是否有误')
    finally:
        pass

l = [1, 2, 3]
l.append(l)
print(len(l))
print(l[3][3][3])

if __name__ == '__main__':
    user = userInfo('xpf', 20, 13333333333, 'xpf@xpf.com')
    add_userInfo_to_pickle(user)
    print('请输入您想要做的操作：')
    print('1.添加')
    print('2.查找')
    num = int(input('请输入您想要做的操作：'))
    if num == 1:
        name = input('请输入姓名:')
        age = input('请输入年龄:')
        mobile = input('请输入手机号:')
        emial = input('请输入emial:')
        user = userInfo(name, age, mobile, emial)
        add_userInfo_to_pickle(user)
    elif num == 2:
        name = input('请输入您想要查找的用户名：')
        search_userInfo_with_name(name)
