import cv2 as cv


def face_detect_demo(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # 将图片灰度
    # 加载特征数据
    face_detector = cv.CascadeClassifier('D:/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml')
    faces = face_detector.detectMultiScale(gray)
    for x, y, w, h in faces:
        cv.rectangle(img, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=2)
        # cv.circle(img, center=(x + w // 2, y + h // 2), radius=(w // 2), color=(0, 255, 0), thickness=2)
    cv.imshow('result', img)


# 读取视频
cap = cv.VideoCapture('videos/video.mp4')
# 视频重复播放，每一帧都是一张图片
while True:
    flag, frame = cap.read()
    if not flag:
        break
    print('flag:', flag, 'frame.shape:', frame.shape)
    face_detect_demo(frame)
    if ord('q') == cv.waitKey(10):
        break
cv.destroyAllWindows()
cap.release()
