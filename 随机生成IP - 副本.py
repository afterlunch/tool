import random
from re import A
from time import sleep
import scapy.all as scapy
n = int(0)
a = 50
b = int(a)
while n < b:
    n = n + 1
    print(n)
    m=random.randint(1,1)
    n=random.randint(119,119)
    x=random.randint(0,127)
    y=random.randint(0,255)
    randomIP=str(m)+'.'+str(n)+'.'+str(x)+'.'+str(y)
    print(str(randomIP))
    sleep(0.5)
