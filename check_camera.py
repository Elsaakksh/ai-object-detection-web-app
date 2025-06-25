import cv2

print("正在尝试打开摄像头...")
# 尝试打开默认摄像头
cap = cv2.VideoCapture(0)

# 检查摄像头是否真的打开了
if not cap.isOpened():
    print("错误：无法打开索引为 0 的摄像头。")
    # 尝试其他索引
    print("正在尝试索引 1 ...")
    cap = cv2.VideoCapture(1)
    if not cap.isOpened():
        print("错误：也无法打开索引为 1 的摄像头。请检查摄像头是否连接或被其他程序占用。")
        exit()

print("摄像头成功打开！按 'q' 键退出。")

while True:
    ret, frame = cap.read()
    if not ret:
        print("无法从摄像头读取帧。")
        break

    # 显示原始帧
    cv2.imshow('Camera Test', frame)

    # 等待1毫秒，并检查按键
    # 这一行至关重要！没有它，窗口可能无法刷新。
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()
print("程序已正常退出。")