def task_1():
 print("Задание №1")
 n=int(input("Введите число - "))
 if n%2==0:
   print("чёт")
 else:
   print("нечёт")   

def task_2():
 print("Задание №2")
 a=int(input("Введите чило a - "))
 b=int(input("Введите число b - "))
 if a%b == 0:
   print("Кратно")
 else:
   print("Некратно")

def task_3():
 print("Задание №3")
 a=int(input("Введите  а - "))
 b=int(input("Введите  b - "))
 c=int(input("Введите  с - "))
 if a>b>c:
   print(c)
 elif a<b<c:
   print(a)
 else:
   print(b)

def task_4():
 print("Задание №4")
 a=int(input("Введите сторону a - "))  
 b=int(input("Введите сторону b - "))
 c=int(input("Введите сторону с - ")) 
 if (a+b>=c)and(a+c>=b)and(c+b>=a):
   print("Это треугольник")
 else:
   print("Это не треугольник")    

def task_5():
 print("Задание №5")
 a=int(input("Введите радиус - "))
 print(2*a*3.14)
 print(3.14*a**2)  


def task_6():
 print("Задание №6")
 import math
 def getRoots(a,b,c):
   d=b**2-4*a*c
   if d>0:
     x1=(-b+d**.5)/(2*a)
     x2=(-b+math.sqrt(d))/(2*a)
     result=str(x1) + "/n"+str(x2)
   elif d == 0:
     x= -b/(2*a)
     result=str(x)
   else:
     result="нет корней"
     
 a=int(input("Введите a - "))
 b=int(input("Введите b - "))
 c=int(input("Введите с - "))
 print(getRoots(a,b,c))