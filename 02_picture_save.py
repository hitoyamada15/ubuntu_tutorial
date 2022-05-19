import cv2
import datetime  # datatimeパッケージを読み込む

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    strdate=datetime.datetime.now().strftime('%Y%m%d_%H%M%S') # 今の"年月日_時分秒"をファイル名にする
    cv2.imshow('frame',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('s'): # もしキーボードの"s"を押すと
        img_name = "image/" + strdate + ".jpg" # ファイル名を指定
        cv2.imwrite(img_name, frame) # imwriteでframeをimg_nameで保存
    
    elif cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
