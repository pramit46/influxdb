import json
import requests
import time
import datetime
import random


#errorcount, APP=EM, type=IISlog, region=aws-e errorcode=<<errorcode>>,errorcount=<<number>> <<timestamp>>
#errorcount,app=em, type=iislog errorcode=503,errorcount=160 1477300521



filename='ErrorCountDataFile.txt'
#target = open(filename, 'w')
for x in xrange(0,500):

        #target = open(filename, 'w')

        rand=(random.randint(0,100))
        errorcode_rand=(random.randint(500,503))
        errorcode=errorcode_rand

        #print(str(rand))
        #now = datetime.datetime.now()
        #print('str:'+str(now))

        #dtime = datetime.datetime.now()
        #timestamp = time.mktime(dtime.timetuple())

        measurement = 'errorcount'

        value = 'errorcount'+'='+(str(rand))
        #print(tag)

        tag = 'app'+'='+'emite'+','+'type'+'='+'iislog'+','+'errorcode'+'='+str(errorcode)
        #print(value)

        point_val = measurement+','+tag+' '+value+' '

        #+' '+str(int(timestamp))    # +str(1422568543702900261)
        print(point_val)

        #target.write(point_val)
		#target.write("\n")

        #target.close()

        url = "http://10.121.48.24:8086/write?db=pramit"
        #file_data = open(filename, 'rb').read()
        #fs = {'file' : open(filename,'rb')}
        r = requests.post(url,data=point_val)
        print(r.text)
        print(r.json)


#curl -i -XPOST 'http://localhost:8086/write?db=pramit' --data-binary @DataFile.txt
#errorcount,app=em, type=iislog errorcode=503,errorcount=160 1477300521
