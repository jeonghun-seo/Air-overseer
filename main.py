import detector
import comm_server
import schedule
import numpy as np
import time

def run():
    flag = comm_server.check_status()
    print("서버 분기점 수신 완료")
    
    detected_list = detector.detect(flag)
    
    # 감지 후 인식된 객체 수 리스트의 평균을 구하고 반올림
    m = round(np.mean(detected_list[:-2])) 
    
    # 현재 시간 구하기
    detected_time = detected_list[-2]

    result_str = f'{detected_time}, 감지 결과:{m}'
    print(result_str)
    
    #파일명 가져오기
    img_name = detected_list[-1]
    
    #서버에 POST요청
    comm_server.upload(img_name,result_str)

schedule.every(30).seconds.do(run)

while True:
    print("스케줄 동작중...")
    schedule.run_pending()
    time.sleep(10)