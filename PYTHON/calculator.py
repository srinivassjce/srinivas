#!/usr/bin/python
from collections import Counter
class calculator :
	def __init__(self) :
		pass
		
	def add(self,*number) :
		self.number=number
		sum=0
		for i in self.number :
			sum += i
		return sum		

	def diff(self,*number) :
		self.number=number
		diff=self.number[0]
		for i in self.number[1::] :
			diff -= i
		return diff
	def mul(self,*number) :
                self.number=number
                result=1
                for i in self.number :
                        result *= i
                return result

	def div(self,*number) :
		self.number=number
		result= self.number[0]
		try : 
			for i in self.number[1::] :
				result /=i

		except ZeroDivisionError:
			print 'Error:ZeroDivisionError'
		
		else :
			return result
			print 'Divsion is fine'

	def count(self,*number) :
		self.number=number
		return  Counter(self.number) 
		

		

cal=calculator()
print cal.add(3,4,5)
print cal.diff(10,4,5)
print cal.mul(2,3,4)
print cal.div(1,2,1)
a=cal.count(1,2,2,1,1,1,1,1,1,1,2,3,3,2,2,2,3,3,3,4,4,4,5,5,5,5,5)
for k,v in  a.items() :
	print 'Number of ' + str(k) +' in list are ' + str(v)





	


