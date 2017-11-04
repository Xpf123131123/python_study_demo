import os
import time

source = ['D:\\MyDocuments']

target_dir = 'D:\\backup'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

today = target_dir + os.sep + time.strftime('%Y%m%d')

if not os.path.exists(today):
    os.mkdir(today)

now = time.strftime('%H%M%S')

print('print a command ->')
str = input()

if len(str) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + str.replace(' ', '_') + '_' + '.zip'

zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

print('Zip command:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')


while True:
    print("\n\n按任意键退出程序")
    num = int(input())
    if num:
        break
    pass


