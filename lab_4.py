print("Задание №1")
d = open('rt.txt') 
text = d.read() 
print(text) 
d.close()

print("Задание №2")
d = open('rt.txt',)
text = d.read() 
lines = text.split('\n')
d.close()
n=len(lines)
for i in range(n):
  if i%2==0:
    print(lines[i])

print("Задание №3")
d1=open('rt.txt',"r")
text=d1.read().split("\n")
d2=open('out.txt',"w")
q = len(text)
for i in range(q):
 d2.write(str(i+1))
 d2.write("\t")
 d2.write(text[i])
 d2.write('\n')
d1.close
d2.close()

print("Задание №4")
d = open('rt.txt')
acc = 0
for line in lines:
	lst = line.split(' ')
	acc += sum(list(map(int, lst)))
d.close()


print("#Сумма всех строк равана - ",acc,"#")

print("Задание №5")
d = open('rt.txt', 'r')
a=0
l=0
c=0
e=0
k=0
text = d.read()
lines = text.split('\n')
for line in lines:
 a+=int(lst[0])
 l+=int(lst[1])
 c+=int(lst[2])
 e+=int(lst[3])
 k+=int(lst[4])
 
print("#Cумма 1 строки -",a,"#" ,"#Cумма 2 строки - ",l,"#","#Cумма 3 строки - ",c,"#","#Cумма 4 строки - ",e,"#","#Cумма 5 строки - ",k,"#")

if a>l>c>e>k:
 print("Большее из них число -a-",l)
else:
  if l>c>e>k:
    print("Большее из них число -l-",l)
  else:
    if c>e>k:
      print("Большее из них число -c-",c)
    else:
      if e>k:
       print("Большее из них число -e-",e)
      else:
       print("Большее из них число -k-",k )




# print("Задание №6")