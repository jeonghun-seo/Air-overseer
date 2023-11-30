import requests

def upload(img_name,result_str):
    files = open(img_name,'rb')
    upload = {'file':files}
    data = {'obj':result_str}
    res = requests.post('http://127.0.0.1:3333/upload',files=upload, data=data) #로컬 서버로 전송
    if (res):
        print("POST Done!")