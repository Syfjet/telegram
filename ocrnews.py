# -*- coding: utf-8 -*-
import config
import telebot
import time
import sys

from bs4 import BeautifulSoup
from urllib.request import urlopen
global full_list

full_list = []

def finder(name):
	page = urlopen('https://vk.com/wall-'+str(name))
	soup = BeautifulSoup(page,'html.parser')
	tag = str(soup)
	lis = tag.split('>')
	list_wall = []
	for i in range(len(lis)):
		if '<a class="post' in lis[i]:
			list_wall.append(lis[i][43:-1])
			
	list_wall = sorted(list_wall)
	print(list_wall) 
	result = list_wall[len(list_wall)-1]
	return result

def opt_post(result):
	flag = 1
	# f = open('list_post.txt','r')
	# lis = f.readlines()
	# f.close()
	#print(full_list,result)
	#sys.exit()
	for i in range(len(full_list)):
		if str(result) == str(full_list[i]):
			flag = 0
			break
	if flag == 1:
		full_list.append(result)
		# f = open('list_post.txt','a')
		# f.write(result+'\n')
		# f.close()	
	return flag
##############################################						
liga_list = []
liga_list.append(102783620) #liga_heroes
liga_list.append(74256839) #Race_Gladiators
liga_list.append(117680198) #StandMan
#liga_list.append(81769179) #lifeSport
liga_list.append(109465610) #Bear Race
liga_list.append(57722658) #Heroes Race
##############################################		

bot = telebot.TeleBot(config.token)	
while True:
	for i in range(len(liga_list)):
		liga_ = finder(liga_list[i])
		flag = opt_post(liga_)
		if flag == 1:
			bot.send_message('@OCRnews', 'https://vk.com/wall-'+str(liga_))
			time.sleep(1)
	time.sleep(60)