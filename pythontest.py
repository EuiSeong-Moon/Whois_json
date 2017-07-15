import pythonwhois
import sys
import json
#from collections import OrdereDict

#file_data=OrderedDict()

f=open("domains",'r')

data=f.readline()

webdata=pythonwhois.get_whois(data)

f2=open("jsonfiles",'w')

#file_data["status"]=data[status}
f2.write(unicode(json.dumps(webdata,ensure_ascii=False)))
#print webdata
f.close()
#print(domain1)
#admin
f2.close()
