#!/usr/bin/python3
import yaml

doc="""
name:srinivas
desccription:>
	bad boy
	not a good guy
	unlucky guy


"""

for data in yaml.load_all(doc):
	print (data)
