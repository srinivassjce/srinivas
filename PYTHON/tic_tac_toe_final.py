#!/usr/bin/python
import time
import random
def boardposition(board):
	print '==============    [Reference  postions]\n\n'
	print '\t'+ '|'+board[1] + '|' + board[2] + '|' + board[3] + '|'      + '\t\t'+ str(1) + '|' + str(2) + '|' + str(3)
	print '\t'+ '|'+board[4] + '|' + board[5] + '|' + board[6]  + '|'    + '\t\t'+ str(4) + '|' + str(5) + '|' + str(6)
	print '\t'+ '|'+board[7] + '|' + board[8] + '|' + board[9]  + '|'    +  '\t\t'+ str(7) + '|' + str(8) + '|' + str(9)
	print '\n\n======================================\n'

def whoseturnfirst() :
	return random.randint(0,1)


def chooseXorO() :
	input_player=raw_input('Choose either X or O  to fill the board : ')
	if input_player.lower() == 'x' :
		return 'X'
	elif input_player.lower() == 'o' :
		return 'O'
	else :
		print 'Input is wrong kindly '.upper()
		chooseXorO()

def clearboard() :
	board=[' ']
	board= board * 10
	return board


def wincheck(board,map1) :
	#print board , map1
	return ( board[1] == board [2] == board[3] == map1 or
		 board[4] == board [5] == board[6] == map1 or
		 board[7] == board [8] == board[9] == map1 or
		 board[1] == board [4] == board[7] == map1 or
                 board[2] == board [5] == board[8] == map1 or
                 board[3] == board [6] == board[9] == map1 or
		 board[1] == board [5] == board[9] == map1 or
                 board[3] == board [5] == board[7] == map1 )
	


def playermove(board,map1) :
	#boardposition(board)	
	global input1
	sublist=[]
	for i in range(1,10):
                if board[i] == 'X' or board[i] == 'O':
                        pass
                else :
                        sublist.append(i)
	try :
		global input1
		input1= int(raw_input('choose the postions out of   ' +  str (sublist) + '  : ' ))
	except :
		print 'Input is wrong '.upper()
		playermove(board,map1)	

	if int(input1) not in sublist :
		print 'Input is wrong '.upper()
		playermove(board,map1)
	else :
		print 'Entered position is ' + str (input1)
		input1=int(input1)
		board[input1] = map1
		print 'board postion after player entry'.upper()
		boardposition(board)
		return board
	return board


def decide_input(board,sublist,map1) :
	if map1 == 'X' :
		map2='O'
	else :
		map2='X'
	for i in range(1,10,3) :
		if board[i:i+2].count(map2) == 2 :
			for j in  range(i,i+3) : 
				if  j in sublist :
					return j
		elif board[i:i+2].count(map1) == 2 :
                        for j in  range(i,i+3) :
                                if  j in sublist :
                                        return j


	for i in range(1,4) :
		list1=[ board[i] , board[i+3] , board[i+6] ]
                if list1.count(map2) == 2 :
                        for j in  range(i,10,3) :
                                if  j in sublist :
                                        return j
		elif list1.count(map1) == 2 :
                        for j in  range(i,10,3) :
                                if  j in sublist :
                                        return j


	list1=[board[1] ,board[5],board[9] ]
	if list1.count(map2) == 2 :
                        for j in  range(1,10,4) :
                                if  j in sublist :
                                        return j
	elif list1.count(map1) == 2 :
                        for j in  range(1,10,4) :
                                if  j in sublist :
                                        return j

	list1=[board[3] ,board[5],board[7] ]
        if list1.count(map2) == 2 :
                        for j in  range(3,8,2) :
                                if  j in sublist :
                                        return j

	elif list1.count(map1) == 2 :
                        for j in  range(3,8,2) :
                                if  j in sublist :
                                        return j

	return random.choice(sublist) 

		


def computermove(board,map1) :
        global input1
        sublist=[]
        for i in range(1,10):
                if board[i] == 'X' or board[i] == 'O':
                        pass
                else :
                        sublist.append(i)
        try :
                global input1
                input1= decide_input(board,sublist,map1)

                print 'computer entered position is ' + str (input1)
                input1=int(input1)
                board[input1] = map1
		print 'board postion after computer entry'.upper()
                boardposition(board)
                return board
	except :
		print 'Input Error'.upper()
        return board
	
	


def boardfullcheck(board) :
	for i in range(1,10) :
		if board[i] == 'X' or board[i] == 'O':
			pass
		else :
			return 1
	




 
while True:
	board=[' ']
	board= board * 10
	boardposition(board)
	turn=whoseturnfirst()
	if turn == 1 :
		print " player's turn to start filling the board ".upper()
		choice=chooseXorO()
		if choice == 'X' :
			compmap='O'
                        playermap='X'
		else :
			compmap='X'
                        playermap='O'
			
	else :
		print 'Computer turn'
		comp=whoseturnfirst()
		if comp :
			compmap='X'
			playermap='O'
			print 'Computer  has choosen X Hence player has to use O'

		else :
			compmap='O'
                        playermap='X'
                        print 'Computer  has choosen O Hence player has to use X'

	for i in range(1,10) :
		time.sleep(1)
		
		if turn  :
			board=playermove(board,playermap) 
			if wincheck(board,playermap) :
				print '------------------------------------------------------------\n'
				print 'Congrates !!!!!!!!!!!!! \n\n Player has own TIC-TAC-TOE game\n'
				break

			if boardfullcheck(board) :
                                pass
                        else :
                            print 'GAME is TIE' 
                            break

		else :
			board=computermove(board,compmap)
                        if wincheck(board,compmap) :
                                print 'Congrates !!!!!!!!!!!!! \n\n Computer has own TIC-TAC-TOE game\n'
                                break


			if boardfullcheck(board) :
				pass
			else :
			    print 'GAME is TIE'	
			    break		
		turn =  not (turn)

	
	
	time.sleep(1)

	while True :
		new_game=raw_input('Please enter Y/yes to start new game else enter Q/quit  :  '.lower()) 
		if new_game.lower() == 'y' or new_game.lower() == 'yes' :
			break
		elif new_game.lower() == 'q' or new_game.lower() == 'quit' :
			exit() 
		else :
			print 'Input is wrong'.lower()
			continue




