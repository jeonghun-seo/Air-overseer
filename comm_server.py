import requests
import os
import json

#secret key 로드
secret_file = "secrets.json"

with open(secret_file) as f:
    secrets = json.loads(f.read())
    
server_ip = secrets["server_ip"]
port = secrets["port"]

def upload(img_name,result_str):
    files = open(img_name,'rb')
    upload = {'file':files}
    data = {'obj':result_str}
    res = requests.post(f'http://{server_ip}:{port}/upload',files=upload, data=data) #로컬 서버로 전송
    if (res):
        print("POST Done!")

def check_status():
    res = requests.post(f'http://{server_ip}:{port}/status')
    flag = res.text
    print(f'now status is {flag}')
    return flag

check_status()