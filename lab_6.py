def task_1():
 print(" 1# Тот-кого-нельзя-называть")
 inp = input("Введите что нибудь - ").split()
 for i in range(len(inp)):
   inp[i] = int(inp[i])
 print(inp)
 min1 = min(inp);
 max1 = max(inp);
 print((min1/max1)*100)


def task_2():
 print(" 2# Уравнение Незнайки")
 str1 = input("Введите что нибудь - ")
 st = []
 for i in range(0,len(str1),2):
   if str1[i]=="x":
     coor = i;
   else:
     st.append(int(str1[i]))
 if str1[1] == "+":
   print(st[1]-st[0])
 elif str1[1]=="-" and coor == 2:
   print("-",end="")
   print(st[1]-st[0])
 elif str1[1]=="-" and coor == 0:
   print(st[1]+st[0])


def task_3():
 print(" 3# Нумерология Кнопочки")
 f1 = open("ratata.txt","r")
 text = f1.read().split("\n")
 tab = []; x = 0;
 for i in range(len(text)):
   tab.append(text[i].split())
 ints = []; f = 0;
 for i in range(1,13):
   ints.append(i)
 for i in range(len(ints)):
   for g in range(1,ints[i]+1):
     if ints[i] % g == 0:
       f+=1;
   if f % 2 == 1:
     print(tab[i][1])


def task_4():
 print(" 4# Шифрование Пилюлькина")
 inp = input("Введите что нибудь - ").split()
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
 print(" 5# Лекции Незнайки")
 n = [];
 words = []; 
 c = [0,0,0];
 s = 0;
 r = open("levak.txt","r")
 for i in range(int(r.readline())):
   n.append(r.readline())
 for i in range(int(r.readline())):
   words.append(r.readline())
 for i in range(len(n)):
   for j in range(len(words)):
     if len(n[i]) != len(words[j]):
       continue
     for k in range(len(n[i])):
       if n[i][k] != words[i][k]:
         s+=1;
     if s == 1:
       c[i]+=s
       s = 0;
     s = 0
 print(*c)


def task_6():
 print(" 6# Равнобедренные треугольники")
 n = int(input("Введите что нибудь - "))
 print("*")
 for i in range(0,n-2):
   print("*",end = '')
   print(" "*i, end = '')
   print("*")
 for i in range(n-2,-1,-1):
   print("*",end = '')
   print(" "*i, end = '')
   print("*")
 print("*")

