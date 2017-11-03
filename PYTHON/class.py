#!/usr/bin/python



class bankAccount():
	def __init__(self,name,account) :
		self.name=name
		self.account=account	
	def credit(self,credit):
		self.credit = credit
		print self.credit
	def debit(self,debit) :
		 self.debit=debit
		 print self.debit
	def balance(self,balance) :
		self.balance=self.credit-self.debit	




srinivas=bankAccount('srinivas',0001) 
srinivas.credit('100')
srinivas.debit(self,'')
print srinivas.name
print srinivas.account




