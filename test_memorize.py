from memoize_cache3 import Memorize


@Memorize
def test_memorize_nested(x):
    print('invoked original nested test_memorize!')
    return x

test_memorize_nested(124)
