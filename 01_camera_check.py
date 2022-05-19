import cv2 # opencvパッケージを読み込む

cap = cv2.VideoCapture(0) # 0番目のカメラ情報を取得

while(True): # while文の無限ループ
    ret, frame = cap.read() # capを読み込む(ret:カメラ情報, frame:映像データ)
    cv2.imshow('frame',frame) # ディスプレイに映像を表示
    if cv2.waitKey(1) & 0xFF == ord('q'): # もしキーボードの"q"を押すと
        break # while文から抜ける

cap.release() # カメラを切断
cv2.destroyAllWindows() # imshowで表示したウィンドウを削除
