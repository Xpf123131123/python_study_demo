def translate(p, c='bcdfghjklmnpqrstvwxz', v='aeiouy', s=__import__('re').sub):
    return s(r'([%s])..' % v, r'\1', s(r'([%s]).' % c, r'\1', p))