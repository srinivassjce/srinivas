import os
import shutil
import re
import stat
from stat import *
import glob
import os
import time
import operator
import pdb
from sys import exc_info


alist={}
now = time.time()
my_path = "//172.17.40.40/cpe/AMI/Builds/OWI_Builds/ASIC_SCE_FAN_DEMO/Latest"

print(my_path)
#print(os.listdir(my_path))

f = open("C:\\ASIC\\Builds\\code\\file.txt",'w+')
l = f.readlines()
f.close()	

os.chdir(my_path)
for file in os.listdir("."):
	if os.path.isdir(file):
		timestamp = os.path.getmtime( file )
        # get timestamp and directory name and store to dictionary
		alist[os.path.join(os.getcwd(),file)]=timestamp
		
#sort the timestamp in dictionary(i.e sorting by value)
for i in sorted(alist.items(), key=operator.itemgetter(1)):
	latest="%s" % ( i[0])
print("newest directory is ", latest)

build_name = os.path.basename(latest)
print("latest build name is : ",build_name)

os.chdir(latest)
new_path = latest + "\\Distribution-Files\\ASIC-NIC-Dev\\"
print("new_path = ",new_path)

final_path_list = os.listdir(new_path)
print("final path list = ",final_path_list)

var = re.findall(r'(\w+\-\w+\-\w+\.\w+\.gz)',str(final_path_list))[0]
print(new_path+'\\'+var)

# base dir
dir = "C:\\ASIC\\Builds\\node\\A7_builds"       

# create dynamic name like C:\ASIC\Builds\node\A7_builds\FW_0_4_41_770269-Nov02Build\
dir = os.path.join(dir, build_name)

# create 'dynamic' dir, if it does not exist
if not os.path.exists(dir):
    os.makedirs(dir)
print("Directory path = ",dir)


if new_path not in l:
	build= str(new_path)+str(var)
	print("Latest build-%s "%build)
	shutil.copy2( str(new_path)+str(var),dir)
elif l == None:
	pass
else:
	print("***Build already exists***\n")
	
#copying latest build name in to file
f = open("C:\\ASIC\\Builds\\code\\file.txt",'w')
f.write(new_path);
f.close()
