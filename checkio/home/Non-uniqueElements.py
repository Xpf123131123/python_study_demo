"""
你将得到一个含有整数（X）的非空列表。
在这个任务里，你应该返回在此列表中的非唯一元素的列表。
要做到这一点，你需要删除所有独特的元素（这是包含在一个给定的列表只有一次的元素）。
解决这个任务时，不能改变列表的顺序。
例如：[1，2，3，1，3] 1和3是非唯一元素，结果将是 [1, 3, 1, 3]。

输入: 一个含有整数的列表。

输出: 一个含有不唯一元素的整数列表。

如何使用： 这个任务将帮助您了解如何操作数组，这是解决更复杂的任务的基础。这个概念可以很容易地推广到真实世界的任务。例如你需要通过删除低频的元素（噪声）来使统计数据更清楚。

前提:
0 < |X| < 1000

"""

def checkio_my(data):
    #Your code here
    #It's main function. Don't remove this function
    #It's used for auto-testing and must return a result for check.

    list = data.copy()
    for index,element in enumerate(data):
        if data.count(element) == 1:
            list.remove(element)
    #replace this for solution
    return list

def checkio(data):
    return [x for x in data if data.count(x) > 1]

if __name__ == '__main__':
    assert isinstance(checkio([1]), list), "The result must be a list"
    assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
    assert checkio([1, 2, 3, 4, 5]) == [], "2nd example"
    assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"
    assert checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "4th example"