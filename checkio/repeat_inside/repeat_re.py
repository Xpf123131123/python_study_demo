import re
def repeat_inside(text):
    x = [i for i,k in re.findall(r"((.{2,})\2+)",text) + re.findall(r"((.)\2+)",text)]
    return sorted(x ,key = len,reverse = True)[0] if x else ""