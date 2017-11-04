import os
import time

# TODO: 需要进行压缩的原文件地址
# 需要备份的文件与目录将被指定在一个列表中
# 在这里要注意到我们必须在字符串中使用双引号用以括起其中包含空格的名字
source = ['D:\\MyDocuments']

# TODO: 压缩文件存储路径

# 根路径
target_dir = 'D:\\backup'

# 压缩路径不存在则创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

# 备份文件将打包压缩成zip文件
# 将当期日期作为主备份目录下的子目录名称
today = target_dir + os.sep + time.strftime('%Y%m%d')

# 将当前时间作为zip文件的文件名
now = time.strftime('%H%M%S')

# zip文件名称格式
# target = today + os.sep + now + '.zip'
# now = time.strftime('%H%M%S')

print('print a command ->')
str = input()

if len(str) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + str.replace(' ', '_') + '_' + '.zip'

# 如果子目录不存在则创建一个
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)

# TODO: zip命令拼接生成
zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

# TODO: 运行备份、打印信息
print('Zip command is:')
print(zip_command)
print('Running:')

if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print("Backup FAILED")

while True:
    print("\n\n按任意键退出程序")
    num = int(input())
    if num:
        break
    pass






