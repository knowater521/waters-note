import os
import time

os.system("git pull")

# 空文件夹占位文件的处理
rootDir = os.getcwd()

for root, dirs, files in os.walk(rootDir):
    for file in files:
        if file == 'gitkeep':
            if len(dirs) != 0:
                os.remove(root + '\gitkeep')
                print('路径' + root + '\gitkeep 删除占位文件')
            if len(dirs) == 0 and len(files) > 1:
                os.remove(root + '\gitkeep')
                print('路径' + root + '\gitkeep 删除占位文件')
    
for root, dirs, files in os.walk(rootDir):
    result = '.git' in root
    if len(dirs) == 0 and len(files) == 0 and not result:
        gitkeep = open(root + '\gitkeep', 'w', encoding='UTF-8')
        gitkeep.close()
        print('路径' + root + '\gitkeep 添加占位文件')

# git操作处理
os.system("git status")
os.system("git add .")
os.system("git status")
os.system("git commit -m '" + time.strftime("%Y%m%d-%H%M%S") + "'")
os.system("git push -u origin master")
