# coding:utf-8

import queue
import threading
import time

q = queue.Queue()
f = open("AreaNum.txt")

class MyThread(threading.Thread):
	def __init__(self,arg):
		super(MyThread, self).__init__()#注意：一定要显式的调用父类的初始化函数。
		self.arg=arg
	def run(self):#定义每个线程要运行的函数
		name_tmp = threading.current_thread().name
		print (name_tmp + "+" + self.arg)



def main():
	for line in f:
		line_tmp = line.strip("\n")
		q.put(line_tmp)

	while not q.empty():
		try:
			t = MyThread(q.get())
			t.start()
		except e:
			print (e)

if __name__ == '__main__':
	main()




# for i in range(5):
# 	q.put(i)
# while not q.empty():
# 	print q.get()
