import shutil
import psutil
import os
import mysql.connector
from time import sleep
from datetime import datetime
                                       
                                                                      
while True:
 total, used, free = shutil.disk_usage("/")

 #Timestamp
 print("="*40, "Timestamp", "="*39)                             #Header
 now = datetime.now()
 current_time = now.strftime("%H:%M:%S")
 print("Current Timestamp =", current_time)

 #HDD Space
 totmem = "Total: %d GB" % (total // (2**30))
 usedmem = "Used: %d GB" % (used // (2**30))

 print("="*40, "Memory Info", "="*37)                           #Header
 print(totmem)
 print(usedmem)

 #RAM
 perram =psutil.virtual_memory().percent
 usedram = psutil.virtual_memory().used /1000000000

 print("="*40, "RAM Info", "="*40)                              #Header
 print(perram, "%")                                             #Memory use in %
 print(usedram, "GB")                                           #Memory use in GB

 #CPU
 cpuper = psutil.cpu_percent()
 cpufreq = psutil.cpu_freq()
 

 print("="*40, "CPU Info", "="*40)                              #Header
 print(f"Current Frequency: {cpufreq.current:.2f}Mhz")          #Momentante Frequenz
 print(cpuper, "%")

 mydb = mysql.connector.connect(                                     
  host="localhost",                                                 
  user="root",                                                      
  password="",                                                      
  database="monitoringtask") 
 mycursor = mydb.cursor()                                            
                                               
 sqlmemory = "INSERT INTO memory (id, computer_id, total, used) VALUES ('1','1','1','1');"
  
 sqlram = "INSERT INTO ram (id, computer_id, percentual, used) VALUES ('1','1','1','1');"

 sqlcpu = "INSERT INTO cpu (id, computer_id, frequency, percent) VALUES ('1', '1', '1', '1');"

               
 # Insert into cpu (id, computerid, frequency, percent) VALUES ()

 mycursor.execute(sqlmemory)
 mycursor.execute(sqlram)
 mycursor.execute(sqlcpu)
 mydb.commit()                             
                                             
 print(mycursor.rowcount, "record inserted.") 

 sleep(5)                                                       #5 second pause