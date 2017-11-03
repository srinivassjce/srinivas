#!/usr/bin/python
from __future__ import print_function
import random
import datetime
import pandas as pd
import texttable as tt
print ('Game of Identifing odd-man out'.upper() )
tab=tt.Texttable()

game={
	8:0,
	0:'O',
	3:9,
	':':';',
	';':':',
	'{':'}',
	'E':3,
	
	}
	
	
while True :
	score=0
	total=0
	for (k,v) in game.items() : 
	#	print (k,v)	
		try:
			rows=raw_input('Enter numberr of rows : ') 
			cols=raw_input('Enter numberr of cols : ') 
		except :
			print ('Wrong input ')
			exit(1)

		rows=int(rows)
		cols=int(cols)


		choice= int (random.choice ( list (  range (cols * rows) )  ) )


		a=str(k)*rows
		p=1
		v=[]
		for i in range(cols) :
			l=[]
			for j in a :
		
				if p == choice :
					print (v,end=' ')
					l.append(v)
				else :
					print (j,end=' ')
					l.append(v)
				p +=1

			print ('') 
			v.extend(l)
		df = pd.DataFrame(l)
		print (df)
		
		print ('Identify odd man out'.upper() )
		
		try :
			userinput=raw_input('Enter postion of odd man out : '.upper())
			
			if int(userinput) == choice :
				print ('user idenify the proper postion of odd man out'.upper())
				score  += 1  
				total  += 1
				print ( 'user score '.upper() + '--------: ' + str(score) + '/' + str(total)  )
			else :
				print ('user entered the wrong postion'.upper() )
				total += 1 
				print ( 'user score '.upper() + '--------: ' + str(score) + '/' + str(total)  )
		except TypeError :
			print ('TypeError')

		except :
			print ('Wrong integer input'.upper() )
			



