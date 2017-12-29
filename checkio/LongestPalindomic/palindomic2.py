def longest_palindromic(text):
    """ A palindrome is
    a sequence of characters
    which reads the same backward as forward,
    such as "madam" or "racecar".

    - "aaaa" even case "aa" == "aa" <- halves equality ? no the same element
    - "aba" odd case, without center|middle 'b' -> to even case "a" == "a"

    for "artrartrt":
    "ar" -> 'a' vs. 'r' <- min possible size|basic case
    "art" -> 'a' vs. 't'
        "rt" -> 'r' vs. 't'
    "artr" -> 'ar' vs. 'tr'
        "art" -> cache
        "rtr" -> 'r' vs. 'r' <- found, size:3,pos:1
            "rt" -> cache
            "tr" -> 't' vs. 'r'
    "artra" -> 'ar' vs. 'ra'
        "rtra" -> 'rt' vs. 'ra'
            "tra" -> 't' vs. 'a'
                "tr" -> cache
                "ra" -> 'r' vs. 'a'
            "rtr" -> cache
    "artrar" -> 'art' vs. 'rar'
        "rtra" -> cache
        "rtrar" -> 'rt' vs. 'ar'
            "trar" -> 'tr' vs. 'ar'
                "rar" -> 'r' vs. 'r' <- found, size:3,pos:3
                    "ra" -> cache
                    "ar" -> cache
                "tra" -> cache
            "rtra" -> cache
    ...
    stop condition ?
    last character checked ?
    """

    def is_Mirrored(
            text_Str: str,
            is_DeBug_Mode=1 == 0
    ) -> bool:
        """ helper method
        that actually checks a palindrome property

        for "rtrartr".size:7
        from 0 to 7 // 2:3 by 1
         r0 vs r7-1
         t1 vs t7-2
         r2 vs r7-3

        >>> is_Mirrored( "aaaa" )# doctest: -SKIP -ELLIPSIS +NORMALIZE_WHITESPACE
        True
        >>> is_Mirrored( "aba" )# doctest: -SKIP -ELLIPSIS +NORMALIZE_WHITESPACE
        True
        >>> is_Mirrored( "rtrartr" )# doctest: -SKIP -ELLIPSIS +NORMALIZE_WHITESPACE
        True
        >>> is_Mirrored( "rtrabtr" )# doctest: -SKIP -ELLIPSIS +NORMALIZE_WHITESPACE
        False
        """
        # for_All holds
        check_Result = True  # False
        subStr_Len = len(text_Str)
        assert subStr_Len > 1, "'text_Str' must have at least 2 characters !"
        half_Size = subStr_Len // 2
        left_Half = ""
        right_Half = ""
        # l_Char = ""
        # r_Char = ""
        #
        for i in range(0, half_Size, 1):
            #
            l_Char = text_Str[i]
            r_Char = text_Str[-(i + 1)]
            #
            left_Half += l_Char
            right_Half += r_Char
            #
            if l_Char != r_Char:
                #
                check_Result = False
                break  # for
        #
        if check_Result and is_DeBug_Mode:
            print(
                "for \"{}\" left_Half:'{}' is_Mirrored right_Half:'{}'".format(
                    text_Str, left_Half, right_Half))
        #
        return check_Result  # False

    #
    # is_Mirrored( "rtrabtr" )
    is_DeBug_Mode = 1 == 0
    # print( "text:{}".format( text ) )
    checked_Set = set()
    # ( size, start(ing) position )
    palindromes_List = [(0, 0)]
    #
    subStr_Accum = ""
    #
    for (char_i, char) in enumerate(text):
        #
        subStr_Accum += char
        if is_DeBug_Mode:
            print("char:'{}', subStr_Accum:'{}'".format(char, subStr_Accum))
        # @toDo: recursively check all subStr_Accum's substrings .
        # @toDo: must track somehow 'subStr' start position in initial 'text'
        if len(subStr_Accum) > 0:
            # initialization
            check_List = [(subStr_Accum, 0)]
            #
            while len(check_List) > 0:
                # FiFo or LiFo ?
                subStr_Stat = check_List.pop(-1)
                (subStr, start) = subStr_Stat
                subStr_Size = len(subStr)
                #
                if subStr_Size > 1 and subStr not in checked_Set:
                    # update
                    checked_Set.add(subStr)
                    if 1 == 0:
                        if subStr_Size % 2 == 0:
                            # even
                            left_Half = subStr[0:half_Size]
                            right_Half = subStr[half_Size:]
                        else:  # subStr_Size % 2 != 0
                            # odd
                            left_Half = subStr[0:half_Size]
                            right_Half = subStr[half_Size + 1:]
                    #
                    if is_Mirrored(text_Str=subStr):  # left_Half == right_Half:
                        palindromes_List.append((subStr_Size, start))
                    # update
                    if subStr_Size > 2:
                        # left head part
                        check_List.append((subStr[:-1], start))
                        # right tail part
                        check_List.append((subStr[1:], start + 1))
                    elif subStr_Size == 2:
                        palindromes_List.append((1, start))
                        palindromes_List.append((1, start + 1))
                elif subStr_Size == 1:
                    palindromes_List.append((subStr_Size, start))
    #
    palindromes_List.sort(key=lambda x: (-x[0], x[1]))
    longest_Stat = palindromes_List[0]
    (longest_Size, longest_Start) = longest_Stat
    if is_DeBug_Mode:
        print(
            "longest_Size:{}, longest_Start:{}".format(
                longest_Size, longest_Start))
    # s[i:j:k]    slice of s from i to j with step k
    longest = text[longest_Start:longest_Size + longest_Start]
    if is_DeBug_Mode:
        print(
            "for text:'{}' longest palindrome is '{}'".format(
                text, longest))
    #
    return longest  # text


#
if __name__ == '__main__':
    # The module `doctest` is not allowed on checkio.
    # import doctest
    #
    #
    # doctest.testmod(verbose = True)
    #
    assert longest_palindromic("1") == "1", "digit one"
    assert longest_palindromic("abc") == "a", "one 'A'"
    assert longest_palindromic("aaaa") == "aaaa", "The A"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"