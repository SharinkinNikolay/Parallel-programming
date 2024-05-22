
import http.client
import sys
import time

#get http server ip
http_server = sys.argv[1]
#create a connection
conn = http.client.HTTPConnection(http_server)

while 1:

    time.sleep(0.25)
    #request command to server
    conn.request("GET", "worker:GET")

    #get response from server
    rsp = conn.getresponse()

    if(rsp.status == 200):  
        data_received = rsp.read().decode("utf-8")
        if(data_received == 'EMPTY'):
            continue

        result = str(eval(data_received))

        conn.request("GET", "result:"+result)

        #get response from server
        rsp = conn.getresponse()

        print(rsp.status, rsp.reason)
        data_received = rsp.read().decode("utf-8")
        print(data_received)

    
conn.close()
