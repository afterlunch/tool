import time
import pyautogui
from PIL import ImageGrab
import os
time.sleep(5)
print("\033[1;33;44m#################----3.0---#####################\033[0m")
print("\033[1;35m#本程序每0.5秒执行一次截图 并执行一次键盘下键按钮\033![")
print("\033[1;35m#可以尽快截出网页所有内容 \033[0m")
print("\033[1;35m#可将截图内容粘贴到OneNote 中，便于搜索使用\033[0m")
print("\033[1;33;44m################################################\033[0m")
#截屏
a = input('请输入截图左上横坐标')
b = input('请输入截图右上纵坐标')
c = input('请输入截图左下横坐标')
d = input('请输入截图右下纵坐标')
e = int(a)
f = int(b)
g = int(c)
h = int(d)
def Screenshot():
	nowtime = time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime(time.time()))
	print(nowtime)
	im = ImageGrab.grab((e,f,g,h))
	im.save(r'png\%s.png' %(nowtime))

myabsPath = os.path.abspath('.')
path = [x for x in os.listdir('.') if os.path.isdir(x)]
	# print(path)
if 'png' in path:
		#print('yes')
	pass
else:
	#print('no')
		#创建目录
	pngPath = os.path.join(myabsPath,'png')
	os.mkdir(pngPath)
def anjian():
    pyautogui.hotkey('down')
while True:    
	print("截图！")
	Screenshot()
	anjian()
	print("\n")
	time.sleep(0.5) 
