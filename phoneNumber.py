# coding:utf-8

import queue
import threading
import time
import random

q = queue.Queue()
f = open("AreaNum.txt")

class MyThread(threading.Thread):
	def __init__(self,arg):
		super(MyThread, self).__init__()#注意：一定要显式的调用父类的初始化函数。
		self.arg=arg
	def run(self):#定义每个线程要运行的函数
		name_tmp = threading.current_thread().name
		print (name_tmp + "+" + self.arg)




def getheaders():
	user_agent_list = [\
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",\
	"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0",\
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",\
	"Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50",\
	"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)",\
	"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)",\
	"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB7.0)",\
	"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",\
	"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",\
	"Mozilla/5.0 (Windows; U; Windows NT 6.1; ) AppleWebKit/534.12 (KHTML, like Gecko) Maxthon/3.0 Safari/534.12",\
	"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E)",\
	]
	UserAgent = random.choice(user_agent_list)
	# headers = ('User-Agent': UserAgent)
	# return headers
	return UserAgent

def getProxy():
	ip_list = [{"method":"http","ip":"127.0.0.1:1111"},{"method":"https","ip":"127.0.0.1:2222"},{"method":"http","ip":"127.0.0.1:3333"},{"method":"https","ip":"127.0.0.1:4444"}]
	get_ip = random.choice(ip_list)
	return get_ip["method"] + " " + get_ip["ip"] 


def main():
	for line in f:
		line_tmp = line.strip("\n")
		q.put(line_tmp)

	while not q.empty():
		try:
			t = MyThread(q.get())
			t.start()
			print(getProxy())
		except e:
			print (e)

if __name__ == '__main__':
	main()




# for i in range(5):
# 	q.put(i)
# while not q.empty():
# 	print q.get()
