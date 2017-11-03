os.system("clear")

def ping_test(address) :
	if  re.search(r':',address) :	
		command = "ping6 -c 2 " + str(address) 
	elif re.search(r'.',address) :
		command = "ping -c 4 " +str (address)

	a= re.findall ( r'.*(\d)\s*received',os.popen(command).read() ) 
	if a[0] == '2' or a[0] == '1' or a[0] == '3' or a[0] == '4':
		cprint   ( "ping : %s SUCESS "%address.upper() ,'red' ) 
	else :
		cprint   ( "ping : %s  FAIL "%address.upper() ,'red' )

		sys.exit()

def ssh_command(host,command) :
	s = pxssh.pxssh()
        if not s.login (host, 'root',password='itron',port=22, auto_prompt_reset=False) :
                cprint ("SSH session failed on login -%s"%host ,red )
                print str(s)
        else:
                label ="=====================\n command : %s of %s\n ======================\n"%(command,host)
               	f=''
		if "ngcstatus.sh" in command : 
			f=" | grep -E " + str(filter_ngc)
		elif  "modversion" in command :
			f=  " | grep -E " + str(filter_modversion)
		
		if f :
			command = command  +  f
		else :
			command =command

                s.sendline (command)
		s.prompt()
                a = str (label) + str (s.before)        # match the prompt
                cprint (a,'blue')     # print everything before the prompt.
		s.logout()	

for  i in username_list :
	ping_test(i)


#proc = Process(target=doubler, args=(5,))
procs = []

for command in command_list :
    cprint ("Waiting  for status : %s"%command ,'cyan')	
    for host in username_list :
	proc=multiprocessing.Process(target=ssh_command, args=(host,command))
	procs.append(proc)
        proc.start()


for proc in procs:
        proc.join() 

