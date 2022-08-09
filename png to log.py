# python批量更改指定后缀名
import os
import sys
#更改为指定的目录，自行修改
os.chdir('.')

# 列出当前目录下所有的文件
files = os.listdir('./')
print('files',files)

for fileName in files:
	portion = os.path.splitext(fileName)
	# 如果后缀是.jfif，自行修改
	if portion[1] == ".png":
		#把原文件后缀名改为 .jpg，自行修改
		newName = portion[0] + ".log" 
		os.rename(fileName, newName)