def alko_1():
# Shifrovka
#  n = 2**16-1
# print(n,chr(n))
 from alkad import getSifr, getDeSifr, get
 s=input("Введите фразу - ")
 key=int(input("Введите ключ - "))
#  p=int(input("Если хотите расшифровать введите - 1, иначе введите - 1 - "))
 newS = getSifr(key, s)

 print(s,'\n',newS,sep='')

 deSifr = getDeSifr(key,newS)

 print(deSifr)


 print()
 newS = get(key, s)
 print(newS)
 deSifr = get(key,newS,-1)
 print(deSifr)