import pythonwhois
import sys
import json


arguments=sys.argv[1]#we can get filename through argv
#file_data=OrderedDict()

f=open(arguments,'r')

data=f.readline()

webdata=pythonwhois.get_whois(data)#we can get whois data

f2=open("jsonfiles",'w')
#print webdata['nameservers']


def date_handler(obj):		#this funciton in order to catch timeerror
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    else:
        raise TypeError
#// use two argument, we can catch timeerror,this is json encoding
data2=json.dumps(webdata,default=date_handler)

f2.write(data2)

#file_data["status"]=data[status}
#f2.write(unicode(json.dumps(webdata,ensure_ascii=False)))
#print webdata
f.close()
#print(domain1)
#status contacts nameservers
f2.close()
