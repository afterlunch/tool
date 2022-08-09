import os
import pytesseract
# 文字图片的路径
path =  os.path
# 获取图片路径列表
imgs = [path + i for i in os.listdir(path)]
# 打开文件
f = open('text.txt', 'w+', encoding='utf-8')
# 将各个图片的路径写入text.txt文件当中
for img in imgs:
    f.write(img + '\n')
# 关闭文件
f.close()
# 文字识别