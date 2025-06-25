import cv2
from ultralytics import YOLO
import time

# 加载预训练的YOLOv8n模型 (n代表nano，是最小最快的版本)
# 模型会自动从网络下载（如果第一次运行）
model = YOLO('yolov8n.pt')

# 打开你的默认摄像头 (通常索引是0)
cap = cv2.VideoCapture(0)

# 检查摄像头是否成功打开
if not cap.isOpened():
    print("错误：无法打开摄像头。")
    exit()

print("摄像头已启动，按 'q' 键退出。")

prev_frame_time = 0
new_frame_time = 0

# 循环读取摄像头的每一帧
while True:
    # success是一个布尔值，如果成功读取帧则为True
    # frame是捕获到的图像帧
    success, frame = cap.read()

    if not success:
        print("无法接收帧，可能视频流已结束。")
        break

    # --- 核心部分：在帧上运行YOLOv8推理 ---
    # results是一个包含检测结果的列表
    results = model(frame)

    # --- 可视化结果 ---
    # plot()方法会在原始帧上绘制边界框和标签
    annotated_frame = results[0].plot()

    # --- 计算并显示帧率 (FPS) ---
    new_frame_time = time.time()
    fps = 1 / (new_frame_time - prev_frame_time)
    prev_frame_time = new_frame_time
    fps_text = f"FPS: {int(fps)}"
    cv2.putText(annotated_frame, fps_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # 显示处理后的帧
    cv2.imshow("YOLOv8 Real-Time Object Detection", annotated_frame)

    # 如果在窗口中按下了 'q' 键，则退出循环
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# 释放摄像头资源并关闭所有OpenCV窗口
cap.release()
cv2.destroyAllWindows()
print("程序已退出。")