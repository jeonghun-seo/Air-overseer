import time
import serial

def get_data():
    serial_port = serial.Serial(
    port="/dev/ttyTHS1",
    baudrate=115200,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    )
    # Wait a second to let the port initialize
    time.sleep(1)
    try:
        buffer = ""  # 데이터를 저장할 버퍼 초기화
        while True:
            if serial_port.inWaiting() > 0:
                data = serial_port.read().decode()  # 읽은 데이터를 문자열로 변환
                buffer += data  # 버퍼에 데이터 추가

                if '=' in buffer:  # newline 문자가 버퍼에 있는지 확인
                    lines = buffer.split('=')  # 버퍼를 newline 문자로 분할
                    for line in lines[:-1]:  # 마지막 줄은 다음 버퍼에 저장
                        print(line)  # 한 줄씩 출력
                    buffer = lines[-1]  # 다음 루프에서 사용할 버퍼로 설정
                    return line
    finally:
        serial_port.close()
