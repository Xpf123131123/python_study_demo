repeat_inside=lambda s,r=range(50):max([s[i:j]*(k+2)for i in r
for j in r for k in r], key=lambda x:len(x)*bool(s.count(x)))



def repeat_inside(line):
    return max([m.group(0) for n in range(len(line)) for m in re.finditer(r'([a-z]+?)\1+', line[n:])], key=len, default="")
