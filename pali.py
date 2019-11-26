def pali_1():
 import palu as m
 lines = m.getLines('rut.txt')
 for line in lines:
	 print(m.palindrom(line), ' - ', line)
