def largest_histogram(data):

    def sequence(d,i, v):
        '''
        :param d: 初始累加元素
        :param i: 当前index
        :param v: 方向(-1, 1)
        :return:  sum
        '''
        if i >= 0 and i < len(data) and data[i] >= d:
            return d + sequence(d, i+v, v)
        else:
            return 0

    list = [sequence(d, i, 1) + sequence(d, i, -1) - d for i,d in enumerate(data)]

    return max(list)


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert largest_histogram([5]) == 5, "one is always the biggest"
    assert largest_histogram([5, 3]) == 6, "two are smallest X 2"
    assert largest_histogram([1, 1, 4, 1]) == 4, "vertical"
    assert largest_histogram([1, 1, 3, 1]) == 4, "horizontal"
    assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8, "complex"
    print("Done! Go check it!")