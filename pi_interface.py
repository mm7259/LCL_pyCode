# sensors: 
# - RFID for association of LCL + container
# - GPS for detecting LCL destination 
# - A counter to start association/ loading session

#GPS is emulated using timer 
#RFID tag is emulated using button press 
#each loading session is represented by the counter
import requests
import time 

listOfLCL = [1, 2, 3]
tagurl = 'https://lcl-enterprises.herokuapp.com/lcls/register' 
arrivalurl = 'https://lcl-enterprises.herokuapp.com/lcls/arrived'

counter = 0; 

while counter <= 2: 
	randLCL = randint(0, 2)
	tagEmulate = input("Press a to emulate the tag: ")
	if tagEmulate == 'a': 
		#container ID is unique to each microprocessor
		r = requests.post(tagurl, data = {'container_id' : "GLFU2814428", 'lcl_id' : listOfLCL[randLCL]})  
	counter = counter + 1 #simulates each loading session 


time.sleep(3)
#after 3 seconds have been elapsed (emulating arrival)
arrival = requests.post(arrivalurl, data = {'container_id' : "2"} )
