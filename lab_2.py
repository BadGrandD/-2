def task_6():
  print("Задание №6")
  n = int(input("Введите высоту -  "))
  c=1
  k = n
  while c<=n*2:
    s = " "*k + "#"*c 
    print(s)
    c += 2
    k -= 1

def task_5():
  print("Задание №5")
  import math
  g = int(input("Введите в градусах - "))
  x = g * math.pi / 180; q = 0.001
  p = 1; f = 1; z = 1
  old = x**p / f; f = 1
  while True:
   p += 2; f *=p* (p-1);  z = -z
   new = old + z * x**p / f
   if abs(new - old) <= q:
     break
   old = new
   print(new)

def task_4():
  print("Задание №4")
  c = int(input("Введите число - "));
  i = 0;
  a = 2;
  f = 1;
  h = 0;

  for i in range(c):
   h += a/f;
   if(i%2 == 0):
     f+=2; 
   elif(i%2 == 1):
     a +=2
   if(i == c):
     break;
   print(h);

def task_3():
 print("Задание №3")
 b =""
 d=int(input("Введите число - "))
 while d>0:
   b+=str(d%2)
   d//=2
 print("Двоичное число - ",b[::-1]) 

def task_2():
 print("Задание №2")
 n = int(input("Введите число - ")) 
 x = 1
 y = 0
 while x <=n:
   x*= 2
   y+= 1
   if x==n:
      print("да")
   else:
      print("нет")

def task_1():
 print("Задание №1")
 n = int(input("Введите положительное целое число - "))
 g=0;
 while True:
   a = n%10
   g = g+a
   n = int(n/10)
   if(n==0):break
 print(g)


# №3
#or
# b =""
# d = int(input("Введите десятичное число - "))
# while d>0:
#  b+=str(d%2)
#  d//=2
# print(b[::-1]) 