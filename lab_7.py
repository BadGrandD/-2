# def task_1():
#print("--- Задание № 1 ---")


def task_2():
 print(" --- Задание № 2 ---")
 import pali 
 print("--- ПАЛИНДРОМ ---")
 pali.pali_1()


def task_3():
 import game
 print(" --- Задание № 3 --- ") 
 print("---- Игра началась, попробуй отгадай ----")
 game.game_1()

def task_4():
 print(" --- Задание № 4 --- ")
 r = open("steps.txt")
 text = r.read().split("\n")
 tab = []
 for i in text:
   tab.append(i.split())
 m = 0
 d = 0
 for i in range(len(tab)):
   m+=int(tab[i][0])*int(tab [i][2])
   d+=int(tab[i][1])*int(tab[i][2])
   m = m // 100
   d = d // 100
 print(abs(m-d))
























# a = input();
# b = 0;
# for i in range(len(a)):
#   if a[i] == a[len(a)-i-1]:
#     b+=1;
# if(b == len(a)):
#   print("палиндром")
# else:
#   print("не палиндром")