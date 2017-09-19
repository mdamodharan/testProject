import time;
print("To print the current time")
localtime = time.asctime( time.localtime(time.time()) )
print("Local current time :", localtime)
print ("Current date"+time.strftime("%d/%m/%Y"))
print("testing webhook")
