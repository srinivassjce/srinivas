#!/bin/bash

if [ $# -ne 1 ]
then
	echo "Atleast 1 argument should be passed"
	echo "Usage: $0 date"	
	exit 1
fi
date=$1

if [ -d Emails ]
then
	rm -f Emails/*
else
	echo "Emails directory does not exist. So creating a new directory"
	mkdir Emails
fi


while read -r line
do
email=$(echo "$line" | awk -F "," '{print $1}')
fullname=$(echo "$line" | awk -F "," '{print $2}')
name=$(echo "$fullname" | awk '{print $2}')
title=$(echo "$line" | awk -F"," '{print $3}')
amount=$(echo "$line" | awk -F"," '{print $5}')
paidamount=$(echo "$line" | awk -F"," '{print $4}')
date=$(echo $date | sed 's@/@-@g')

if [ $(echo "$amount > $paidamount" |bc -l ) ]
	then
               outfile="g${fullname}.txt"
		
               cat template.txt | sed -e "s/FULLNAME/$fullname/;s/EMAIL/$email/;s/TITLE/$title/;s/NAME/$name/;s/AMOUNT/$amount/;s/DATE/$date/">"Emails/$outfile"
		
		 
        fi

done < p4Customer.txt
