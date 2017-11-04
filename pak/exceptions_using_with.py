import sys
with open('poem.txt') as f:
    for line in f:
        print(line, end='')

print(sys.version_info)

