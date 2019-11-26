# должно получиться  https://pcoding.ru/txt/words.txt  #68747470733A2F2F70636F64696E672E72752F7478742F776F7264732E747874
def task_1():
 import urllib.request
 import uf8 as module

 link = ""
 inp = input()
 for i in range(0,(len(inp)-1),2):
	 link += chr(int(str(inp[i]+inp[i+1]), 16))
 print(link)

 link = urllib.request.urlopen(link)

 lines = []
 for line in link.readlines():
   lines.append(line.decode('windows-1251'))

 print(module.binSearch(lines, "ячейка\n"))


 f1 = open("n8.txt","r")
 sfr = f1.read()

 sfr = sfr.split('\n')

 tab = [[],[],[],[]]
 for i in range(len(sfr)):
   for k in range(0,len(sfr[i])-2,2):
     tab[i].append(sfr[i][k] + sfr[i][k+1])
# for i in range(len(tab)):
# 	print(*tab[i])
 for i in range(0,4):
	 for k in range(0,22):