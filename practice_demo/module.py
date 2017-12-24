#!bin/env/Python3
# -*- encoding: utf-8 -*-

# string
import string

s = 'I am a computer learner, and I love it very much'
print(s)
# 单词首字母大写
print(string.capwords(s))

values = {'var' : 'foo'}

t = string.Template("""
Variable        : $var
Escape          : $$
Variable in text: ${var}iable
""")

print('TEMPLATE:', t.substitute(values))

s = """
Variable        : %(var)s
Escape          : %%
Variable in text: %(var)siable
"""

print("INTERPOLATION:", s % values)

s = """
Variable        : {var}
Escape          : {{}}
Variable in text: {var}iable
"""

print('FORMAT:', s.format(**values))


