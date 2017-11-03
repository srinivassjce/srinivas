import re
import random
import pdb

class cowsandBulls(object):
    def __init__(self):
        pass

    def generate_random(self):
        self.base=random.randint(10,99)
        return self.base

    def validate_two_digit(self,number):
        return re.match(r'^\d\d$',number,re.IGNORECASE)

    def get_input(self):
        self.input=raw_input("Enter two digit number : ")
        self.validate_two_digit(self.input)


    def check_cows(self):
        cow_count=0
        index_list=[]
        self.base_list=[]
        for i in str(self.base) :
            self.base_list.append(i)

        self.number_list=[]

        for j in str(str(self.input)) :
            self.number_list.append(j)

        for i in range(len(str(self.base)) ) :
            if self.base_list[i] != self.number_list[i] :
                cow_count +=1
            else :
                index_list.append(i)

        return (cow_count,index_list)

    def check_bulls(self,list1,b):
        self.list1=list1
        bull_count=b
        pdb.set_trace() 
        for i in self.list1 :
            if str(self.base_list[i]) == str(self.number_list[i]) :
                  bull_count +=1
		  print "bull_count",bull_count
        return  bull_count




if __name__ == "__main__" :
    game=cowsandBulls()
    print "computer orginal number is " ,game.generate_random()
    result=0
    b=0
    while not result :
        game.get_input()
        g=game.check_cows()
        b=game.check_bulls(g[1],b)
        print "cows count and bull count are : ",g[0],b
        if not g[0]  :
            result=1
            break
        print "GAME is LIVE"

    if result :
        print "Entered number by user is same as computer generated number"
        print "GAME OVER"
