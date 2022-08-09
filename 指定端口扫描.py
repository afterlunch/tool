import socket
import datetime
import re
from concurrent.futures import ThreadPoolExecutor, wait
from tkinter import N
DEBUG = False
ip = input("ip:")
b = input("port:")
port = int(b)
def main():
    s = socket.socket()
    s.settimeout(0.9)
    s.connect(ip, port)
    openstr = f'[+] {ip} port:{port} open'
    print(openstr)   
if __name__ == '__main__':
  main()