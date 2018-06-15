from random import *
from time import *
from colorama import Fore, Back , Style , init
import os
os.system('cls')
seed(clock())
init()
i = 0
HP = 100
B = 100
m = 150
G = 500
L=1
HP = 300
DMG = 40
print('Приветствую в butovogame')
x = int(input('1 - Воин \n2 - лучник \n3 - жирный\n'))
if x == 1:
	d = open('воин.txt','r')
	w = d.read()
	l = w.split('\n')
	print(l)
	for x in l:
		q = x.split(' = ')
		if q[0]=='HP':
			HP = int(q[1])
		if q[0]=='DMG':
			DMG = int(q[1])
if x == 2:
	print('|Вы выбрали класс лучник|')
	d = open('лучник.txt','r')	
	w = d.read()
	l = w.split('\n')
	print(l)
	HP = 200
	DMG = 50
if x==3:
	print('|Вы выбрали класс жирный|')
	d = open('жирный.txt','r')
	w = d.read()
	l = w.split('\n')
	print(l)
	HP = 500
	DMG = 25
while 1:
	a = randrange(6)
	if a==0:
		print('Вы видите вход в пещеру\n')
		q = int(input('1 - зайти \n2 - уйти \n3 - совершить самоубийство \n')) 
		if q == 1:
			if randrange(2):
				print('вы ничего не нашли\n')
			else:
				print('вы нашли золотой меч\n')
		if q == 2:
			print('вы решили ушли\n')
		if q == 3:
			break
	if a==1:
		print ('Бандит напал на вас,(есть шанс что вас убьют,если попробовать убежать)\n')
		q = int(input('1 - сражаться \n2 - убежать \n3 - совершить самоубийство\n'))
		if q == 1:
			while 1:
				B=B-DMG
				print('вы ударили бандита, ваше HP :',HP,'HP Бандита :' ,B,)
				HP=HP-randrange(15)
				print('вас ударил бандит, ваше HP :',HP,'HP Бандита :' ,B, )
				if HP<=0:
					print('Вы погибли\n')
					L=0
					break
				if B<=0:
					m=m+randrange(30)
					print('Бандит убит, собраны монеты, всего монет :',m,)
					m=m+15
					break
		if q == 2:
			if randrange(2):
				print('вы успешно убежали\n')
			else:
				print('Вас убили\n')
				L=0
				break
					
		if q == 3:
			break		

	if a==2:
		print('гоблин украл у вас монеты\n')
		m=m-randrange(30)
		print('Теперь ваши монеты :',m,)
	if a==3:
		print('Вас заметила группа маленьких гремлинов\n')
		q = int(input('1 - атаковать \n2 - убежать \n3 - совершить самоубийство\n'))	
		if q == 1:
				while 1:
					G = G -DMG
					print('Вы ударили каждого гремлина, HP группы :',G, )
					HP = HP - randrange(15)
					print ('Вам нанесли урон гремлины, ваше HP :',HP,)
					if G<=0:
						m=m+randrange(150)
						print('Вы убили группу, собраны монеты, всего монет :',m,)
						break
					if HP<=0:
						print('Вы погибли\n')
						L = 0
						break
		if q == 2:
			print('Вы успешно убежали но вас успели задеть\n')
			HP=HP-randrange(40)
			print('Ваше здоровье :',HP,)
		if q == 3:
			L = 0
			break
	if a==4:
		print('Вы споткнулись и упали на скалы, получен случайный урон')
		HP=HP-randrange(50)
		print('Ваше здоровье :',HP,)	
	if a==5:
		print('Вы нашли палатку')
		q = int(input('1 - купить зелье здоровья(стоимость : 10 монет,+30 HP\n 2 - купить зелье силы(стоимость : 50 монет,+15 DMG)\n 3 - пойти дальше\n'))
		if q==1:
			HP=HP+30
			m=m-10
		if q==2:
			DMG=DMG+15
			m=m-50		
	if not L:
		print('You are dead')
		break



			

