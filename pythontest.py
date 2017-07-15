import pythonwhois
import sys
import json
#from collections import OrdereDict

#file_data=OrderedDict()

f=open("domains",'r')

data=f.readline()

webdata=pythonwhois.get_whois(data)

f2=open("jsonfiles",'w')
#print webdata['nameservers']

#json_acceptable_string = webdata.replace("'", "\"")
def date_handler(obj):		#this funciton in order to catch timeerror
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    else:
        raise TypeError
#// use two argument, we can catch timeerror,json encoding
data2=json.dumps(webdata,default=date_handler)

f2.write(data2)

#file_data["status"]=data[status}
#f2.write(unicode(json.dumps(webdata,ensure_ascii=False)))
#print webdata
f.close()
#print(domain1)
#status contacts nameservers
f2.close()
