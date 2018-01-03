def repeat_inside(
    line: str,
    is_DeBug_Mode: bool = 1 == 0
) -> str:
    """
    the first
    longest repeating substring
    of size > 1
    consisted of sequential equal blocks|parts
    of size > 0
    """
    from collections import namedtuple
    #
    #
    # your code here
    line_Size = len( line )
    longest_Repeat = ""
    longest_Size = 0
    min_Repeat_Size = 2
    if is_DeBug_Mode:
        print( "Input -> line({}):'{}'".format( line_Size, line ) )
    # early return
    if len( set( line ) ) == 1:
        # special case
        if is_DeBug_Mode:
            print(
                "early return -> longest_Repeat({}):'{}'".format( line_Size, line ) )
        #
        return line
    #
    Seq_Stat = namedtuple(
        "Seq_Stat",
        [
            #'start_i',
            #'end_i',
            'freq',
            'starts_List'
        ]
    )
    # iterate over possible repeat sizes
    for repeat_Size in range( line_Size - 1, 0, -1 ):
        #
        if is_DeBug_Mode:
            print( "repeat_Size:{}".format( repeat_Size ) )
        distinct_Map = dict()
        subStrings_Count = 0
        # iterate|slide over *adjacent* substrings
        for subString_Start_i in range(
            0,
            line_Size - repeat_Size + 1,
            1#repeat_Size
        ):
            #
            subString = line[subString_Start_i:subString_Start_i + repeat_Size]
            if is_DeBug_Mode:
                print(
                    "{}subString({}):'{}', subString_Start_i:{}".format(
                        "\t", len( subString ), subString, subString_Start_i ) )
            get_Str = distinct_Map.get( subString )
            #
            if get_Str is not None:
                # 'subString' in 'distinct_Map'
                # update current
                #
                # cases:
                #       f:1,f:2,f:3
                #       0*  1*2*  <- max
                #"rghtyjdfrtdfdf56r"
                # 0*  0*1*  0*1*2* <- max
                # 0*  1*2*  3*4*5*
                #"rg12rgrg34rgrgrg56r"
                ### @toDo: store all starts+ends of 'subString' in 'line'
                ### @toDo: then find longest continuous seq for each 'subString'
                ### using theirs respactful|corresponding stored 'starts+ends'
                if is_DeBug_Mode:
                    print(
                        "{}get_Str.freq:{}, get_Str.starts_List:{}".format(
                        #"{}get_Str.start_i:{}, get_Str.end_i:{}, get_Str.freq:{}".format(
                            "\t\t",
                            #get_Str.start_i,
                            #get_Str.end_i,
                            get_Str.freq,
                            get_Str.starts_List
                        )
                    )
                next_Repetitions = get_Str.freq + 1
                distinct_Map[ subString ] = Seq_Stat(
                    freq = next_Repetitions,
                    starts_List = get_Str.starts_List + [ subString_Start_i ]
                )
            else:# get_Str is None:
                # 'subString' is not in 'distinct_Map'
                # add new
                distinct_Map[ subString ] = Seq_Stat(
                    #start_i = subString_Start_i,
                    freq = 1,
                    #end_i = subString_Start_i + repeat_Size - 1
                    starts_List = [ subString_Start_i ]
                )
            #
            subStrings_Count += 1
        #
        distinct_Map_Size = len( distinct_Map )
        if is_DeBug_Mode:
            print(
                "subStrings_Count:{}, distinct_Map({}):{}".format(
                    subStrings_Count,
                    distinct_Map_Size, distinct_Map
                )
            )
        #
        if distinct_Map_Size < subStrings_Count:
            # indicates that some keys are repeated|occured more then once
            #
            # longest ?
            # but which one ?
            #subString = distinct_Set.pop()
            #subString = distinct_Map.popitem()[0]
            ### @toDo: find most frequent subString
            max_Frequency = 0
            most_Frequent_Str = 0
            #
            for (
                subString,
                (
                    #subString_Start_i,
                    #subString_End_i,
                    freq,
                    starts_List
                )
            ) in distinct_Map.items():
                #
                if freq > 1:
                    # 'subString' occures more then once
                    # analyse 'subString' starts indexes
                    # example:
                    # { 'df': Seq_Stat(freq=3, starts_List=[6, 10, 12]) }
                    ### @toDo: merge|concatenate continuous intervals
                    # for size:2 and ( start, end, repeat_Count )
                    # from [(6,7,1), (10,11,1), (12,13,1)]
                    # to   [(6,7,1), (10,13,2)]
                    ### @toDo: or simply track the max interval size
                    continue_From_i = -1
                    # span
                    interval_Size = repeat_Size#0
                    # it might be >= 2 * repeat_Size or 0 ?
                    max_Interval_Size = 0
                    #
                    for s_i in starts_List:
                        #
                        if is_DeBug_Mode:
                            print(
                                "continue_From_i:{}, interval_Size:{}, max_Interval_Size:{}, s_i:{}".format(
                                    continue_From_i,
                                    interval_Size,
                                    max_Interval_Size,
                                    s_i
                                )
                            )
                        if continue_From_i == s_i:
                            # continuation found
                            # update
                            interval_Size += repeat_Size
                            max_Interval_Size = max(
                                max_Interval_Size, interval_Size )
                        else:# continue_From_i != s_i
                            # gap found
                            max_Interval_Size = max(
                                max_Interval_Size, interval_Size )
                            # reset
                            interval_Size = repeat_Size
                        # update
                        continue_From_i = s_i + repeat_Size
                    #
                    # post check ?
                    if(
                        longest_Size < max_Interval_Size and
                        repeat_Size < max_Interval_Size
                    ):
                        #
                        interval_Str = subString * (
                            max_Interval_Size // repeat_Size )
                        if is_DeBug_Mode:
                            print(
                                "Update -> longest_Size:{}, longest_Repeat({}):'{}' vs. '{}'({})".format(
                                    longest_Size,
                                    len( longest_Repeat ),
                                    longest_Repeat,
                                    interval_Str,
                                    max_Interval_Size
                                )
                            )
                        longest_Size = max_Interval_Size
                        longest_Repeat = interval_Str
                else:#if freq == 1:
                    pass
        # post check ?
        if longest_Size > repeat_Size:
            #
            break # for
    #
    if is_DeBug_Mode:
        print(
            "Result -> longest_Repeat({}):'{}'".format(
                #len( longest_Repeat ),
                longest_Size,
                longest_Repeat
            )
        )
    #
    return longest_Repeat#line
#
if __name__ == '__main__':
    # These "asserts" using only for self-checking
    # and not necessary for auto-testing
    #                           0*  1*2*
    assert repeat_inside('aabbff') == 'aa', "Second -> != 'aa'"
    assert repeat_inside('rghtyjdfrtdfdf56r') == 'dfdf', "!= 'dfdf'"
    assert repeat_inside('aaaaa') == 'aaaaa', "First"
    assert repeat_inside('aababcc') == 'abab', "Third"
    assert repeat_inside('abc') == '', "Forth"
    assert repeat_inside('abcabcabab') == 'abcabc', "Fifth"
    #
    print('"Run" is good. How is "Check"?')