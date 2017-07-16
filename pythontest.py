import pythonwhois
import sys
import json

#This function can catch typeeroor
def date_handler(obj):		
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    else:
        raise TypeError

# we have to write filename
argumens=sys.argv[1]
f=open(argumens,'r')





f2=open("jsonfiles",'w')
#we can receive domain google.com and, daum.net
for x in range(2):
	data=f.readline()
	webdata=pythonwhois.get_whois(data)
	data2=json.dumps(webdata,default=date_handler)
	f2.write(data2)
	#f2.write("\n ---------------------------------------------------- \n")

f.close()
f2.close()

