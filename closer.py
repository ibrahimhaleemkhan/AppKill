#this App closes unecessary files  , and gives information for the users to kill them again and again
import os, time
# this section is for Windows linux coming soon
#IBRAhIM hALEEM khan
#github.com/ibrahimhaleemkhan

def displayprogs():
	while True:

        	print " The FOllOWING are the Processes that you can close \n and they have been assigned a activity Status \n "
        
        	print "THE PROCESS BELOW ARE CURRENLTY RUNNING THE BACKGROUND : \n"
        	time.sleep(2)
        	os.system("tasklist")
        	try:
        		print "-----------------------------------------------------------------------"
        		apid = int(input("Please Enter The Process PID, YOu want TO kill  "))
        		print "-----------------------------------------------------------------------\n"
        		
        	except Exception as e:
        		print "|___________________________________________|"
        		print "|Enter Proper Numeric PID- PROCESS ID       |"
        		print "|___________________________________________| \n"
        		time.sleep(2)
        		continue
        		raise e
       	

        	try:
        		os.popen('TASKKILL /PID '+str(apid)+' /F')  
        		 
        		print "|___________________________________________|"
        		print "|Successfully KILLED PID :",apid,"           |"
        		print "|___________________________________________| \n"             
        
        	except Exception as e:
        		print "You dont Have Sufficent PRiv, Please Run as adminsitrator"
        		raise e

        	print "Want TO kill Another ?"
        	a =raw_input("YES/NO")
        	if a=="yes"or "YES"or "y" or "Yes":
        		continue
        	else :
        		print "BHUYE BHYE"
        		exit()
        		break

		
displayprogs()
