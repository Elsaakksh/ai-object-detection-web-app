from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import cv2
from ultralytics import YOLO
import asyncio
import numpy as np

# --- 初始化 ---
# 创建FastAPI应用实例
app = FastAPI()

# 设置HTML模板目录
templates = Jinja2Templates(directory="templates")

# 加载YOLO模型
model = YOLO('yolov8n.pt')

# --- 辅助函数：将图像编码为JPEG ---
def encode_frame_to_jpeg(frame):
    """将OpenCV的图像帧编码为JPEG格式的字节流"""
    # frame 是一个numpy数组 (height, width, channels)
    # cv2.imencode 会将其压缩成内存中的缓冲区
    # '.jpg' 指定了压缩格式
    # retval 是一个布尔值，表示是否成功
    # buffer 是编码后的数据
    retval, buffer = cv2.imencode('.jpg', frame)
    if retval:
        return buffer.tobytes()
    return None

# --- HTTP 路由：提供主页 ---
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """当用户访问根URL (http://127.0.0.1:8000/) 时，返回index.html页面"""
    return templates.TemplateResponse("index.html", {"request": request})

# --- WebSocket 路由：处理实时视频流 ---
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """处理WebSocket连接，接收客户端请求，并实时发送视频帧"""
    await websocket.accept()
    print("WebSocket connection established.")

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera.")
        await websocket.close(code=1008, reason="Could not open camera")
        return

    try:
        while True:
            # 从摄像头读取一帧
            success, frame = cap.read()
            if not success:
                print("Failed to grab frame.")
                break

            # 在帧上运行YOLOv8推理
            results = model(frame)
            annotated_frame = results[0].plot()

            # 将处理后的帧编码为JPEG
            jpeg_bytes = encode_frame_to_jpeg(annotated_frame)

            if jpeg_bytes:
                # 通过WebSocket发送JPEG字节流到浏览器
                await websocket.send_bytes(jpeg_bytes)
            
            # 这是一个关键点！
            # 我们需要给事件循环一个机会去处理其他任务（比如接收WebSocket的断开消息）。
            # await asyncio.sleep(0.01) 效果类似于 cv2.waitKey()，但用于异步编程。
            # 它会"暂停"当前任务，让服务器能响应其他请求。
            await asyncio.sleep(0.01) 

    except WebSocketDisconnect:
        print("WebSocket connection closed by client.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cap.release()
        print("Camera released and WebSocket connection closed.")