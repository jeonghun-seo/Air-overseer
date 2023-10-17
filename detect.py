from ultralytics import YOLO 

def run(): #실시간 객체감지 테스트
    model = YOLO('models/yolov8n.pt')
    result = model.predict(source=0,show=True)
    return 0

if __name__=="__main__":
    print(__name__)