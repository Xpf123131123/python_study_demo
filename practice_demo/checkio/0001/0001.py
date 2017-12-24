"""
{} [] () + - * / 0~9
判断由以上字符组成的数学公式是否符合标准

延伸：解析xml格式
"""
import re
checkio=c=lambda e,d=500:d and c(re.sub(r'[^][(){}]|\(\)|\{}|\[]','',e),d-1)or not e



# def checkio(exp):
#
#     left = '{[('
#     right = '}])'
#
#     left_list = [(i, index) for index, i in enumerate(exp) if i in left]
#     right_list = [(i, index) for index, i in enumerate(exp) if i in right]
#
#     if len(left_list) != len(right_list):
#         return False
#
#     for t in right_list:
#         p = t[0]
#         list = [i for i in left_list if i[1] < t[1]]
#         if left.find(list[-1][0]) != right.find(p):
#             return False
#         left_list.remove(list[-1])
#
#
#     return True







if __name__ == '__main__':
    assert checkio('{1-2}*(2*2)+[3/3]') == True, 'first'
    assert checkio('{(1+2})-(3)*{9*[4-5]}') == False, 'second'
    assert checkio('') == True, 'third'
    assert checkio('((5+3)*2+1)') == True, '4'
    assert checkio('{[(3+1)+2]+}') == True, '5'
    assert checkio('(3+{1-1)}') == False, '6'
    assert checkio('(({[(((1)-2)+3)-3]/3}-)') == False, '7'
    assert checkio('2+3') == True, '8'
    assert checkio('{((((((((9-8))))))))}+[888-[[9]]]') == True, '9'
    print('you win')



