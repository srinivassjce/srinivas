#!/usr/bin/python
import re
import random
import time
print 'welcome to the game of numbers'.upper()
print '-----------------------------------------------------'
print '\n\nHere are game rules\n\nPlayer has to choose the range of rumbers from 0 to [choice]e.g 5,6,10\n\nTaget will 10 times the number entered e.g 5 is range then 50 is target \n\nPlayer or computer will start  the game \n\nplayer/computer every turn can selects number in next range\n\nwhoever reach the target will lose the game\n\nhence (target-1) who chooses intellenetly can win the game'.upper()
print '-----------------------------------------------------\n\n'

def whoseturn() :
	if random.randint(0,1) : 
		return str('PC')  
	else : 
		return str('Player') 


def validate_input(x,y,input_value) :
	print x,y,input_value
	if y <= input_value >= x :
		return input_value
	else :
		input_value=input(  'PC : Enter the input within the  range of '.upper() + str (x) +' to '+ str(y) + ' : => ' )
		validate_input(x,y,input_value)


		
def create_intel_list(range_input):
	step_neg=range_input * -1
	intel_list=[]
	for i in range ((range_input*10)-1,1,step_neg):
		intel_list.append(i)
		
	return intel_list

def chose_intel_list(intel_list,x,y) :
	for i in range(x,y + 1,1) :
		if i in intel_list :
			return i
	return 0


def player_entry(player,range_input,input_value,intel_list) :
	x= input_value + 1
	y= input_value + range_input 
	if player :
		input_value=chose_intel_list(intel_list,x,y) 

		if  input_value :
			print 'Computer has chosen value : ' + str(input_value) 
		else :
			input_value=random.randint(x,y) 
			print 'Computer has chosen value : ' + str(input_value)



	else : 
		input_value=input( first_player + ': Enter the input within the  range of '.upper() + str (x) +' to '+ str(y) + ' : => ' )		
		
                        	
	return (x,y,input_value)

def checkforwin(i,r) :
	
	if i == (r*10) - 1 :
		
		return (1,1)
	elif i < (r*10 -1)  :
		return (0,0)
	elif i >= (r*10) :
		return (1,0)
	
	
flag=0
while True :
	range_input=input ('Choose the range of number from 0 to choice :   '.upper())
	print 'Entered range is 1 to '.upper() +' to '+str(range_input)
	print 'Target number is ' + str ( range_input * 10 )	
	print 'Game starts now \n\n'.upper()
	first_player=whoseturn()
	print 'TOSSing for whoseturnfirst:  PC / PLAYER ===> Now its '.upper() + first_player + ' turn '
	x= 1
	y= int (range_input )
	intel_list=create_intel_list(range_input)
	if first_player.lower()  == 'PC'.lower() :
		player=bool(1)
	else :
		player=bool(0)
	

	while True :
		global x
		global y
		global intel_list
		if player :
			''' Computer turn'''
			input_value=chose_intel_list(intel_list,x,y) 
			if input_value >= x and input_value <= y :
				print 'Computer has chosen ' + str(input_value)
				pass
			else :		
				continue	
		else :
			'''Player turn '''		
			try :	
				input_value=int (raw_input('Enter the input ' + str( ' b/w ') + str(x) + ' and '+ str(y) + ' :'  ) )
			except :
				print 'Wrong input , provide integer value '

			if input_value >= x and input_value <= y :
                                pass
                        else :
				print 'Kinldy Enter the correct input '.upper()
                                continue
 
		(result,flag)= checkforwin(input_value,range_input)
		if result == 1 :	
			break
		x=input_value + 1
		y=input_value + range_input
		player= not(player)
	
	if flag==1  and player :
		print 'Computer WON the game '.upper()
	else :
		print 'Player WON the game '.upper()
		
	
	time.sleep(3)
			 

