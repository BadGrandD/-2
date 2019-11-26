def task_1():
 n=int(input("Введите число - "))
 c="X"*n
 print(c)

def task_2():
 n=int(input("Введите число - "))
 c=1
 while c<=n:
   s = "X"*n
   print(s)
   c += 1

def task_3():
 n=int(input("Введите число - "))
 l=0
 for l in range(n):
   if l % 2 == 0:
     print("X"*n)
   else:
     print("-"*n)
 
def task_4():
 n=int(input("Введите число - "))
 for i in range(n):
   print(("X-"*n)[: -n])

def task_5():
 a=int(input("Введите число - "))
 n=0
 for n in range(a):
  print("-"*n+"X"+"-"*(a-n))

def task_6():
 a=int(input("Введите число - "))
 n=0
 for n in range(a):
  print("-"*(a-n)+"X"+"-"*n)

def task_7():
  n=int(input("Введите число - "))
  for i in range(n):
   if(i%2==0):
     r="X-"
   print((r*n)[:-n])
  else:
   r="-X"
   print((r*n)[:-n])

def task_8():
 n=int(input("Введите число - "))
 d=" "
 for i in range(n):
   d+=str(i+1)+""
   print(d)

def task_9():
  n=int(input("Введите число - "))
  k = 0;
  for i in range(n):
    for d in range(1,n+1):
      k+=1;
      print(k,end="\t")
    print()
 
# def task_10()