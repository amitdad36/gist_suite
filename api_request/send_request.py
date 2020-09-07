import requests
from robot.api import logger
from requests.auth import HTTPBasicAuth

class send_request:
    def __init__(self,global_data):
        self.host = global_data['host']
        self.user = global_data['user']
        self.password = global_data['password']

    def send_request(self,method,url,json):
        res = ''
        try:
            res = requests.request(method=method,url=url,json=json,auth=HTTPBasicAuth(self.user,self.password))
        except Exception as error:
            logger.error(f'Http Request Failed : {error}')

        return res

if __name__=="__main__":
    global_data = {
        'host': 'api.github.com',
        'user': 'amitdad36',
        'password': 'amit036198823',
    }
    a = send_request(global_data)
    res = a.send_request('get','https://api.github.com/gists',{})
    print (res.status_code)
    print(res.content)
