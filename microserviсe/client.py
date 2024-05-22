
import http.client
import sys
import time

#get http server ip
http_server = sys.argv[1]
#create a connection
conn = http.client.HTTPConnection(http_server)

while 1:
    cmd = input('input: ')

    conn.request("GET", "client:"+cmd)
    rsp = conn.getresponse()
    
    data_received = rsp.read().decode("utf-8")

    result = "EMPTY"

    while (result == "EMPTY"):

        conn.request("GET", "checkres")
        rsp = conn.getresponse() 
        data_received = rsp.read().decode("utf-8")
        result = data_received
        time.sleep(0.25)

    print(result)
    
conn.close()