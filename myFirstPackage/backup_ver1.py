import os
import time

# TODO: 原文件路径
# 1.需要备份的文件与目录将被指定在一个列表中.
# 在这里要注意到我们必须在字符串中使用双引号，
# 用以括起其中包含空格的名称
# , 'D:\\Code'
source = ['D:\\MyDocuments']


# TODO: 目标文件根路径
# 2.备份文件必须存储在一个主备份目录中
# 要记得将这里的目录地址修改至你讲使用的路径
target_dir = 'D:\\backup'

# TODO: 目标文件路径
# 3.备份文件将打包压缩成zip文件.
# 4.zip压缩文件的文件名由当前日期与时间构成.
target = target_dir + os.sep + \
         time.strftime('%Y%m%d%H%M%S') + '.zip'

# TODO: 若无，则创建目标目录
# 如果目标目录还不存在，则进行创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir) # 创建目录

# TODO: 拼接生成cmd命令
# 5.我们使用zip命令将文件打包成zip格式
zip_conmand = 'zip -r {0} {1}'.format(target, ' '.join(source))

# TODO: 打印信息
# 运行备份
print('Zip command is:')
# TODO: 在控制台则直接会打印
print(zip_conmand)
print('Running:')
if os.system(zip_conmand) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')

