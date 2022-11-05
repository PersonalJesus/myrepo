# import requests module 
from pip._vendor import requests
from datetime import datetime
import time
# Making a get request
list_of_servers = ('api.github.com', 'gitlab.com/api/v4')


starttime = time.time()
while True:
    for sites in list_of_servers:
        response = requests.get(sites)
        answer = response.json()
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")

        print(dt_string + ' ' + sites + ' ' + str(answer['id']))
    
    time.sleep(60.0 - ((time.time() - starttime) % 60.0))

