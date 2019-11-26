def game_1():
 print("##############################################")
 print("##  Вам нужно отгодать число от 100 до 998  ##")
 print("##############################################")
 from random import randint
 x = randint(100,999)
 money = 10
 luck=1
 lost=0
 print(x)

 while True:
   y=int(input('Введите число - '))
   if x==y:
     break;print("Красаучек")
   if x>y:
    #  print("###########################")
     print('######## Больше... ########')
     print("### Попробуй ещё раз... ###")
    #  print("###########################")
     money-=luck
   if money==lost:
     print("You lose");break
   if x<y:
		#  print("###########################")
     print('######## Меньше... ########')
     print("### Попробуй ещё раз... ###")
    #  print("###########################")
     money-=luck
 print("Твой выигрыш - ")
 print(money)
 print("Нужное число - ")
 print(x)