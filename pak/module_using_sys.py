import sys

print('\n\n',dir())

print('The command line arguments are:')
for i in sys.argv:
    print(i)

print('\n\nThe PYTHONPATH is ', sys.path, '\n')

print('\n\n',dir(sys))

print('\n\n',dir())

