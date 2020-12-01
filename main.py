import cv2
import pickle 
from isl_converter.video_processing.video_capture import image_modification as image_modeifier
import warnings
from isl_converter.text_symbolmodule import symboltotext as texter
from isl_converter.video_processing import image_transformation as image_changer
from isl_converter.text_symbolmodule.speechtosymbol import speechtosign 
def main():
    var = input("Enter 1 for symbol to text and 2 for speech to symbol")
    while (var == '1' or var == '2'):
        if (var == '1'):
        
            path = input("enter camera for camera to take live video feed else enter the path of the file ")
            if path == "camera" :
                capture=cv2.VideoCapture(0)
                while capture.isOpened():
                    check,frame=capture.read()
                    lenght_frame = len(frame)
                    cv2.rectangle(frame,(100,100),(lenght_frame,lenght_frame), (0,255,0),0)
                    cv2.imshow("camera",frame)
                    frame = image_modeifier(frame)
                    print(texter.predict(frame))
                    if cv2.waitKey(1)==ord('q'):
                        break
                capture.release()
                cv2.destroyAllWindows()
            else :
            
                path = path[1:-2]
                frame = cv2.imread(path)
                frame = image_changer.apply_image_transformation(frame,0)
                print(texter.predict(frame))
        elif (var == '2'):
            speechsign = speechtosign()
            speechsign.converttosign()
        else :
            exit(0)
        var = input("Enter 1 for symbol to text and 2 for speech to symbol")

            
warnings.filterwarnings('ignore')
if __name__ == "__main__" :
    main()
