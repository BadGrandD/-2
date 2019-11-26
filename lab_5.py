def task_1():
 print("Задание №1 - Свой Чужой ")
 n=int(input("Назовите сумму целых чисел - "))
 d=0
 if (n>0): 
   for i in range(1,n-1):
     d+=i
   print(d)
 else:
   for i in range(1,n-1,-1):
     d+=1
   print(d)

def task_2():
 print("Задание №2 - Дороги ")
 d=open("input.txt","r")
 text = d.read().split("\n");
 tab = []
 for i in range(len(text)):
   tab.append(text[i].split())
 tab[0]=0
 for row in range(1,len(text)):
   for col in range(0,len(text)-1):
     if(tab[row][col]=="1"):
       tab[0]+=1
 print(tab[0]//2)

def task_3():
 print("Задание №3 Прямоугольники ")
 c = int(input("Введите одно целое положительное число - "))
 f=0;
 for i in range(c+1,1,-1):
   if((c/i).is_integer()):
     f+=1
     print(c/i)
 print(f)


def task_4():
 print("Задание №4 - Результаты охоты ")
 inp = input().split()
 inp.append(0)
 str1=""; f = 1;
 for i in range(len(inp)-1):
   if inp[i]==inp[i+1]:
     f+=1
   else:
     str1 = str1 + str(f) + str(inp[i])
     f = 1
 print(str1)


def task_5():
 print("Задание №5 - Ход конём ")
 print ("Введите их коордиты")
 b1 = input()
 b2 = int(input())
 e1 = input()
 e2 = int(input())

 b1 = int(ord(b1))
 e1 = int(ord(e1))

 if((max(b1,e1)-min(b1,e1))+(max(b2,e2)-min(b2,e2)))==3:
   print("Yes")
 else:
   print("No")




def task_6():
 print("Задание №6 - Шамбала ")
 n = int(input("Введите сколько нада или не надо - "));
 n=(n*2)-1
 tab = [];
 for i in range(n):
   tab.append(["x"]*n)
 n-=1
 for i in range(n-1):
   row = col = i;
   if i%2==1:
     while row < n-i:
       tab[row][col]=" "
       row+=1
     while col < n-i:
       tab[row][col]=" "
       col+=1
     while row > i:
       tab[row][col]=" "
       row-=1
     while col > i:
       tab[row][col]=" "
       col-=1
 for i in range(len(tab)):
   print(*tab[i])
  
  



#3 
#    n = int(input("Введите одно целое положительное число - "))
#  f=0;
#  for i in range(n+1,1,-1):
#    if((n/i).is_integer()):
#      f+=1
#    print(n/i)
#  print(f)

#4
  # d=str(input("Какую дичь вы сегодня поймли - "))
#  n=str(input("Сколько дичи вы сегодня поймали - "))
#  l=""
#  f=0;
#  for i in range(len(d)-1):
#    for g in range(len(n)):
#      if(d[i]==n[g]):
#        f+=1
#        l+=d[i]
#  print(l)